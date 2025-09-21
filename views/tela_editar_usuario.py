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
        self.geometry("400x200")
        
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

        tk.Label(frame_form, text="senha:").grid(row=2, column=0, sticky='w', pady=5)
        self.entry_senha = tk.Entry(frame_form, width=40)
        self.entry_senha.grid(row=2, column=1)

        tk.Label(frame_form, text="telefone:").grid(row=3, column=0, sticky='w', pady=5)
        self.entry_telefone = tk.Entry(frame_form, width=40)
        self.entry_telefone.grid(row=3, column=1)

        # Preenchendo com os dados atuais
        self.entry_nome.insert(0, dados_usuario['nome'])
        self.entry_email.insert(0, dados_usuario['email'])
        self.entry_senha.insert(0, dados_usuario['senha'])
        self.entry_telefone.insert(0, dados_usuario['telefone'])
        # Botões
        frame_botoes = tk.Frame(self)
        frame_botoes.pack(pady=10)
        tk.Button(frame_botoes, text="Salvar Alterações", command=self.salvar).pack(side=tk.LEFT, padx=10)
        tk.Button(frame_botoes, text="Cancelar", command=self.destroy).pack(side=tk.LEFT, padx=10)

        centralizar_janela(self)
        self.transient(parent)
        self.grab_set()
        
    def salvar(self):
        # --- LÓGICA SIMULADA ---
        novos_dados = {
            'nome': self.entry_nome.get(),
            'email': self.entry_email.get(),
            'tipo': 'Leitor' # Em um sistema real, você não mudaria o tipo aqui
        }
        self.dados_atualizados = novos_dados
        messagebox.showinfo("Sucesso", "Usuário atualizado com sucesso!")
        self.destroy()