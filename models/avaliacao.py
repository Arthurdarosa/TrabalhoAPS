from __future__ import annotations
from datetime import datetime
from typing import List, TYPE_CHECKING

if TYPE_CHECKING:
    from .leitor import Leitor
    from .livro import Livro

class Avaliacao:
    """
    Representa uma avaliação (nota e comentário) feita por um Leitor a um Livro.
    """
    def __init__(self, leitor: Leitor, livro: Livro, nota: int, comentario: str):
        # Validação delegada para os setters
        self.leitor = leitor
        self.livro = livro
        self.nota = nota
        self.comentario = comentario
        
        # A data é definida na criação e não pode ser alterada
        self.__data = datetime.now()

    # --- Properties (Getters) ---
    @property
    def leitor(self) -> Leitor:
        return self.__leitor

    @property
    def livro(self) -> Livro:
        return self.__livro
        
    @property
    def nota(self) -> int:
        return self.__nota

    @property
    def comentario(self) -> str:
        return self.__comentario

    @property
    def data(self) -> datetime:
        return self.__data

    # --- Setters com Validação ---
    @leitor.setter
    def leitor(self, leitor: Leitor):
        if not isinstance(leitor, Leitor):
            raise TypeError("Atributo 'leitor' deve ser uma instância da classe Leitor.")
        self.__leitor = leitor

    @livro.setter
    def livro(self, livro: Livro):
        if not isinstance(livro, Livro):
            raise TypeError("Atributo 'livro' deve ser uma instância da classe Livro.")
        self.__livro = livro

    @nota.setter
    def nota(self, nota: int):
        if isinstance(nota, int) and 1 <= nota <= 5:
            self.__nota = nota
        else:
            raise ValueError("A nota deve ser um número inteiro entre 1 e 5.")

    @comentario.setter
    def comentario(self, comentario: str):
        if not isinstance(comentario, str):
            raise TypeError("O comentário deve ser uma string.")
        self.__comentario = comentario

    # --- Métodos de Domínio ---
    def alterar(self, nova_nota: int, novo_comentario: str):
        """
        Permite que um usuário altere sua avaliação.
        A lógica de negócio re-utiliza os setters para garantir a validação.
        """
        print(f"INFO: Alterando avaliação do livro '{self.livro.titulo}'.")
        self.nota = nova_nota
        self.comentario = novo_comentario