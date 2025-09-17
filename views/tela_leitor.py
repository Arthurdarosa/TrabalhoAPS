# --- telas/tela_leitor.py ---
import tkinter as tk
from views.tela_buscar_livro import TelaBuscarLivro
from views.tela_emprestimos import TelaEmprestimos

# É uma boa prática incluir a função de centralizar em todas as telas
def centralizar_janela(janela):
    janela.update_idletasks()
    largura = janela.winfo_width()
    altura = janela.winfo_height()
    x = (janela.winfo_screenwidth() // 2) - (largura // 2)
    y = (janela.winfo_screenheight() // 2) - (altura // 2)
    janela.geometry(f'{largura}x{altura}+{x}+{y}')

class TelaLeitor(tk.Tk):
    def __init__(self, nome_leitor: str):
        super().__init__()
        self.title("Painel do Leitor")
        self.geometry("400x300")
        
        tk.Label(self, text=f"Bem-vindo(a), {nome_leitor}!", font=('Helvetica', 18)).pack(pady=20)
        
        tk.Button(self, text="Buscar Livros", width=20, height=2, command=self.abrir_tela_busca).pack(pady=5)
        tk.Button(self, text="Meus Empréstimos", width=20, height=2, command=self.abrir_tela_emprestimos).pack(pady=5)
        
        tk.Button(self, text="Logout", command=self.destroy).pack(side=tk.BOTTOM, pady=20)
        centralizar_janela(self)
    
    def abrir_tela_busca(self):
        print("clicou")
        # Este método cria e exibe a janela de busca de livros
        tela_busca = TelaBuscarLivro(self)
        # O 'grab_set()' na classe TelaBuscarLivro fará com que esta janela espere.
        print("clicou")
        tela_busca.mainloop()

    def abrir_tela_emprestimos(self):
        # Este método cria e exibe a janela de empréstimos
        tela_emprestimos = TelaEmprestimos(self)