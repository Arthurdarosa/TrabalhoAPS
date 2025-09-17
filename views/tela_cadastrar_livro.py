import tkinter as tk
from tkinter import messagebox

def centralizar_janela(janela):
    janela.update_idletasks()
    largura = janela.winfo_width()
    altura = janela.winfo_height()
    x = (janela.winfo_screenwidth() // 2) - (largura // 2)
    y = (janela.winfo_screenheight() // 2) - (altura // 2)
    janela.geometry(f'{largura}x{altura}+{x}+{y}')

class TelaCadastrarLivro(tk.Toplevel):
    def __init__(self, parent):
        super().__init__(parent)
        self.title("Cadastrar Novo Livro")
        self.geometry("400x250")
        self.resizable(False, False)

        # Usando .grid para alinhar labels e campos de entrada
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

        tk.Label(frame_form, text="Quantidade:").grid(row=3, column=0, sticky='w', pady=5)
        self.entry_qtd = tk.Entry(frame_form, width=10)
        self.entry_qtd.grid(row=3, column=1, sticky='w')

        # Botões de ação
        frame_botoes = tk.Frame(self)
        frame_botoes.pack(pady=10)
        tk.Button(frame_botoes, text="Salvar", command=self.salvar_livro).pack(side=tk.LEFT, padx=10)
        tk.Button(frame_botoes, text="Voltar", command=self.destroy).pack(side=tk.LEFT, padx=10)
        
        centralizar_janela(self)
        self.transient(parent)
        self.grab_set()

    def salvar_livro(self):
        # --- LÓGICA SIMULADA ---
        titulo = self.entry_titulo.get()
        autor = self.entry_autor.get()
        
        # Aqui você pegaria os dados e os enviaria para o controlador salvar no banco
        print(f"Salvando livro: Título='{titulo}', Autor='{autor}'")
        messagebox.showinfo("Sucesso", f"Livro '{titulo}' cadastrado com sucesso!")
        
        self.destroy() # Fecha a janela após salvar