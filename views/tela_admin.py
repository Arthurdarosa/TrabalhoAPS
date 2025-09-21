import tkinter as tk
from views.tela_cadastrar_livro import TelaCadastrarLivro
from views.tela_emprestimos_admin import TelaEmprestimosAdmin
from views.tela_gerenciar_livros import TelaGerenciarLivros
# --- Importando as novas telas de gerenciamento ---
from views.tela_gerenciar_leitores import TelaGerenciarLeitores
from views.tela_gerenciar_admins import TelaGerenciarAdmins
from views.tela_relatorios import TelaRelatorios

def centralizar_janela(janela):
    # (função de centralizar aqui)
    janela.update_idletasks()
    largura = janela.winfo_width()
    altura = janela.winfo_height()
    x = (janela.winfo_screenwidth() // 2) - (largura // 2)
    y = (janela.winfo_screenheight() // 2) - (altura // 2)
    janela.geometry(f'{largura}x{altura}+{x}+{y}')

class TelaAdmin(tk.Tk):
    def __init__(self, nome_admin: str):
        super().__init__()
        self.title("Painel Administrativo")
        self.geometry("400x550") # Mais altura para os botões
        
        tk.Label(self, text="Painel do Administrador", font=('Helvetica', 18)).pack(pady=20)
        tk.Label(self, text=f"Logado como: {nome_admin}").pack(pady=5)
        
        tk.Button(self, text="Cadastrar Livro", width=25, height=2, command=self.abrir_tela_cadastro_livro).pack(pady=5)
        tk.Button(self, text="Editar Livros", width=25, height=2, command=self.abrir_tela_gerenciar_livros).pack(pady=5)
        tk.Button(self, text="Gerenciar Leitores", width=25, height=2, command=self.abrir_tela_gerenciar_leitores).pack(pady=5)
        tk.Button(self, text="Gerenciar Administradores", width=25, height=2, command=self.abrir_tela_gerenciar_admins).pack(pady=5)
        
        tk.Button(self, text="Gerenciar Empréstimos", width=25, height=2, command=self.abrir_tela_emprestimos).pack(pady=5)
        tk.Button(self, text="Gerar Relatórios", width=25, height=2, command=self.abrir_tela_relatorios).pack(pady=5)

        tk.Button(self, text="Logout", command=self.destroy).pack(side=tk.BOTTOM, pady=20)
        centralizar_janela(self)

    # Métodos para abrir as telas de livros (já existentes)
    def abrir_tela_cadastro_livro(self):
        self.wait_window(TelaCadastrarLivro(self))
    def abrir_tela_gerenciar_livros(self):
        self.wait_window(TelaGerenciarLivros(self))
    def abrir_tela_emprestimos(self):
        self.wait_window(TelaEmprestimosAdmin(self))

    # --- NOVOS MÉTODOS ---
    def abrir_tela_gerenciar_leitores(self):
        self.wait_window(TelaGerenciarLeitores(self))
    def abrir_tela_gerenciar_admins(self):
        self.wait_window(TelaGerenciarAdmins(self))

    def abrir_tela_relatorios(self):
        tela_relatorios = TelaRelatorios(self)
        self.wait_window(tela_relatorios)