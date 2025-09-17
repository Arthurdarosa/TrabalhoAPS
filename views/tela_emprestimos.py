import tkinter as tk
from tkinter import ttk

def centralizar_janela(janela):
    janela.update_idletasks()
    largura = janela.winfo_width()
    altura = janela.winfo_height()
    x = (janela.winfo_screenwidth() // 2) - (largura // 2)
    y = (janela.winfo_screenheight() // 2) - (altura // 2)
    janela.geometry(f'{largura}x{altura}+{x}+{y}')

class TelaEmprestimos(tk.Toplevel):
    def __init__(self, parent):
        super().__init__(parent)
        self.title("Meus Empréstimos")
        self.geometry("600x450")
        self.resizable(False, False)

        tk.Label(self, text="Livros Emprestados Atualmente", font=('Helvetica', 16)).pack(pady=10)

        # Frame da lista com Listbox e Scrollbar
        frame_lista = tk.Frame(self)
        frame_lista.pack(pady=10, padx=10, expand=True, fill='both')
        
        self.listbox_emprestimos = tk.Listbox(frame_lista, font=('Consolas', 10))
        self.listbox_emprestimos.pack(side=tk.LEFT, expand=True, fill='both')

        scrollbar = tk.Scrollbar(frame_lista, orient='vertical', command=self.listbox_emprestimos.yview)
        scrollbar.pack(side=tk.RIGHT, fill='y')
        self.listbox_emprestimos.config(yscrollcommand=scrollbar.set)
        
        # Botão para fechar
        tk.Button(self, text="Voltar", command=self.destroy).pack(pady=10)

        # Populando com dados de exemplo
        self.popular_lista()
        
        centralizar_janela(self)
        self.transient(parent)
        self.grab_set()

    def popular_lista(self):
        # --- LÓGICA SIMULADA ---
        # No sistema real, aqui você buscaria os empréstimos do usuário logado no banco.
        emprestimos_falsos = [
            ("O Guia do Mochileiro das Galáxias", "25/09/2025"),
            ("A Guerra dos Tronos", "02/10/2025"),
            ("O Nome do Vento", "15/10/2025")
        ]
        
        for livro, data in emprestimos_falsos:
            linha_texto = f"{livro:<45} | Devolução: {data}"
            self.listbox_emprestimos.insert(tk.END, linha_texto)