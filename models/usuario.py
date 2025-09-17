class Usuario:
    """Classe base que representa um usuário do sistema."""
    def __init__(self, nome: str, email: str, CPF: int, senha: str, tipo: str):
        self.nome = nome
        self.email = email
        self.CPF = CPF
        self.__senha_hash = self._gerar_hash(senha)
        self.tipo = tipo

    @property
    def nome(self) -> str:
        return self.__nome
        
    @nome.setter
    def nome(self, nome: str):
        if isinstance(nome, str) and nome.strip():
            self.__nome = nome
        else:
            raise ValueError("Nome deve ser uma string não vazia.")

    # ... (outros getters e setters para email, tipo, e a propriedade de senha_hash) ...

    def _gerar_hash(self, senha: str) -> str:
        if isinstance(senha, str) and len(senha) >= 6:
            return f"hashed_{senha}_salt"
        else:
            raise ValueError("Senha deve ser uma string com pelo menos 6 caracteres.")

    def verificar_senha(self, senha_fornecida: str) -> bool:
        return self.__senha_hash == self._gerar_hash(senha_fornecida)