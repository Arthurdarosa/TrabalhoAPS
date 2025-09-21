import tkinter as tk
from views.tela_buscar_livro import TelaBuscarLivro
from views.tela_emprestimos import TelaEmprestimos
from views.tela_acompanhar_filas import TelaAcompanharFilas
from views.tela_efetuar_pedido import TelaEfetuarPedido

def centralizar_janela(janela):
    # (função de centralizar aqui)
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
        self.geometry("400x400") # Aumentei a altura para mais um botão
        
        tk.Label(self, text=f"Bem-vindo(a), {nome_leitor}!", font=('Helvetica', 18)).pack(pady=20)
        
        tk.Button(self, text="Buscar Livros", width=20, height=2, command=self.abrir_tela_busca).pack(pady=5)
        tk.Button(self, text="Meus Empréstimos", width=20, height=2, command=self.abrir_tela_emprestimos).pack(pady=5)
        tk.Button(self, text="Acompanhar Filas", width=20, height=2, command=self.abrir_tela_filas).pack(pady=5)
        

        tk.Button(self, text="Logout", command=self.destroy).pack(side=tk.BOTTOM, pady=20)
        centralizar_janela(self)

    def abrir_tela_busca(self):
        tela_busca = TelaBuscarLivro(self)
        self.wait_window(tela_busca)

    def abrir_tela_emprestimos(self):
        tela_emprestimos = TelaEmprestimos(self)
        self.wait_window(tela_emprestimos)

    def abrir_tela_filas(self):
        tela_filas = TelaAcompanharFilas(self)
        self.wait_window(tela_filas)

    # --- NOVO MÉTODO PARA O ATALHO ---
    def abrir_tela_pedido_direto(self):
        """
        Abre a tela de efetuar pedido diretamente com um livro de exemplo.
        """
        # Criamos dados falsos de um livro para enviar para a tela de pedido
        livro_exemplo = {
            'titulo': 'Neuromancer (Livro de Teste)',
            'autor': 'William Gibson',
            'quantidade': 0 # Mude para > 0 para ver o botão "Confirmar Empréstimo"
        }
        
        print("DEBUG: Abrindo a tela de pedido diretamente com dados de exemplo.")
        tela_pedido = TelaEfetuarPedido(self, livro_exemplo)
        self.wait_window(tela_pedido)
        print("DEBUG: Tela de pedido fechada.")