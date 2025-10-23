# controllers/leitor_controller.py
import json
import os
from typing import List, Optional
from models.leitor import Leitor # Importa o novo Leitor

class LeitorController:
    """Controller responsável por gerenciar operações relacionadas a leitores."""
    
    def __init__(self, arquivo_dados: str = "data/leitores.json"):
        self.arquivo_dados = arquivo_dados
        self.leitores: List[Leitor] = []
        self._criar_diretorio_se_nao_existir()
        self._carregar_leitores()
    
    def _criar_diretorio_se_nao_existir(self):
        # (Idêntico, sem mudanças)
        diretorio = os.path.dirname(self.arquivo_dados)
        if diretorio and not os.path.exists(diretorio):
            os.makedirs(diretorio)
    
    def _carregar_leitores(self):
        """Carrega leitores do arquivo JSON."""
        if os.path.exists(self.arquivo_dados):
            try:
                with open(self.arquivo_dados, 'r', encoding='utf-8') as f:
                    dados = json.load(f)
                    for leitor_data in dados:
                        try:
                            # Agora usamos o from_stored_data que está no Model!
                            leitor = Leitor.from_stored_data(
                                nome=leitor_data['_Usuario__nome'],
                                email=leitor_data['_Usuario__email'],
                                CPF=leitor_data['_Usuario__CPF'],
                                senha_hash=leitor_data['_Usuario__senha_hash'],
                                telefone=leitor_data['_Usuario__telefone']
                            )
                            # (Aqui viria a lógica para recarregar os empréstimos e filas)
                            self.leitores.append(leitor)
                        except (KeyError, ValueError) as e_item:
                            print(f"Registro de leitor inválido ignorado: {e_item}")
            except (json.JSONDecodeError, OSError) as e:
                print(f"Erro ao carregar arquivo de leitores: {e}")
                self.leitores = []
        
    def _salvar_leitores(self):
        """Salva leitores no arquivo JSON."""
        try:
            # vars(leitor) retorna o dicionário de atributos do objeto
            dados = [vars(leitor) for leitor in self.leitores]
            
            with open(self.arquivo_dados, 'w', encoding='utf-8') as f:
                json.dump(dados, f, indent=2, ensure_ascii=False)
        except Exception as e:
            print(f"Erro ao salvar leitores: {e}")
    
    # --- MÉTODOS DE VALIDAÇÃO REMOVIDOS ---
    # validar_cpf() -> FOI PARA O MODELO
    # validar_email() -> FOI PARA O MODELO
    
    # --- Métodos de Checagem (Ficam no Controller) ---
    
    def email_ja_existe(self, email: str) -> bool:
        """Verifica se email já está cadastrado (lógica de repositório)."""
        return any(leitor.email.lower() == email.lower() for leitor in self.leitores)
    
    def cpf_ja_existe(self, cpf: str) -> bool:
        """Verifica se CPF já está cadastrado (lógica de repositório)."""
        cpf_limpo = int(''.join(filter(str.isdigit, cpf)))
        return any(leitor.CPF == cpf_limpo for leitor in self.leitores)
    
    # --- Métodos de Caso de Uso (Refatorados) ---
    
    def cadastrar_leitor(self, nome: str, email: str, cpf: str, senha: str, telefone: str) -> tuple[bool, str]:
        """
        Cadastra um novo leitor.
        O controller agora SÓ orquestra e captura erros do Model.
        """
        try:
            if self.email_ja_existe(email):
                return False, "Email já cadastrado."
            
            if self.cpf_ja_existe(cpf):
                return False, "CPF já cadastrado."
            
            # 2. Limpeza de dados (preparação para o model)
            cpf_limpo = int(''.join(filter(str.isdigit, cpf)))
            telefone_int = int(''.join(filter(str.isdigit, telefone)))
        
            leitor = Leitor(nome, email, cpf_limpo, senha, telefone_int)
            
            # 4. Se passou, salva.
            self.leitores.append(leitor)
            self._salvar_leitores()
            
            return True, "Leitor cadastrado com sucesso!"
            
        except ValueError as e:
            # 5. Captura o erro de validação vindo do MODEL
            return False, f"{str(e)}"
        except Exception as e:
            return False, f"Erro interno: {str(e)}"
    
    def buscar_leitor_por_email(self, email: str) -> Optional[Leitor]:
        # (Idêntico, sem mudanças)
        for leitor in self.leitores:
            if leitor.email.lower() == email.lower():
                return leitor
        return None
    
    def listar_leitores(self) -> List[Leitor]:
        # (Idêntico, sem mudanças)
        return self.leitores.copy()

    def atualizar_leitor(
        self,
        email_original: str,
        *,
        nome: Optional[str] = None,
        email: Optional[str] = None,
        telefone: Optional[str | int] = None,
        senha: Optional[str] = None,
    ) -> tuple[bool, str]:
        """
        Atualiza dados de um leitor.
        A lógica de validação agora está nos SETTERS do Model.
        """
        try:
            leitor = self.buscar_leitor_por_email(email_original)
            if not leitor:
                return False, "Leitor não encontrado."

            # Tenta aplicar as mudanças.
            # Cada 'leitor.campo = valor' vai disparar o SETTER
            # do modelo, que fará a validação.
            
            if nome is not None:
                leitor.nome = nome # Dispara @nome.setter

            if email is not None and email.strip().lower() != email_original.strip().lower():
                # Checagem de repositório
                if self.email_ja_existe(email):
                    return False, "Email já cadastrado."
                leitor.email = email # Dispara @email.setter

            if telefone is not None:
                telefone_int = int(''.join(filter(str.isdigit, str(telefone))))
                leitor.telefone = telefone_int # Dispara @telefone.setter

            if senha: # Se senha não for None ou ""
                leitor.senha = senha # Dispara @senha.setter (que gera o hash)

            self._salvar_leitores()
            return True, "Leitor atualizado com sucesso!"
        
        except ValueError as e:
            # Captura erros de validação vindos dos SETTERS
            return False, f"{str(e)}"
        except Exception as e:
            return False, f"Erro interno: {str(e)}"

    def excluir_leitor_por_email(self, email: str) -> tuple[bool, str]:
        # (Idêntico, sem mudanças)
        try:
            for i, leitor in enumerate(self.leitores):
                if leitor.email.lower() == email.lower():
                    del self.leitores[i]
                    self._salvar_leitores()
                    return True, "Leitor excluído com sucesso!"
            return False, "Leitor não encontrado."
        except Exception as e:
            return False, f"Erro interno: {str(e)}"