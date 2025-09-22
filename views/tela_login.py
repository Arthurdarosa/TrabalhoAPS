# --- telas/tela_login.py ---
import tkinter as tk
from tkinter import messagebox
from controllers.leitor_controller import LeitorController

def centralizar_janela(janela):
    janela.update_idletasks()
    largura = janela.winfo_width()
    altura = janela.winfo_height()
    x = (janela.winfo_screenwidth() // 2) - (largura // 2)
    y = (janela.winfo_screenheight() // 2) - (altura // 2)
    janela.geometry(f'{largura}x{altura}+{x}+{y}')

class TelaLogin(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Login - Biblioteca")
        self.geometry("350x250")
        self.resizable(False, False)
        
        self.resultado = {'tipo': 'SAIR', 'nome': None}
        self.tipo_usuario = tk.StringVar(value="Leitor")
        self.controller = LeitorController()

        tk.Label(self, text="Login - Biblioteca", font=('Helvetica', 16)).pack(pady=10)
        
        frame_tipo = tk.Frame(self)
        tk.Radiobutton(frame_tipo, text="Leitor", variable=self.tipo_usuario, value="Leitor").pack(side=tk.LEFT, padx=10)
        tk.Radiobutton(frame_tipo, text="Administrador", variable=self.tipo_usuario, value="Administrador").pack(side=tk.LEFT, padx=10)
        frame_tipo.pack()

        frame_form = tk.Frame(self)
        tk.Label(frame_form, text="Email:").grid(row=0, column=0, padx=5, pady=5)
        self.email_entry = tk.Entry(frame_form, width=30)
        self.email_entry.grid(row=0, column=1, padx=5, pady=5)
        tk.Label(frame_form, text="Senha:").grid(row=1, column=0, padx=5, pady=5)
        self.senha_entry = tk.Entry(frame_form, show="*", width=30)
        self.senha_entry.grid(row=1, column=1, padx=5, pady=5)
        frame_form.pack(pady=10)

        frame_botoes = tk.Frame(self)
        tk.Button(frame_botoes, text="Entrar", command=self.entrar).pack(side=tk.LEFT, padx=5)
        tk.Button(frame_botoes, text="Cadastrar leitor", command=self.cadastrar).pack(side=tk.LEFT, padx=5)
        tk.Button(frame_botoes, text="Sair", command=self.sair).pack(side=tk.LEFT, padx=5)
        frame_botoes.pack()
        
        centralizar_janela(self)

    def entrar(self):
        email = self.email_entry.get()
        senha = self.senha_entry.get()
        
        if not email or not senha:
            messagebox.showerror("Erro", "Email e senha são obrigatórios!")
            return
        
        # Para leitores e administradores, aceitar qualquer login por enquanto
        if self.tipo_usuario.get() == "Leitor":
            self.resultado = {'tipo': 'Leitor', 'nome': email}
            self.destroy()
        else:
            # Para administradores, manter lógica simples por enquanto
            self.resultado = {'tipo': 'Administrador', 'nome': email}
            self.destroy()

    def cadastrar(self):
        """Abre a tela de cadastro de leitores."""
        from views.tela_cadastrar_leitor import TelaCadastrarLeitor
        tela_cadastro = TelaCadastrarLeitor(self)
        self.wait_window(tela_cadastro)

    def sair(self):
        self.resultado = {'tipo': 'SAIR', 'nome': None}
        self.destroy()