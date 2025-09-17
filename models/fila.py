from __future__ import annotations
from datetime import datetime
from livro import Livro
from leitor import Leitor

class Fila:
    """Representa a posição de um leitor na fila de espera de um livro."""
    def __init__(self, livro: Livro, leitor: Leitor):
        self.livro = livro
        self.leitor = leitor
        self.__data_entrada_fila = datetime.now() # Nome do atributo alterado
        self.posicao = 0
        self.status = "Aguardando"
    
    # ... (implementar getters e setters para todos os atributos, seguindo o padrão) ...
    @property
    def livro(self):
        return self.__livro
    
    @livro.setter
    def livro(self, livro):
        if not isinstance(livro, Livro): raise TypeError("Deve ser do tipo Livro")
        self.__livro = livro
    
