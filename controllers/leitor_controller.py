import json
import os
from typing import List, Optional
from models.leitor import Leitor

class LeitorController:
    """Controller responsável por gerenciar operações relacionadas a leitores."""
    
    def __init__(self, arquivo_dados: str = "data/leitores.json"):
        self.arquivo_dados = arquivo_dados
        self.leitores: List[Leitor] = []
        self._criar_diretorio_se_nao_existir()
        self._carregar_leitores()
    
    def _criar_diretorio_se_nao_existir(self):
        """Cria o diretório de dados se não existir."""
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
                        senha_salva = leitor_data.get('senha') or ''
                        senha_para_instanciar = senha_salva if isinstance(senha_salva, str) and len(senha_salva) >= 6 else 'placeholder123'
                        leitor = Leitor(
                            nome=leitor_data['nome'],
                            email=leitor_data['email'],
                            CPF=leitor_data['CPF'],
                            senha=senha_para_instanciar,
                            telefone=leitor_data['telefone']
                        )
                        # Restaurar o hash original
                        leitor._Usuario__senha_hash = leitor_data['senha_hash']
                        self.leitores.append(leitor)
            except (json.JSONDecodeError, KeyError, ValueError) as e:
                print(f"Erro ao carregar leitores: {e}")
                self.leitores = []
    
    def _salvar_leitores(self):
        """Salva leitores no arquivo JSON."""
        try:
            dados = []
            for leitor in self.leitores:
                dados.append({
                    'nome': leitor.nome,
                    'email': leitor.email,
                    'CPF': leitor.CPF,
                    'senha': '***',  # Não salvar senha em texto plano
                    'senha_hash': leitor._Usuario__senha_hash,
                    'telefone': leitor.telefone
                })
            
            with open(self.arquivo_dados, 'w', encoding='utf-8') as f:
                json.dump(dados, f, indent=2, ensure_ascii=False)
        except Exception as e:
            print(f"Erro ao salvar leitores: {e}")
    
    def validar_cpf(self, cpf: str) -> bool:
        """Valida CPF usando algoritmo oficial."""
        # Remove caracteres não numéricos
        cpf = ''.join(filter(str.isdigit, cpf))
        
        # Verifica se tem 11 dígitos
        if len(cpf) != 11:
            return False
        
        # Verifica se todos os dígitos são iguais
        if cpf == cpf[0] * 11:
            return False
        
        # Calcula o primeiro dígito verificador
        soma = sum(int(cpf[i]) * (10 - i) for i in range(9))
        resto = soma % 11
        digito1 = 0 if resto < 2 else 11 - resto
        
        # Calcula o segundo dígito verificador
        soma = sum(int(cpf[i]) * (11 - i) for i in range(10))
        resto = soma % 11
        digito2 = 0 if resto < 2 else 11 - resto
        
        # Verifica se os dígitos calculados coincidem com os fornecidos
        return cpf[9] == str(digito1) and cpf[10] == str(digito2)
    
    def validar_email(self, email: str) -> bool:
        """Valida formato de email."""
        import re
        pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
        return re.match(pattern, email) is not None
    
    def email_ja_existe(self, email: str) -> bool:
        """Verifica se email já está cadastrado."""
        return any(leitor.email.lower() == email.lower() for leitor in self.leitores)
    
    def cpf_ja_existe(self, cpf: str) -> bool:
        """Verifica se CPF já está cadastrado."""
        cpf_limpo = ''.join(filter(str.isdigit, cpf))
        return any(str(leitor.CPF) == cpf_limpo for leitor in self.leitores)
    
    def cadastrar_leitor(self, nome: str, email: str, cpf: str, senha: str, telefone: str) -> tuple[bool, str]:
        """
        Cadastra um novo leitor.
        Retorna (sucesso, mensagem)
        """
        try:
            # Validações
            if not nome.strip():
                return False, "Nome é obrigatório."
            
            if not self.validar_email(email):
                return False, "Email inválido."
            
            if self.email_ja_existe(email):
                return False, "Email já cadastrado."
            
            if not self.validar_cpf(cpf):
                return False, "CPF inválido."
            
            if self.cpf_ja_existe(cpf):
                return False, "CPF já cadastrado."
            
            if len(senha) < 6:
                return False, "Senha deve ter pelo menos 6 caracteres."
            
            if not telefone.strip():
                return False, "Telefone é obrigatório."
            
            # Converte CPF para int (remove formatação)
            cpf_limpo = int(''.join(filter(str.isdigit, cpf)))
            telefone_int = int(''.join(filter(str.isdigit, telefone)))
            
            # Cria o leitor
            leitor = Leitor(nome.strip(), email.strip(), cpf_limpo, senha, telefone_int)
            self.leitores.append(leitor)
            self._salvar_leitores()
            
            return True, "Leitor cadastrado com sucesso!"
            
        except ValueError as e:
            return False, f"Erro de validação: {str(e)}"
        except Exception as e:
            return False, f"Erro interno: {str(e)}"
    
    def buscar_leitor_por_email(self, email: str) -> Optional[Leitor]:
        """Busca leitor por email."""
        for leitor in self.leitores:
            if leitor.email.lower() == email.lower():
                return leitor
        return None
    
    def listar_leitores(self) -> List[Leitor]:
        """Retorna lista de todos os leitores."""
        return self.leitores.copy()

    # --- Novas operações: atualizar e excluir ---
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
        Atualiza dados de um leitor identificado pelo email_original.
        Campos None não são alterados. Senha vazia ("") também não altera.
        Retorna (sucesso, mensagem).
        """
        try:
            leitor = self.buscar_leitor_por_email(email_original)
            if not leitor:
                return False, "Leitor não encontrado."

            # Nome
            if nome is not None:
                nome_limpo = nome.strip()
                if not nome_limpo:
                    return False, "Nome é obrigatório."
                leitor.nome = nome_limpo

            # Email
            if email is not None and email.strip().lower() != email_original.strip().lower():
                if not self.validar_email(email):
                    return False, "Email inválido."
                if self.email_ja_existe(email):
                    return False, "Email já cadastrado."
                leitor.email = email.strip()

            # Telefone
            if telefone is not None:
                telefone_str = str(telefone)
                telefone_int = int(''.join(filter(str.isdigit, telefone_str)))
                leitor.telefone = telefone_int

            # Senha (opcional)
            if senha is not None and senha != "":
                if len(senha) < 6:
                    return False, "Senha deve ter pelo menos 6 caracteres."
                # Regerar hash através do construtor privado
                # Truque: criar um hash novo usando o método de verificação
                # Não há setter público, então reaproveitamos a lógica da classe base
                leitor._Usuario__senha_hash = leitor._gerar_hash(senha)

            self._salvar_leitores()
            return True, "Leitor atualizado com sucesso!"
        except ValueError as e:
            return False, f"Erro de validação: {str(e)}"
        except Exception as e:
            return False, f"Erro interno: {str(e)}"

    def excluir_leitor_por_email(self, email: str) -> tuple[bool, str]:
        """Exclui um leitor pelo email. Retorna (sucesso, mensagem)."""
        try:
            for i, leitor in enumerate(self.leitores):
                if leitor.email.lower() == email.lower():
                    del self.leitores[i]
                    self._salvar_leitores()
                    return True, "Leitor excluído com sucesso!"
            return False, "Leitor não encontrado."
        except Exception as e:
            return False, f"Erro interno: {str(e)}"