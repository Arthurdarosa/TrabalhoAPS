import tkinter as tk
from tkinter import messagebox
# Importa a futura tela de edição para podermos abri-la
from views.tela_editar_livro import TelaEditarLivro

def centralizar_janela(janela):
    # (código da função de centralizar aqui)
    janela.update_idletasks()
    largura = janela.winfo_width()
    altura = janela.winfo_height()
    x = (janela.winfo_screenwidth() // 2) - (largura // 2)
    y = (janela.winfo_screenheight() // 2) - (altura // 2)
    janela.geometry(f'{largura}x{altura}+{x}+{y}')

class TelaGerenciarLivros(tk.Toplevel):
    def __init__(self, parent):
        super().__init__(parent)
        self.title("Gerenciar Acervo de Livros")
        self.geometry("600x450")

        # Dados falsos para simulação
        self.livros_cadastrados = [
            {'titulo': 'Duna', 'autor': 'Frank Herbert', 'genero': 'Ficção Científica', 'quantidade': 5},
            {'titulo': 'O Senhor dos Anéis', 'autor': 'J.R.R. Tolkien', 'genero': 'Fantasia', 'quantidade': 3},
            {'titulo': 'Fundação', 'autor': 'Isaac Asimov', 'genero': 'Ficção Científica', 'quantidade': 7},
        ]

        # --- Widgets ---
        tk.Label(self, text="Consultar e Editar Livros", font=('Helvetica', 16)).pack(pady=10)

        # Frame da lista
        frame_lista = tk.Frame(self)
        frame_lista.pack(pady=10, padx=10, expand=True, fill='both')
        self.listbox_livros = tk.Listbox(frame_lista, font=('Consolas', 10))
        self.listbox_livros.pack(side=tk.LEFT, expand=True, fill='both')
        scrollbar = tk.Scrollbar(frame_lista, orient='vertical', command=self.listbox_livros.yview)
        scrollbar.pack(side=tk.RIGHT, fill='y')
        self.listbox_livros.config(yscrollcommand=scrollbar.set)
        
        # Frame de botões
        frame_botoes = tk.Frame(self)
        frame_botoes.pack(pady=10)
        tk.Button(frame_botoes, text="Editar Livro Selecionado", command=self.abrir_tela_edicao).pack(side=tk.LEFT, padx=5)
        # Futuramente, você poderia adicionar um botão de excluir
        # tk.Button(frame_botoes, text="Excluir Selecionado", command=self.excluir_livro).pack(side=tk.LEFT, padx=5)
        tk.Button(self, text="Voltar", command=self.destroy).pack(pady=5)

        self.popular_lista()
        centralizar_janela(self)
        self.transient(parent)
        self.grab_set()

    def popular_lista(self):
        self.listbox_livros.delete(0, tk.END) # Limpa a lista
        # --- LÓGICA SIMULADA ---
        for livro in self.livros_cadastrados:
            texto = f"TÍTULO: {livro['titulo']:<30} | AUTOR: {livro['autor']:<20} | QTD: {livro['quantidade']}"
            self.listbox_livros.insert(tk.END, texto)

    def abrir_tela_edicao(self):
        # Pega o índice do item selecionado na lista
        indices_selecionados = self.listbox_livros.curselection()
        if not indices_selecionados:
            messagebox.showwarning("Aviso", "Por favor, selecione um livro da lista para editar.")
            return

        index = indices_selecionados[0]
        # Pega os dados do livro selecionado da nossa lista de dicionários
        livro_selecionado = self.livros_cadastrados[index]

        # Abre a tela de edição, passando os dados do livro para ela
        tela_edicao = TelaEditarLivro(self, livro_selecionado)
        self.wait_window(tela_edicao)

        # --- LÓGICA SIMULADA ---
        # Após a janela de edição fechar, atualiza a lista para refletir as mudanças
        # Em um app real, você buscaria os dados atualizados do banco.
        if hasattr(tela_edicao, 'dados_atualizados') and tela_edicao.dados_atualizados:
            self.livros_cadastrados[index] = tela_edicao.dados_atualizados
            self.popular_lista()
            # Seleciona novamente o item que foi editado
            self.listbox_livros.selection_set(index)