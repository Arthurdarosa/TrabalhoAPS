from enum import Enum, auto

class StatusEmprestimo(Enum):
    """ Define os estados possíveis de um empréstimo. """
    PENDENTE = auto()
    ATIVO = auto()
    ATRASADO = auto()
    DEVOLVIDO = auto()
    
