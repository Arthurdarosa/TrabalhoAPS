import tkinter as tk
from tkinter import messagebox
from views.tela_editar_usuario import TelaEditarUsuario
from controllers.leitor_controller import LeitorController

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
        self.controller = LeitorController()
        
        # Lista interna representando a visão (dicts) derivada do controller
        self.leitores = []

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

        self.recarregar()
        centralizar_janela(self)
        self.transient(parent)
        self.grab_set()

    def popular_lista(self):
        self.listbox_leitores.delete(0, tk.END)
        for leitor in self.leitores:
            self.listbox_leitores.insert(tk.END, f"{leitor['nome']:<25} | {leitor['email']}")

    def recarregar(self):
        # Converte objetos em dicts simples para exibição/edição
        self.leitores = [
            {
                'nome': l.nome,
                'email': l.email,
                'telefone': str(l.telefone),
            }
            for l in self.controller.listar_leitores()
        ]
        self.popular_lista()

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
            novos = tela_edicao.dados_atualizados
            sucesso, mensagem = self.controller.atualizar_leitor(
                email_original=dados_leitor['email'],
                nome=novos.get('nome'),
                email=novos.get('email'),
                telefone=novos.get('telefone'),
                senha=novos.get('senha'),
            )
            if sucesso:
                messagebox.showinfo("Sucesso", mensagem)
                self.recarregar()
            else:
                messagebox.showerror("Erro", mensagem)

    def excluir_leitor(self):
        indices = self.listbox_leitores.curselection()
        if not indices:
            messagebox.showwarning("Aviso", "Selecione um leitor para excluir.")
            return

        index = indices[0]
        leitor = self.leitores[index]
        
        if messagebox.askyesno("Confirmar", f"Tem certeza que deseja excluir o leitor {leitor['nome']}?"):
            sucesso, mensagem = self.controller.excluir_leitor_por_email(leitor['email'])
            if sucesso:
                messagebox.showinfo("Sucesso", mensagem)
                self.recarregar()
            else:
                messagebox.showerror("Erro", mensagem)