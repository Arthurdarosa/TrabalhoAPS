from __future__ import annotations
from datetime import datetime, timedelta
from estado import StatusEmprestimo
from .livro import Livro
from .leitor import Leitor

class Emprestimo:
    """
    Representa o ato de um Leitor pegar um Livro emprestado.
    Valida os tipos de dados e encapsula o estado.
    """
    def __init__(self, livro: Livro, leitor: Leitor):
        self.livro = livro
        self.leitor = leitor
        
        self.__data_emprestimo = datetime.now()
        self.__data_devolucao_prevista = self.__data_emprestimo + timedelta(days=14)
        
        # O status inicial agora usa o Enum
        self.status = StatusEmprestimo.PENDENTE

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
    def status(self) -> StatusEmprestimo:  # <-- Tipo de retorno atualizado
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
    def status(self, status: StatusEmprestimo): # <-- Tipo de entrada atualizado
        # A validação agora é muito mais simples e segura
        if not isinstance(status, StatusEmprestimo):
            raise TypeError("Status deve ser um membro de StatusEmprestimo Enum.")
        self.__status = status
            
    # --- Métodos de Domínio (Lógica de Negócio) ---
    def registrar_devolucao(self):
        """
        Muda o status do empréstimo para 'Devolvido'.
        """
        print(f"INFO: Registrando devolução de '{self.livro.titulo}' por '{self.leitor.nome}'.")
        # Usando o Enum
        self.status = StatusEmprestimo.DEVOLVIDO

    def verificar_atraso(self) -> bool:
        """
        Verifica se o empréstimo está atrasado e atualiza o status se necessário.
        """
        # Comparação usando o Enum
        # (Mantendo a lógica que discutimos: só fica atrasado se estava Ativo)
        if self.status == StatusEmprestimo.ATIVO and datetime.now() > self.data_devolucao_prevista:
            self.status = StatusEmprestimo.ATRASADO
            return True
        
        # Verificação usando o Enum
        return self.status == StatusEmprestimo.ATRASADO