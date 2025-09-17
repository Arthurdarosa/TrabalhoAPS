import tkinter as tk
# Importando as novas telas
from views.tela_cadastrar_livro import TelaCadastrarLivro
from views.tela_gerenciar_usuarios import TelaGerenciarUsuarios
from views.tela_emprestimos_admin import TelaEmprestimosAdmin
from views.tela_gerenciar_livros import TelaGerenciarLivros

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
        self.geometry("400x350") # Aumentei um pouco a altura
        
        tk.Label(self, text="Painel do Administrador", font=('Helvetica', 18)).pack(pady=20)
        tk.Label(self, text=f"Logado como: {nome_admin}").pack(pady=5)
        

        tk.Button(self, text="Cadastrar Livro", width=25, height=2, command=self.abrir_tela_cadastro_livro).pack(pady=5)
        tk.Button(self, text="gerenciar Livro", width=25, height=2, command=self.abrir_tela_gerenciar_livros).pack(pady=5)
        tk.Button(self, text="Gerenciar Usuários", width=25, height=2, command=self.abrir_tela_gerenciar_usuarios).pack(pady=5)
        tk.Button(self, text="Gerenciar Empréstimos", width=25, height=2, command=self.abrir_tela_emprestimos).pack(pady=5)
        
        tk.Button(self, text="Logout", command=self.destroy).pack(side=tk.BOTTOM, pady=20)
        centralizar_janela(self)

    # --- NOVOS MÉTODOS para abrir cada janela ---
    def abrir_tela_cadastro_livro(self):
        tela_cadastro = TelaCadastrarLivro(self)
        self.wait_window(tela_cadastro)

    def abrir_tela_gerenciar_usuarios(self):
        tela_usuarios = TelaGerenciarUsuarios(self)
        self.wait_window(tela_usuarios)

    def abrir_tela_emprestimos(self):
        tela_emprestimos = TelaEmprestimosAdmin(self)
        self.wait_window(tela_emprestimos)

    def abrir_tela_gerenciar_livros(self):
        tela_livros = TelaGerenciarLivros(self)
        self.wait_window(tela_livros)