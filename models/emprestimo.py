# emprestimo.py
from __future__ import annotations
from datetime import datetime, timedelta
from .estado import StatusEmprestimo
from .livro import Livro  # Importando o mock
from .leitor import Leitor # Importando o mock
import itertools # Para gerar IDs únicos

# Contador simples para IDs de empréstimo (simulando um AUTO_INCREMENT)
id_counter = itertools.count(1)

class Emprestimo:
    def __init__(self, livro: Livro, leitor: Leitor):
        
        # --- NOVO: ID do Empréstimo ---
        self.id = next(id_counter) 
        
        self.livro = livro
        self.leitor = leitor
        
        # A data de empréstimo SÓ SERÁ DEFINIDA NA COLETA
        self.__data_emprestimo = None
        self.__data_devolucao_prevista = None
        
        # O status inicial é PENDENTE (aguardando coleta)
        self.status = StatusEmprestimo.PENDENTE

    # ... (properties de livro e leitor não mudam) ...
    
    @property
    def livro(self) -> Livro:
        return self.__livro

    @property
    def leitor(self) -> Leitor:
        return self.__leitor
    
    @property
    def data_emprestimo(self) -> datetime | None: # Pode ser None
        return self.__data_emprestimo
        
    @property
    def data_devolucao_prevista(self) -> datetime | None: # Pode ser None
        return self.__data_devolucao_prevista

    @property
    def status(self) -> StatusEmprestimo:
        return self.__status

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
    def status(self, status: StatusEmprestimo):
        if not isinstance(status, StatusEmprestimo):
            raise TypeError("Status deve ser um membro de StatusEmprestimo Enum.")
        self.__status = status
            
    # --- NOVO MÉTODO DE NEGÓCIO ---
    def ativar_coleta(self):
        """
        Confirma a coleta do livro pelo leitor.
        Muda o status para ATIVO e define as datas de empréstimo.
        """
        if self.status != StatusEmprestimo.PENDENTE:
            raise ValueError(f"Este empréstimo não está pendente. Status atual: {self.status.value}")
            
        print(f"INFO: Ativando coleta do Empréstimo ID {self.id}...")
        self.status = StatusEmprestimo.ATIVO
        self.__data_emprestimo = datetime.now()
        self.__data_devolucao_prevista = self.__data_emprestimo + timedelta(days=14)
        print(f"INFO: Empréstimo {self.id} agora está ATIVO. Devolução em: {self.__data_devolucao_prevista.strftime('%d/%m/%Y')}")

    def registrar_devolucao(self):
        # ... (seu método original) ...
        self.status = StatusEmprestimo.DEVOLVIDO

    def verificar_atraso(self) -> bool:
        # ... (seu método original) ...
        if self.status == StatusEmprestimo.ATIVO and datetime.now() > self.data_devolucao_prevista:
            self.status = StatusEmprestimo.ATRASADO
            return True
        return self.status == StatusEmprestimo.ATRASADO