from __future__ import annotations
from typing import List
from avaliacao import Avaliacao

class Livro:
    """Representa um livro no acervo da biblioteca."""
    def __init__(self, titulo: str, autor: str, genero: str, quantidade_total: int):
        self.titulo = titulo
        self.autor = autor
        self.genero = genero
        self.quantidade_total = quantidade_total
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

    # ... (outros getters e setters como na versão anterior) ...
    # (Omitidos aqui por brevidade, mas devem ser incluídos)

    def adicionar_avaliacao(self, avaliacao: Avaliacao):
        if not isinstance(avaliacao, Avaliacao):
            raise TypeError("Deve ser uma instância de Avaliacao.")
        self.__avaliacoes.append(avaliacao)

    def media_avaliacoes(self) -> float:
        if not self.__avaliacoes: return 0.0
        return round(sum(av.nota for av in self.__avaliacoes) / len(self.__avaliacoes), 2)
