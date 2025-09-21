import tkinter as tk
from tkinter import messagebox
from views.tela_editar_usuario import TelaEditarUsuario # Reutilizando a mesma tela de edição!

def centralizar_janela(janela):
    # (função de centralizar aqui)
    janela.update_idletasks()
    # ...
    largura = janela.winfo_width()
    altura = janela.winfo_height()
    x = (janela.winfo_screenwidth() // 2) - (largura // 2)
    y = (janela.winfo_screenheight() // 2) - (altura // 2)
    janela.geometry(f'{largura}x{altura}+{x}+{y}')

class TelaGerenciarAdmins(tk.Toplevel):
    def __init__(self, parent):
        super().__init__(parent)
        self.title("Gerenciar Administradores")
        self.geometry("500x400")
        
        # Dados Falsos
        self.usuarios_falsos = [
            {'nome': 'Ana Silva', 'email': 'ana@email.com', 'CPF':'11122233344', 'senha':'123', 'telefone':'99998888'},
            {'nome': 'Carlos Souza', 'email': 'carlos@admin.com', 'CPF':'11122233344', 'senha':'123', 'telefone':'99998888'},
            {'nome': 'João Pereira', 'email': 'joao@leitor.com','CPF':'11122233344', 'senha':'123', 'telefone':'99998888'}
        ]
        self.admins = [u for u in self.usuarios_falsos if u['CPF'] == '11122233344']

        tk.Label(self, text="Lista de Administradores", font=('Helvetica', 16)).pack(pady=10)

        # Copie e cole os frames e widgets da TelaGerenciarLeitores aqui
        # A estrutura é idêntica, apenas mudando as variáveis para 'admins'
        frame_lista = tk.Frame(self)
        frame_lista.pack(pady=10, padx=10, expand=True, fill='both')
        self.listbox_admins = tk.Listbox(frame_lista, font=('Consolas', 10))
        self.listbox_admins.pack(side=tk.LEFT, expand=True, fill='both')
        scrollbar = tk.Scrollbar(frame_lista, orient='vertical', command=self.listbox_admins.yview)
        scrollbar.pack(side=tk.RIGHT, fill='y')
        self.listbox_admins.config(yscrollcommand=scrollbar.set)
        
        frame_botoes = tk.Frame(self)
        frame_botoes.pack(pady=10)
        tk.Button(frame_botoes, text="Editar Selecionado", command=self.editar_admin).pack(side=tk.LEFT, padx=5)
        tk.Button(frame_botoes, text="Excluir Selecionado", command=self.excluir_admin).pack(side=tk.LEFT, padx=5)
        tk.Button(self, text="Voltar", command=self.destroy).pack(pady=5)

        self.popular_lista()
        centralizar_janela(self)
        self.transient(parent)
        self.grab_set()

    def popular_lista(self):
        self.listbox_admins.delete(0, tk.END)
        for admin in self.admins:
            self.listbox_admins.insert(tk.END, f"{admin['nome']:<25} | {admin['email']}")
    
    def editar_admin(self):
        # A lógica é idêntica à de editar leitor
        indices = self.listbox_admins.curselection()
        if not indices: return
        index = indices[0]
        tela_edicao = TelaEditarUsuario(self, self.admins[index])
        self.wait_window(tela_edicao)
        if tela_edicao.dados_atualizados:
            # Atualiza o tipo para não virar leitor
            tela_edicao.dados_atualizados['tipo'] = 'Administrador'
            self.admins[index] = tela_edicao.dados_atualizados
            self.popular_lista()

    def excluir_admin(self):
        # A lógica é idêntica à de excluir leitor
        indices = self.listbox_admins.curselection()
        if not indices: return
        index = indices[0]
        if messagebox.askyesno("Confirmar", "Tem certeza?"):
            del self.admins[index]
            self.popular_lista()