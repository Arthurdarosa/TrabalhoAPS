import tkinter as tk
from tkinter import scrolledtext # Usaremos um widget de texto com rolagem

def centralizar_janela(janela):
    # (função de centralizar aqui)
    janela.update_idletasks()
    largura = janela.winfo_width()
    altura = janela.winfo_height()
    x = (janela.winfo_screenwidth() // 2) - (largura // 2)
    y = (janela.winfo_screenheight() // 2) - (altura // 2)
    janela.geometry(f'{largura}x{altura}+{x}+{y}')

class TelaRelatorios(tk.Toplevel):
    def __init__(self, parent):
        super().__init__(parent)
        self.title("Central de Relatórios")
        self.geometry("700x500")

        tk.Label(self, text="Gerador de Relatórios", font=('Helvetica', 16)).pack(pady=10)

        # Frame principal para dividir a tela em duas
        main_frame = tk.Frame(self)
        main_frame.pack(expand=True, fill='both', padx=10, pady=10)

        # --- Frame dos Botões (à esquerda) ---
        frame_botoes = tk.Frame(main_frame, width=200)
        frame_botoes.pack(side=tk.LEFT, fill='y', padx=(0, 10))

        tk.Button(frame_botoes, text="Avaliações de Livros", command=self.relatorio_avaliacoes).pack(fill='x', pady=2)
        tk.Button(frame_botoes, text="Melhores Médias", command=self.relatorio_melhores_medias).pack(fill='x', pady=2)
        tk.Button(frame_botoes, text="Piores Médias", command=self.relatorio_piores_medias).pack(fill='x', pady=2)
        tk.Button(frame_botoes, text="Empréstimos atrasados", command=self.relatorio_emprestimos_atrasados).pack(fill='x', pady=2)
        tk.Button(frame_botoes, text="Empréstimos ativos", command=self.relatorio_emprestimos_ativos).pack(fill='x', pady=2)
        
        tk.Button(frame_botoes, text="Fechar", command=self.destroy).pack(side=tk.BOTTOM, fill='x', pady=10)
        
        # --- Frame do Relatório (à direita) ---
        frame_texto = tk.Frame(main_frame)
        frame_texto.pack(side=tk.LEFT, expand=True, fill='both')
        
        self.texto_relatorio = scrolledtext.ScrolledText(frame_texto, wrap=tk.WORD, font=('Consolas', 10))
        self.texto_relatorio.pack(expand=True, fill='both')
        # Impede que o usuário edite o relatório
        self.texto_relatorio.config(state='disabled')

        centralizar_janela(self)
        self.transient(parent)
        self.grab_set()

    def limpar_relatorio(self):
        """Habilita, limpa e desabilita a caixa de texto."""
        self.texto_relatorio.config(state='normal')
        self.texto_relatorio.delete('1.0', tk.END)

    def finalizar_relatorio(self):
        """Desabilita a edição da caixa de texto."""
        self.texto_relatorio.config(state='disabled')

    # --- Métodos para gerar cada relatório ---
    def relatorio_avaliacoes(self):
        self.limpar_relatorio()
        self.texto_relatorio.insert(tk.END, "--- Relatório de Todas as Avaliações ---\n\n")
        # Lógica Simulada
        avaliacoes = [("Duna", 8, "Clássico!"), ("O Senhor dos Anéis", 9, "Perfeito."), ("Fundação", 9, "Muito bom, mas o final...")]
        for livro, nota, com in avaliacoes:
            self.texto_relatorio.insert(tk.END, f"Livro: {livro}\nNota: {nota}\nComentário: {com}\n\n")
        self.finalizar_relatorio()

    def relatorio_melhores_medias(self):
        self.limpar_relatorio()
        self.texto_relatorio.insert(tk.END, "--- Relatório: Livros com as Melhores Médias ---\n\n")
        # Lógica Simulada
        livros = [("O Senhor dos Anéis", 5.0), ("Duna", 4.8), ("O Nome do Vento", 4.7)]
        for livro, media in livros:
            self.texto_relatorio.insert(tk.END, f"Média: {media:.1f} - {livro}\n")
        self.finalizar_relatorio()
        
    def relatorio_piores_medias(self):
        # Observação: Assumi que "primeires medias" era um erro de digitação para "piores médias".
        self.limpar_relatorio()
        self.texto_relatorio.insert(tk.END, "--- Relatório: Livros com as Piores Médias ---\n\n")
        # Lógica Simulada
        livros = [("Crepúsculo", 2.1), ("Cinquenta Tons de Cinza", 1.5), ("After", 1.2)]
        for livro, media in livros:
            self.texto_relatorio.insert(tk.END, f"Média: {media:.1f} - {livro}\n")
        self.finalizar_relatorio()

    def relatorio_emprestimos_atrasados(self):
        self.limpar_relatorio()
        self.texto_relatorio.insert(tk.END, "--- Relatório de Empréstimos Atrasados) ---\n\n")
        # Lógica Simulada
        atrasados = [("Duna", "ana@email.com", "35"), ("Fundação", "joao@leitor.com", "2"), ("harry poter", "joao@leitor.com", "13")]
        for livro, usuario, atraso in atrasados:
            self.texto_relatorio.insert(tk.END, f"Livro: {livro}\nUsuário: {usuario}\ndias de atraso: {atraso}\n\n")
        self.finalizar_relatorio()

    def relatorio_emprestimos_ativos(self):
        self.limpar_relatorio()
        self.texto_relatorio.insert(tk.END, "--- Relatório de Empréstimos ativos ---\n\n")
        # Lógica Simulada
        ativos = [("O Guia do Mochileiro", "ana@email.com", "15/09/2025"), ("Neuromancer", "carlos@admin.com", "12/09/2025")]
        for livro, usuario, data in ativos:
            self.texto_relatorio.insert(tk.END, f"Livro: {livro}\nUsuário: {usuario}\nData Devolução: {data}\n\n")
        self.finalizar_relatorio()