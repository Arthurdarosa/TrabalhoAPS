class Usuario:
    """Classe base que representa um usuário do sistema."""
    def __init__(self, nome: str, email: str, CPF: int, senha: str, telefone: int):
        self.nome = nome
        self.email = email
        self.CPF = CPF
        self.__senha_hash = self._gerar_hash(senha)
        self.telefone = telefone
    
    @classmethod
    def from_stored_data(cls, nome: str, email: str, CPF: int, senha_hash: str, telefone: int):
        usuario = cls.__new__(cls) 
        usuario.nome = nome
        usuario.email = email
        usuario.CPF = CPF
        usuario.__senha_hash = senha_hash 
        usuario.telefone = telefone
        return usuario

    @property
    def nome(self) -> str:
        return self.__nome
        
    @nome.setter
    def nome(self, nome: str):
        if isinstance(nome, str) and nome.strip():
            self.__nome = nome
        else:
            raise ValueError("Nome deve ser uma string não vazia.")

    @property
    def email(self) -> str:
        return self.__email
        
    @email.setter
    def email(self, email: str):
        if isinstance(email, str) and email.strip() and "@" in email:
            self.__email = email
        else:
            raise ValueError("Email deve ser uma string válida.")

    @property
    def CPF(self) -> int:
        return self.__CPF
        
    @CPF.setter
    def CPF(self, CPF: int):
        if isinstance(CPF, int) and CPF > 0:
            self.__CPF = CPF
        else:
            raise ValueError("CPF deve ser um número inteiro positivo.")

    @property
    def telefone(self) -> int:
        return self.__telefone
        
    @telefone.setter
    def telefone(self, telefone: int):
        if isinstance(telefone, int) and telefone > 0:
            self.__telefone = telefone
        else:
            raise ValueError("Telefone deve ser um número inteiro positivo.")

    def _gerar_hash(self, senha: str) -> str:
        if isinstance(senha, str) and len(senha) >= 6:
            return f"hashed_{senha}_salt"
        else:
            raise ValueError("Senha deve ser uma string com pelo menos 6 caracteres.")

    def verificar_senha(self, senha_fornecida: str) -> bool:
        return self.__senha_hash == self._gerar_hash(senha_fornecida)