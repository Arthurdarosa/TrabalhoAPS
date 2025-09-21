import tkinter as tk
from tkinter import messagebox
from views.tela_editar_usuario import TelaEditarUsuario

def centralizar_janela(janela):
    # (função de centralizar aqui)
    janela.update_idletasks()
    largura = janela.winfo_width()
    altura = janela.winfo_height()
    x = (janela.winfo_screenwidth() // 2) - (largura // 2)
    y = (janela.winfo_screenheight() // 2) - (altura // 2)
    janela.geometry(f'{largura}x{altura}+{x}+{y}')

class TelaGerenciarLeitores(tk.Toplevel):
    def __init__(self, parent):
        super().__init__(parent)
        self.title("Gerenciar Leitores")
        self.geometry("500x400")
        
        # Dados Falsos
        self.usuarios_falsos = [
            {'nome': 'Ana Silva', 'email': 'ana@email.com', 'CPF':'11122233344', 'senha':'123', 'telefone':'99998888'},
            {'nome': 'Carlos Souza', 'email': 'carlos@admin.com', 'CPF':'11122233344', 'senha':'123', 'telefone':'99998888'},
            {'nome': 'João Pereira', 'email': 'joao@leitor.com','CPF':'11122233344', 'senha':'123', 'telefone':'99998888'}
        ]
        
        self.leitores = [u for u in self.usuarios_falsos if u['CPF'] == '11122233344']

        tk.Label(self, text="Lista de Leitores Cadastrados", font=('Helvetica', 16)).pack(pady=10)

        frame_lista = tk.Frame(self)
        frame_lista.pack(pady=10, padx=10, expand=True, fill='both')
        self.listbox_leitores = tk.Listbox(frame_lista, font=('Consolas', 10))
        self.listbox_leitores.pack(side=tk.LEFT, expand=True, fill='both')
        scrollbar = tk.Scrollbar(frame_lista, orient='vertical', command=self.listbox_leitores.yview)
        scrollbar.pack(side=tk.RIGHT, fill='y')
        self.listbox_leitores.config(yscrollcommand=scrollbar.set)
        
        frame_botoes = tk.Frame(self)
        frame_botoes.pack(pady=10)
        tk.Button(frame_botoes, text="Editar Selecionado", command=self.editar_leitor).pack(side=tk.LEFT, padx=5)
        tk.Button(frame_botoes, text="Excluir Selecionado", command=self.excluir_leitor).pack(side=tk.LEFT, padx=5)
        tk.Button(self, text="Voltar", command=self.destroy).pack(pady=5)

        self.popular_lista()
        centralizar_janela(self)
        self.transient(parent)
        self.grab_set()

    def popular_lista(self):
        self.listbox_leitores.delete(0, tk.END)
        for leitor in self.leitores:
            self.listbox_leitores.insert(tk.END, f"{leitor['nome']:<25} | {leitor['email']}")

    def editar_leitor(self):
        indices = self.listbox_leitores.curselection()
        if not indices:
            messagebox.showwarning("Aviso", "Selecione um leitor para editar.")
            return
        
        index = indices[0]
        dados_leitor = self.leitores[index]
        
        tela_edicao = TelaEditarUsuario(self, dados_leitor)
        self.wait_window(tela_edicao)

        if tela_edicao.dados_atualizados:
            self.leitores[index] = tela_edicao.dados_atualizados
            self.popular_lista()

    def excluir_leitor(self):
        indices = self.listbox_leitores.curselection()
        if not indices:
            messagebox.showwarning("Aviso", "Selecione um leitor para excluir.")
            return

        index = indices[0]
        leitor = self.leitores[index]
        
        if messagebox.askyesno("Confirmar", f"Tem certeza que deseja excluir o leitor {leitor['nome']}?"):
            print(f"Excluindo leitor: {leitor['email']}")
            del self.leitores[index]
            self.popular_lista()