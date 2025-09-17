# --- telas/tela_login.py ---
import tkinter as tk

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
        self.geometry("350x200")
        self.resizable(False, False)
        
        self.resultado = {'tipo': 'SAIR', 'nome': None}
        self.tipo_usuario = tk.StringVar(value="Leitor")

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
        tk.Button(frame_botoes, text="Entrar", command=self.entrar).pack(side=tk.LEFT, padx=10)
        tk.Button(frame_botoes, text="Sair", command=self.sair).pack(side=tk.LEFT, padx=10)
        frame_botoes.pack()
        
        centralizar_janela(self)

    def entrar(self):
        email = self.email_entry.get()
        self.resultado = {'tipo': self.tipo_usuario.get(), 'nome': email}
        self.destroy()

    def sair(self):
        self.resultado = {'tipo': 'SAIR', 'nome': None}
        self.destroy()