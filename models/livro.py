from __future__ import annotations
from typing import List
from avaliacao import Avaliacao
from fila import Fila

class Livro:
    """Representa um livro no acervo da biblioteca."""
    def __init__(self, titulo: str, autor: str, genero: str, quantidade_total: int):
        self.titulo = titulo
        self.autor = autor
        self.genero = genero
        self.quantidade_total = quantidade_total
        self.__fila = Fila(self)
        self.__avaliacoes: List[Avaliacao] = []

    @property
    def titulo(self) -> str:
        return self.__titulo

    @titulo.setter
    def titulo(self, titulo: str):
        if isinstance(titulo, str) and titulo.strip():
            self.__titulo = titulo
        else:
            raise ValueError("Título deve ser uma string não vazia.")


    @property
    def autor(self) -> str:
        return self.__autor

    @autor.setter
    def autor(self, autor: str):
        if isinstance(autor, str) and autor.strip():
            self.__autor = autor
        else:
            raise ValueError("Autor deve ser uma string não vazia.")
        

    @property
    def genero(self) -> str:
        return self.__genero

    @genero.setter
    def genero(self, genero: str):
        if isinstance(genero, str) and genero.strip():
            self.__genero = genero
        else:
            raise ValueError("Genero deve ser uma string não vazia.")


    @property
    def quantidade_total(self) -> str:
        return self.__quantidade_total

    @quantidade_total.setter
    def quantidade_total(self, quantidade_total: str):
        if isinstance(quantidade_total, str) and quantidade_total.strip():
            self.__quantidade_total = quantidade_total
        else:
            raise ValueError("quantidade total deve ser um int.")



    def adicionar_avaliacao(self, avaliacao: Avaliacao):
        if not isinstance(avaliacao, Avaliacao):
            raise TypeError("Deve ser uma instância de Avaliacao.")
        self.__avaliacoes.append(avaliacao)

    def media_avaliacoes(self) -> float:
        if not self.__avaliacoes: return 0.0
        return round(sum(av.nota for av in self.__avaliacoes) / len(self.__avaliacoes), 2)
