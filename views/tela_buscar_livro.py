import tkinter as tk
from tkinter import messagebox
# Importando a nova tela de pedido
from views.tela_efetuar_pedido import TelaEfetuarPedido

def centralizar_janela(janela):
    # (função de centralizar aqui)
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

        # Dados falsos para simulação (incluindo quantidade)
        self.livros_encontrados = [
            {'titulo': 'Duna', 'autor': 'Frank Herbert', 'genero': 'Ficção Científica', 'quantidade': 5},
            {'titulo': 'O Guia do Mochileiro das Galáxias', 'autor': 'Douglas Adams', 'genero': 'Ficção Científica', 'quantidade': 0},
            {'titulo': 'O Senhor dos Anéis', 'autor': 'J.R.R. Tolkien', 'genero': 'Fantasia', 'quantidade': 3},
        ]
        
        # --- Widgets ---
        frame_busca = tk.Frame(self)
        frame_busca.pack(pady=10, padx=10, fill='x')
        tk.Label(frame_busca, text="Nome do Livro:").pack(side=tk.LEFT, padx=(0, 5))
        self.entry_busca = tk.Entry(frame_busca)
        self.entry_busca.pack(side=tk.LEFT, expand=True, fill='x', padx=5)
        tk.Button(frame_busca, text="Buscar", command=self.buscar_livros).pack(side=tk.LEFT)
        
        frame_resultados = tk.Frame(self)
        frame_resultados.pack(pady=10, padx=10, expand=True, fill='both')
        self.listbox_resultados = tk.Listbox(frame_resultados)
        self.listbox_resultados.pack(side=tk.LEFT, expand=True, fill='both')
        scrollbar = tk.Scrollbar(frame_resultados, orient='vertical', command=self.listbox_resultados.yview)
        scrollbar.pack(side=tk.RIGHT, fill='y')
        self.listbox_resultados.config(yscrollcommand=scrollbar.set)

        # --- MUDANÇA: Novo botão "Efetuar Pedido", que começa desabilitado ---
        frame_botoes = tk.Frame(self)
        frame_botoes.pack(pady=10)
        self.botao_pedido = tk.Button(frame_botoes, text="Efetuar Pedido", state="disabled", command=self.abrir_tela_pedido)
        self.botao_pedido.pack(side=tk.LEFT, padx=10)
        tk.Button(frame_botoes, text="Voltar", command=self.destroy).pack(side=tk.LEFT, padx=10)

        # --- MUDANÇA: Associar um evento à seleção de item na lista ---
        self.listbox_resultados.bind('<<ListboxSelect>>', self.on_livro_selecionado)
        
        centralizar_janela(self)
        self.transient(parent)
        self.grab_set()

    def on_livro_selecionado(self, event):
        """
        Esta função é chamada sempre que um item da lista é selecionado.
        Ela ativa ou desativa o botão de pedido.
        """
        # Se houver itens selecionados na lista
        if self.listbox_resultados.curselection():
            self.botao_pedido.config(state="normal") # Ativa o botão
        else:
            self.botao_pedido.config(state="disabled") # Desativa o botão

    def buscar_livros(self):
        # ... (lógica de busca simulada continua a mesma) ...
        self.listbox_resultados.delete(0, tk.END)
        self.botao_pedido.config(state="disabled") # Desativa o botão ao buscar de novo
        termo_busca = self.entry_busca.get()
        for livro in self.livros_encontrados:
            if termo_busca.lower() in livro['titulo'].lower():
                self.listbox_resultados.insert(tk.END, livro['titulo'])
    
    def abrir_tela_pedido(self):
        """
        Abre a tela de confirmação do pedido para o livro selecionado.
        """
        indices_selecionados = self.listbox_resultados.curselection()
        if not indices_selecionados:
            return

        index = indices_selecionados[0]
        # Encontra o dicionário completo do livro selecionado
        titulo_selecionado = self.listbox_resultados.get(index)
        dados_livro = next((livro for livro in self.livros_encontrados if livro['titulo'] == titulo_selecionado), None)

        if dados_livro:
            tela_pedido = TelaEfetuarPedido(self, dados_livro)
            self.wait_window(tela_pedido)
            
            # Se o pedido foi efetuado com sucesso, fecha também a tela de busca
            if hasattr(tela_pedido, 'pedido_efetuado') and tela_pedido.pedido_efetuado:
                self.destroy()