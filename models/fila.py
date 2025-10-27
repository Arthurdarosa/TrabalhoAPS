from __future__ import annotations
from datetime import datetime
from typing import List
from typing import List, TYPE_CHECKING
if TYPE_CHECKING:
    from .livro import Livro
    from .leitor import Leitor

class Fila:    
    def __init__(self, livro: Livro):
        self.livro = livro
        self.__leitores: List[Leitor] = []

    def adicionar(self, leitor: Leitor):
        self.__leitores.append(leitor)

    def proximo(self) -> Leitor | None:
        if self.__leitores:
            return self.__leitores.pop(0)
        return None

    def listar(self) -> List[Leitor]:
        return list(self.__leitores)