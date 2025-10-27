import json
import os
from datetime import datetime
from models.emprestimo import Emprestimo
from models.livro import Livro           # Precisa saber o que é um Livro
from models.leitor import Leitor         # Precisa saber o que é um Leitor
from models.estado import StatusEmprestimo # Precisa saber o que é um StatusEmprestimo

class SistemaController:
    """
    Controller principal que gerencia os dados do sistema.
    Carrega dados de arquivos JSON ao iniciar.
    """
    def __init__(self):
        BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
        # Garantindo que o nome do arquivo está correto (singular, como você pediu)
        self.PATH_EMPRESTIMOS = os.path.join(BASE_DIR, 'data', 'emprestimo.json')

        self.emprestimos = self._carregar_emprestimos()
        
        print("------------------------------------------")
        print(f"Controller iniciado. {len(self.emprestimos)} empréstimos carregados.")
        for emp in self.emprestimos:
             print(f"  -> ID: {emp.id}, Livro: {emp.livro.titulo}, Status: {emp.status.value}")
        print("------------------------------------------")


    def _carregar_emprestimos(self) -> list[Emprestimo]:
        """Carrega e "recria" os empréstimos do JSON denormalizado."""
        lista_obj_emprestimos = []
        max_id = 0
        try:
            with open(self.PATH_EMPRESTIMOS, 'r', encoding='utf-8') as f:
                lista_de_dicts = json.load(f)

            for data_dict in lista_de_dicts:
                livro_data = data_dict.get('livro')
                leitor_data = data_dict.get('leitor')

                if not livro_data or not leitor_data:
                    print(f"AVISO: Ignorando empréstimo ID {data_dict.get('id')}. 'livro' ou 'leitor' faltando no JSON.")
                    continue

                # 1. Crie a CÓPIA do Livro a partir dos dados embutidos
                try:
                    livro_obj = Livro(
                        titulo=livro_data.get("_Livro__titulo"),
                        autor=livro_data.get("_Livro__autor"),
                        genero=livro_data.get("_Livro__genero"),
                        quantidade_total=int(livro_data.get("_Livro__quantidade_total"))
                    )
                except Exception as e:
                    print(f"ERRO ao recriar Livro para Empréstimo {data_dict.get('id')}: {e}")
                    continue # Pula este empréstimo
                
                # 2. Crie a CÓPIA do Leitor a partir dos dados embutidos
                try:
                    # Usando o método from_stored_data herdado de Usuario
                    leitor_obj = Leitor.from_stored_data(
                        nome=leitor_data.get("_Usuario__nome"),
                        email=leitor_data.get("_Usuario__email"),
                        CPF=int(leitor_data.get("_Usuario__CPF")),
                        senha_hash="dummy_hash",  # Hash dummy já que não temos o original
                        telefone=int(leitor_data.get("_Usuario__telefone"))
                    )
                    # Inicializar os atributos específicos de Leitor que não são herdados de Usuario
                    leitor_obj._Leitor__livros_emprestados = []
                    leitor_obj._Leitor__fila_de_espera = []
                except Exception as e:
                    print(f"ERRO ao recriar Leitor para Empréstimo {data_dict.get('id')}: {e}")
                    continue # Pula este empréstimo

                # 3. Crie o Emprestimo com os objetos-cópia
                emp = Emprestimo(livro=livro_obj, leitor=leitor_obj)

                # 4. Sobreponha os dados do JSON (ID, status, datas)
                emp_id = int(data_dict['id'])
                emp.id = emp_id # Sobrepõe o ID
                emp.status = StatusEmprestimo[data_dict['status']] # Usa colchetes para acessar pelo nome

                data_emp_str = data_dict.get('data_emprestimo')
                data_dev_str = data_dict.get('data_devolucao_prevista')

                # Usando "name mangling" para setar os atributos privados
                emp._Emprestimo__data_emprestimo = datetime.fromisoformat(data_emp_str) if data_emp_str else None
                emp._Emprestimo__data_devolucao_prevista = datetime.fromisoformat(data_dev_str) if data_dev_str else None
                
                lista_obj_emprestimos.append(emp)
                
                if emp_id > max_id:
                    max_id = emp_id

            # 5. Atualize o contador global de IDs
            proximo_id = max_id + 1
            print(f"INFO: Carregados {len(lista_obj_emprestimos)} empréstimos. Próximo ID será {proximo_id}.")

        except FileNotFoundError:
            print(f"AVISO: Arquivo {self.PATH_EMPRESTIMOS} não encontrado. Usando lista vazia.")
        except json.JSONDecodeError:
            print(f"ERRO: O arquivo {self.PATH_EMPRESTIMOS} está vazio ou mal formatado. Usando lista vazia.")
        except Exception as e:
            print(f"ERRO inesperado ao carregar empréstimos: {e}.")
            
        return lista_obj_emprestimos

    
    def _salvar_emprestimos(self):
        """Salva empréstimos no arquivo JSON."""
        try:
            lista_dicts = []
            for emp in self.emprestimos:
                # Serializa manualmente o livro (sem Fila e Avaliações)
                livro_dict = {
                    "_Livro__titulo": emp.livro.titulo,
                    "_Livro__autor": emp.livro.autor,
                    "_Livro__genero": emp.livro.genero,
                    "_Livro__quantidade_total": emp.livro.quantidade_total
                }
                
                # Serializa manualmente o leitor
                leitor_dict = {
                    "_Usuario__nome": emp.leitor.nome,
                    "_Usuario__email": emp.leitor.email,
                    "_Usuario__CPF": emp.leitor.CPF,
                    "_Usuario__telefone": emp.leitor.telefone
                }
                
                # Serializa cada empréstimo para JSON
                emp_dict = {
                    "id": emp.id,
                    "status": emp.status.name,  # .name pega o nome da string do enum
                    "data_emprestimo": emp.data_emprestimo.isoformat() if emp.data_emprestimo else None,
                    "data_devolucao_prevista": emp.data_devolucao_prevista.isoformat() if emp.data_devolucao_prevista else None,
                    "livro": livro_dict,
                    "leitor": leitor_dict
                }
                lista_dicts.append(emp_dict)
            
            with open(self.PATH_EMPRESTIMOS, 'w', encoding='utf-8') as f:
                json.dump(lista_dicts, f, indent=2, ensure_ascii=False)
            
            print(f"INFO: {len(lista_dicts)} empréstimos salvos no arquivo.")
        except Exception as e:
            print(f"ERRO ao salvar empréstimos: {e}")
    
    def buscar_emprestimo_por_id(self, emprestimo_id: int) -> Emprestimo | None:
        """
        Busca um empréstimo na "base de dados" pelo seu ID.
        """
        print(f"CONTROLLER: Buscando Empréstimo ID {emprestimo_id}")
        for emp in self.emprestimos:
            if emp.id == emprestimo_id:
                return emp
        return None

    def registrar_coleta(self, emprestimo_id: int) -> Emprestimo:
        """
        Lógica de negócio para registrar a coleta.
        """
        print(f"CONTROLLER: Tentando registrar coleta do ID {emprestimo_id}")
        emprestimo = self.buscar_emprestimo_por_id(emprestimo_id)
        
        if not emprestimo:
            raise ValueError(f"Empréstimo com ID {emprestimo_id} não encontrado.")
            
        emprestimo.ativar_coleta() 
        self._salvar_emprestimos()  # Salva as mudanças no arquivo
        return emprestimo