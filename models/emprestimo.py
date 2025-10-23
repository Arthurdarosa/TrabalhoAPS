from __future__ import annotations
from datetime import datetime, timedelta
from .livro import Livro
from .leitor import Leitor

class Emprestimo:
    """
    Representa o ato de um Leitor pegar um Livro emprestado.
    Valida os tipos de dados e encapsula o estado.
    """
    def __init__(self, livro: Livro, leitor: Leitor):
        # Usamos os setters no construtor para garantir a validação na criação do objeto
        self.livro = livro
        self.leitor = leitor
        
        # Atributos de data são definidos na criação e não devem ser alterados externamente
        self.__data_emprestimo = datetime.now()
        self.__data_devolucao_prevista = self.__data_emprestimo + timedelta(days=14)
        
        # O status inicial é sempre "Ativo"
        self.estado = "pendente"

    # --- Properties (Getters) ---
    @property
    def livro(self) -> Livro:
        return self.__livro

    @property
    def leitor(self) -> Leitor:
        return self.__leitor
    
    @property
    def data_emprestimo(self) -> datetime:
        return self.__data_emprestimo
        
    @property
    def data_devolucao_prevista(self) -> datetime:
        return self.__data_devolucao_prevista

    @property
    def status(self) -> str:
        return self.__status

    # --- Setters com Validação ---
    @livro.setter
    def livro(self, livro: Livro):
        if not isinstance(livro, Livro):
            raise TypeError("Atributo 'livro' deve ser uma instância da classe Livro.")
        self.__livro = livro

    @leitor.setter
    def leitor(self, leitor: Leitor):
        if not isinstance(leitor, Leitor):
            raise TypeError("Atributo 'leitor' deve ser uma instância da classe Leitor.")
        self.__leitor = leitor
            
    @status.setter
    def status(self, status: str):
        allowed_statuses = ["Ativo", "Atrasado", "Devolvido", "pendente"]
        if isinstance(status, str) and status in allowed_statuses:
            self.__status = status
        else:
            raise ValueError(f"Status inválido. Permitidos: {allowed_statuses}")
            
    # --- Métodos de Domínio (Lógica de Negócio) ---
    def registrar_devolucao(self):
        """
        Muda o status do empréstimo para 'Devolvido'.
        Este método de negócio usa o setter para garantir a regra de validação.
        """
        print(f"INFO: Registrando devolução de '{self.livro.titulo}' por '{self.leitor.nome}'.")
        self.status = "Devolvido"

    def verificar_atraso(self) -> bool:
        """
        Verifica se o empréstimo está atrasado e atualiza o status se necessário.
        """
        if self.status == "Ativo" and datetime.now() > self.data_devolucao_prevista:
            self.status = "Atrasado"
            return True
        return self.status == "Atrasado"