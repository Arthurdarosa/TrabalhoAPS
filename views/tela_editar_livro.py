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

        tk.Label(frame_form, text="Quantidade:").grid(row=3, column=0, sticky='w', pady=5)
        # --- CORREÇÃO AQUI: A variável estava errada (era self.entry_genero) ---
        self.entry_qtd = tk.Entry(frame_form, width=10)
        self.entry_qtd.grid(row=3, column=1, sticky='w')

        # --- ADICIONADO: Preenchendo o formulário com os dados existentes ---
        self.entry_titulo.insert(0, dados_livro.get('titulo', ''))
        self.entry_autor.insert(0, dados_livro.get('autor', ''))
        self.entry_genero.insert(0, dados_livro.get('genero', ''))
        self.entry_qtd.insert(0, str(dados_livro.get('quantidade', '')))

        # --- ADICIONADO: Botões de ação ---
        frame_botoes = tk.Frame(self)
        frame_botoes.pack(pady=10)
        tk.Button(frame_botoes, text="Salvar Alterações", command=self.salvar).pack(side=tk.LEFT, padx=10)
        tk.Button(frame_botoes, text="Cancelar", command=self.destroy).pack(side=tk.LEFT, padx=10)
        
        # --- ADICIONADO: Finalização da janela (centralizar e tornar modal) ---
        centralizar_janela(self)
        self.transient(parent)
        self.grab_set()

    def salvar(self):
        """
        Pega os dados dos campos, mostra uma mensagem de sucesso e fecha a janela.
        """
        # --- LÓGICA SIMULADA ---
        try:
            novos_dados = {
                'titulo': self.entry_titulo.get(),
                'autor': self.entry_autor.get(),
                'genero': self.entry_genero.get(),
                'quantidade': int(self.entry_qtd.get()) # Converte para inteiro
            }
            self.dados_atualizados = novos_dados # Guarda os dados para a tela anterior ler

            print(f"Salvando alterações para o livro: {novos_dados['titulo']}")
            messagebox.showinfo("Sucesso", "Alterações salvas com sucesso!")
            
            self.destroy() # Fecha a janela
        except ValueError:
            messagebox.showerror("Erro", "A quantidade deve ser um número inteiro.")