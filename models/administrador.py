from usuario import Usuario

class Administrador(Usuario):
    """Um usuário com privilégios de administrador."""
    def __init__(self, nome: str, email: str, senha: str):
        super().__init__(nome, email, senha, tipo='Administrador')