from __future__ import annotations
from typing import List
from usuario import Usuario
from emprestimo import Emprestimo
from fila import Fila

class Leitor(Usuario):
    """Um usuário que pode emprestar, reservar e avaliar livros."""
    def __init__(self, nome: str, email: str, CPF: int, senha: str):
        super().__init__(nome, email, senha, tipo='Leitor')
        self.__livros_emprestados: List[Emprestimo] = []
        self.__fila_de_espera: List[Fila] = [] # Alterado de 'reservas' para 'fila_de_espera'

    @property
    def livros_emprestados(self) -> List[Emprestimo]:
        return self.__livros_emprestados

    @property
    def fila_de_espera(self) -> List[Fila]:
        return self.__fila_de_espera

