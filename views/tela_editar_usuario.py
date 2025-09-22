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

class TelaEditarUsuario(tk.Toplevel):
    def __init__(self, parent, dados_usuario: dict):
        super().__init__(parent)
        self.title(f"Editando Usuário: {dados_usuario['email']}")
        self.geometry("450x260")
        
        self.dados_atualizados = None

        # Formulário para editar os dados
        frame_form = tk.Frame(self)
        frame_form.pack(pady=20, padx=20)

        tk.Label(frame_form, text="Nome:").grid(row=0, column=0, sticky='w', pady=5)
        self.entry_nome = tk.Entry(frame_form, width=40)
        self.entry_nome.grid(row=0, column=1)

        tk.Label(frame_form, text="Email:").grid(row=1, column=0, sticky='w', pady=5)
        self.entry_email = tk.Entry(frame_form, width=40)
        self.entry_email.grid(row=1, column=1)

        tk.Label(frame_form, text="Senha (opcional):").grid(row=2, column=0, sticky='w', pady=5)
        self.entry_senha = tk.Entry(frame_form, width=40, show='*')
        self.entry_senha.grid(row=2, column=1)

        tk.Label(frame_form, text="Telefone:").grid(row=3, column=0, sticky='w', pady=5)
        self.entry_telefone = tk.Entry(frame_form, width=40)
        self.entry_telefone.grid(row=3, column=1)

        # Preenchendo com os dados atuais
        self.entry_nome.insert(0, dados_usuario['nome'])
        self.entry_email.insert(0, dados_usuario['email'])
        # Não preencher senha. Deixar vazio para manter a atual
        self.entry_telefone.insert(0, dados_usuario.get('telefone', ''))
        # Botões
        frame_botoes = tk.Frame(self)
        frame_botoes.pack(pady=10)
        tk.Button(frame_botoes, text="Salvar Alterações", command=self.salvar).pack(side=tk.LEFT, padx=10)
        tk.Button(frame_botoes, text="Cancelar", command=self.destroy).pack(side=tk.LEFT, padx=10)

        centralizar_janela(self)
        self.transient(parent)
        self.grab_set()
        
    def salvar(self):
        nome = self.entry_nome.get().strip()
        email = self.entry_email.get().strip()
        senha = self.entry_senha.get()
        telefone = self.entry_telefone.get().strip()

        if not nome:
            messagebox.showerror("Erro", "Nome é obrigatório!")
            return
        if not email:
            messagebox.showerror("Erro", "Email é obrigatório!")
            return

        self.dados_atualizados = {
            'nome': nome,
            'email': email,
            'telefone': telefone,
            'senha': senha,  # pode ser vazio para manter
        }
        messagebox.showinfo("Sucesso", "Usuário atualizado com sucesso!")
        self.destroy()