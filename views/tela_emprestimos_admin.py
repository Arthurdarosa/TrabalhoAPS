import tkinter as tk
from tkinter import messagebox

def centralizar_janela(janela):
    # (função de centralizar aqui)
    janela.update_idletasks()
    largura = janela.winfo_width()
    altura = janela.winfo_height()
    x = (janela.winfo_screenwidth() // 2) - (largura // 2)
    y = (janela.winfo_screenheight() // 2) - (altura // 2)
    janela.geometry(f'{largura}x{altura}+{x}+{y}')

class TelaEmprestimosAdmin(tk.Toplevel):
    def __init__(self, parent):
        super().__init__(parent)
        self.title("Todos os Empréstimos")
        self.geometry("600x400")

        tk.Label(self, text="Lista de Empréstimos Ativos", font=('Helvetica', 16)).pack(pady=10)

        frame_lista = tk.Frame(self)
        frame_lista.pack(pady=10, padx=10, expand=True, fill='both')
        
        self.listbox_emprestimos = tk.Listbox(frame_lista, font=('Consolas', 10))
        self.listbox_emprestimos.pack(side=tk.LEFT, expand=True, fill='both')

        scrollbar = tk.Scrollbar(frame_lista, orient='vertical', command=self.listbox_emprestimos.yview)
        scrollbar.pack(side=tk.RIGHT, fill='y')
        self.listbox_emprestimos.config(yscrollcommand=scrollbar.set)
        
        frame_botoes = tk.Frame(self)
        frame_botoes.pack(pady=10)
        tk.Button(frame_botoes, text="Marcar como Devolvido", command=self.funcao_placeholder).pack(side=tk.LEFT, padx=5)
        tk.Button(self, text="Voltar", command=self.destroy).pack(pady=5)
        
        self.popular_lista()
        centralizar_janela(self)
        self.transient(parent)
        self.grab_set()

    def popular_lista(self):
        # --- LÓGICA SIMULADA ---
        emprestimos_falsos = [("Duna", "ana@email.com", "01/10/2025"), ("O Nome do Vento", "joao@leitor.com", "15/10/2025")]
        for livro, usuario, data in emprestimos_falsos:
            self.listbox_emprestimos.insert(tk.END, f"LIVRO: {livro:<25} | USUÁRIO: {usuario:<20} | DEVOLUÇÃO: {data}")

    def funcao_placeholder(self):
        messagebox.showinfo("Em Breve", "Funcionalidade a ser implementada!")