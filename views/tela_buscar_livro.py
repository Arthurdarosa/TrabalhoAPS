import tkinter as tk
from tkinter import ttk 

def centralizar_janela(janela):
    janela.update_idletasks()
    largura = janela.winfo_width()
    altura = janela.winfo_height()
    x = (janela.winfo_screenwidth() // 2) - (largura // 2)
    y = (janela.winfo_screenheight() // 2) - (altura // 2)
    janela.geometry(f'{largura}x{altura}+{x}+{y}')

class TelaBuscarLivro(tk.Toplevel):
    def __init__(self, parent):
        super().__init__(parent)
        self.title("Buscar Livro por Nome")
        self.geometry("500x400")
        self.resizable(False, False)

        # Frame de busca
        frame_busca = tk.Frame(self)
        frame_busca.pack(pady=10, padx=10, fill='x')

        tk.Label(frame_busca, text="Nome do Livro:").pack(side=tk.LEFT, padx=(0, 5))
        self.entry_busca = tk.Entry(frame_busca)
        self.entry_busca.pack(side=tk.LEFT, expand=True, fill='x', padx=5)
        tk.Button(frame_busca, text="Buscar", command=self.buscar_livros).pack(side=tk.LEFT)
        
        # Frame de resultados com Listbox e Scrollbar
        frame_resultados = tk.Frame(self)
        frame_resultados.pack(pady=10, padx=10, expand=True, fill='both')

        self.listbox_resultados = tk.Listbox(frame_resultados)
        self.listbox_resultados.pack(side=tk.LEFT, expand=True, fill='both')
        
        scrollbar = tk.Scrollbar(frame_resultados, orient='vertical', command=self.listbox_resultados.yview)
        scrollbar.pack(side=tk.RIGHT, fill='y')
        self.listbox_resultados.config(yscrollcommand=scrollbar.set)

        # Botão para fechar
        tk.Button(self, text="Voltar", command=self.destroy).pack(pady=10)
        
        centralizar_janela(self)
        self.transient(parent)
        self.grab_set()

    def buscar_livros(self):
        # Limpa a lista de resultados anteriores
        self.listbox_resultados.delete(0, tk.END)

        termo_busca = self.entry_busca.get()
        
        # --- LÓGICA SIMULADA ---
        # No sistema real, aqui você faria a busca no banco de dados.
        print(f"Buscando por livros que contenham: '{termo_busca}'")
        
        # Adicionando resultados de exemplo
        resultados_falsos = [
            "Duna - Frank Herbert",
            "O Senhor dos Anéis - J.R.R. Tolkien",
            "Fundação - Isaac Asimov",
            "Neuromancer - William Gibson"
        ]
        
        for resultado in resultados_falsos:
            if termo_busca.lower() in resultado.lower():
                self.listbox_resultados.insert(tk.END, resultado)