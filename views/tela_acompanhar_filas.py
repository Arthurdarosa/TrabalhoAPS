import tkinter as tk
from tkinter import ttk

def centralizar_janela(janela):
    # (função de centralizar aqui)
    janela.update_idletasks()
    largura = janela.winfo_width()
    altura = janela.winfo_height()
    x = (janela.winfo_screenwidth() // 2) - (largura // 2)
    y = (janela.winfo_screenheight() // 2) - (altura // 2)
    janela.geometry(f'{largura}x{altura}+{x}+{y}')

class TelaAcompanharFilas(tk.Toplevel):
    def __init__(self, parent):
        super().__init__(parent)
        self.title("Minhas Filas de Espera")
        self.geometry("500x400")
        self.resizable(False, False)

        tk.Label(self, text="Acompanhe sua Posição nas Filas", font=('Helvetica', 16)).pack(pady=10)

        # Frame da lista com Listbox
        frame_lista = tk.Frame(self)
        frame_lista.pack(pady=10, padx=10, expand=True, fill='both')
        
        self.listbox_filas = tk.Listbox(frame_lista, font=('Consolas', 10))
        self.listbox_filas.pack(side=tk.LEFT, expand=True, fill='both')

        scrollbar = tk.Scrollbar(frame_lista, orient='vertical', command=self.listbox_filas.yview)
        scrollbar.pack(side=tk.RIGHT, fill='y')
        self.listbox_filas.config(yscrollcommand=scrollbar.set)
        
        tk.Button(self, text="Voltar", command=self.destroy).pack(pady=10)

        # Populando a lista com dados de exemplo
        self.popular_lista()
        
        centralizar_janela(self)
        self.transient(parent)
        self.grab_set()

    def popular_lista(self):
        # --- LÓGICA SIMULADA ---
        # No sistema real, você buscaria as filas do usuário logado no banco de dados.
        filas_falsas = [
            ("O Guia do Mochileiro das Galáxias", 2),
            ("A Dança dos Dragões", 5),
            ("Duna: Messias", 1)
        ]
        
        self.listbox_filas.insert(tk.END, f"{'LIVRO':<40} | {'SUA POSIÇÃO'}")
        self.listbox_filas.insert(tk.END, "-"*60)

        for livro, posicao in filas_falsas:
            linha_texto = f"{livro:<40} | {posicao}º na fila"
            self.listbox_filas.insert(tk.END, linha_texto)