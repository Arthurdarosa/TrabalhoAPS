import tkinter as tk
from tkinter import messagebox

def centralizar_janela(janela):
    # (código da função de centralizar aqui)
    janela.update_idletasks()
    largura = janela.winfo_width()
    altura = janela.winfo_height()
    x = (janela.winfo_screenwidth() // 2) - (largura // 2)
    y = (janela.winfo_screenheight() // 2) - (altura // 2)
    janela.geometry(f'{largura}x{altura}+{x}+{y}')

class TelaEditarLivro(tk.Toplevel):
    # O __init__ agora recebe os dados do livro para preencher o formulário
    def __init__(self, parent, dados_livro: dict):
        super().__init__(parent)
        self.title("Editar Livro")
        self.geometry("400x250")
        self.resizable(False, False)

        self.dados_atualizados = None # Para retornar os dados alterados

        # --- Widgets ---
        frame_form = tk.Frame(self)
        frame_form.pack(pady=20, padx=20)

        tk.Label(frame_form, text="Título:").grid(row=0, column=0, sticky='w', pady=5)
        self.entry_titulo = tk.Entry(frame_form, width=40)
        self.entry_titulo.grid(row=0, column=1)

        tk.Label(frame_form, text="Autor:").grid(row=1, column=0, sticky='w', pady=5)
        self.entry_autor = tk.Entry(frame_form, width=40)
        self.entry_autor.grid(row=1, column=1)

        tk.Label(frame_form, text="Gênero:").grid(row=2, column=0, sticky='w', pady=5)
        self.entry_genero = tk.Entry(frame_form, width=40)
        self.entry_genero.grid(row=2, column=1)

        tk.Label(frame_form, text="Quantidade:").grid(row=2, column=0, sticky='w', pady=5)
        self.entry_genero = tk.Entry(frame_form, width=40)
        self.entry_genero.grid(row=2, column=1)