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

class TelaEfetuarPedido(tk.Toplevel):
    def __init__(self, parent, dados_livro: dict):
        super().__init__(parent)
        self.title("Confirmar Pedido")
        self.geometry("450x250")
        self.resizable(False, False)

        self.pedido_efetuado = False

        # --- Widgets para mostrar detalhes do livro ---
        tk.Label(self, text="Confirmar Pedido do Livro", font=('Helvetica', 16)).pack(pady=10)
        frame_detalhes = tk.Frame(self, padx=10, pady=10)
        frame_detalhes.pack(expand=True, fill='both')

        tk.Label(frame_detalhes, text="Título:", font=('Helvetica', 10, 'bold')).grid(row=0, column=0, sticky='w')
        tk.Label(frame_detalhes, text=dados_livro['titulo'], font=('Helvetica', 10)).grid(row=0, column=1, sticky='w')
        tk.Label(frame_detalhes, text="Autor:", font=('Helvetica', 10, 'bold')).grid(row=1, column=0, sticky='w')
        tk.Label(frame_detalhes, text=dados_livro['autor'], font=('Helvetica', 10)).grid(row=1, column=1, sticky='w')

        # ===================================================================
        # ## MUDANÇA PRINCIPAL AQUI ##
        # Lógica de Situação (Substituindo a antiga "Lógica de Disponibilidade")
        # ===================================================================
        if dados_livro['quantidade'] > 0:
            situacao_texto = "Pronto para Retirada"
            situacao_cor = "green"
            texto_botao_confirmar = "Efetuar Empréstimo"
        else:
            # Simula o tamanho da fila. Em um sistema real, você buscaria isso no banco.
            tamanho_fila = dados_livro.get('fila_espera', 0) 
            posicao_usuario = tamanho_fila + 1
            situacao_texto = f"{posicao_usuario}º na fila de espera"
            situacao_cor = "orange"
            texto_botao_confirmar = "Entrar na Fila"
        
        tk.Label(frame_detalhes, text="Situação:", font=('Helvetica', 10, 'bold')).grid(row=2, column=0, sticky='w', pady=(10,0))
        tk.Label(frame_detalhes, text=situacao_texto, font=('Helvetica', 10), fg=situacao_cor).grid(row=2, column=1, sticky='w', pady=(10,0))
        # ===================================================================
        
        # Botões de ação
        frame_botoes = tk.Frame(self)
        frame_botoes.pack(pady=20)
        tk.Button(frame_botoes, text=texto_botao_confirmar, command=self.confirmar).pack(side=tk.LEFT, padx=10)
        tk.Button(frame_botoes, text="Cancelar", command=self.destroy).pack(side=tk.LEFT, padx=10)
        
        centralizar_janela(self)
        self.transient(parent)
        self.grab_set()

    def confirmar(self):
        self.pedido_efetuado = True
        messagebox.showinfo("Sucesso", "Operação realizada com sucesso!")
        self.destroy()