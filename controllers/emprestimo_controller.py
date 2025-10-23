from datetime import date, timedelta
from models.emprestimo import Emprestimo

class EmprestimoController:
    
    def __init__(self, repositorio_livros, repositorio_leitores, repositorio_emprestimos):
        self.repositorio_livros = repositorio_livros
        self.repositorio_leitores = repositorio_leitores
        self.repositorio_emprestimos = repositorio_emprestimos

    # --------------------------------------------
    # UC10 – Efetuar Empréstimo
    # --------------------------------------------
    def efetuar_emprestimo(self, leitor_cpf: int, livro_id: int):
        leitor = self.repositorio_leitores.buscar_por_cpf(leitor_cpf)
        livro = self.repositorio_livros.buscar_por_id(livro_id)

        if not leitor:
            raise ValueError("Leitor não encontrado.")
        if not livro:
            raise ValueError("Livro não encontrado.")
        if not livro.esta_disponivel:
            raise ValueError("Livro não está disponível para empréstimo.")

        # Criar novo empréstimo
        novo_emprestimo = Emprestimo(
            id=self.repositorio_emprestimos.gerar_novo_id(),
            leitor=leitor,
            livro=livro,
            data_emprestimo=date.today(),
            data_devolucao_prevista=date.today() + timedelta(days=7),
            estado="ativo"
        )

        # Atualiza estados e salva
        livro.esta_disponivel = False
        self.repositorio_livros.salvar(livro)
        self.repositorio_emprestimos.adicionar(novo_emprestimo)

        return novo_emprestimo

    # --------------------------------------------
    # UC11 – Registrar Devolução
    # --------------------------------------------
    def registrar_devolucao(self, emprestimo_id: int):
        emprestimo = self.repositorio_emprestimos.buscar_por_id(emprestimo_id)
        if not emprestimo:
            raise ValueError("Empréstimo não encontrado.")

        if emprestimo.estado == "finalizado":
            raise ValueError("Empréstimo já foi finalizado.")

        # Atualiza estado
        emprestimo.estado = "finalizado"
        emprestimo.data_devolucao_real = date.today()

        # Atualiza o livro
        emprestimo.livro.esta_disponivel = True
        self.repositorio_livros.salvar(emprestimo.livro)
        self.repositorio_emprestimos.salvar(emprestimo)

        return emprestimo

    # --------------------------------------------
    # Consultar empréstimos de um leitor
    # --------------------------------------------
    def consultar_emprestimos_por_leitor(self, leitor_id: int):
        leitor = self.repositorio_leitores.buscar_por_id(leitor_id)
        if not leitor:
            raise ValueError("Leitor não encontrado.")
        
        return self.repositorio_emprestimos.buscar_por_leitor(leitor_id)

    # --------------------------------------------
    # Consultar empréstimos pendentes (para tela do admin)
    # --------------------------------------------
    def listar_pendentes_para_confirmacao(self):
        """Retorna todos os empréstimos com estado 'pendente'."""
        return [
            e for e in self.repositorio_emprestimos.listar_todos()
            if e.estado == "pendente"
        ]

    def confirmar_retirada(self, emprestimo_id: int):
        """Confirma a retirada do livro reservada pelo leitor."""
        emprestimo = self.repositorio_emprestimos.buscar_por_id(emprestimo_id)
        if not emprestimo:
            raise ValueError("Empréstimo não encontrado.")

        if emprestimo.estado != "pendente":
            raise ValueError("Somente empréstimos pendentes podem ser confirmados.")

        emprestimo.estado = "ativo"
        emprestimo.data_emprestimo = date.today()
        emprestimo.data_devolucao_prevista = date.today() + timedelta(days=7)

        emprestimo.livro.esta_disponivel = False
        self.repositorio_livros.salvar(emprestimo.livro)
        self.repositorio_emprestimos.salvar(emprestimo)

        return emprestimo