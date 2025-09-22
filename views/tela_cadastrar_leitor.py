import tkinter as tk
from tkinter import messagebox, ttk
from controllers.leitor_controller import LeitorController

def centralizar_janela(janela):
    """Centraliza a janela na tela."""
    janela.update_idletasks()
    largura = janela.winfo_width()
    altura = janela.winfo_height()
    x = (janela.winfo_screenwidth() // 2) - (largura // 2)
    y = (janela.winfo_screenheight() // 2) - (altura // 2)
    janela.geometry(f'{largura}x{altura}+{x}+{y}')

class TelaCadastrarLeitor(tk.Toplevel):
    """Tela para cadastro de novos leitores."""
    
    def __init__(self, parent):
        super().__init__(parent)
        self.parent = parent
        self.controller = LeitorController()
        self.leitor_temporario = None  # Armazena dados temporariamente
        
        self.title("Cadastrar Leitor")
        self.geometry("500x700")
        self.resizable(False, False)
        
        # Configurar para fechar apenas esta janela
        self.protocol("WM_DELETE_WINDOW", self.fechar)
        
        self.criar_interface()
        centralizar_janela(self)
    
    def criar_interface(self):
        """Cria a interface da tela."""
        # Título
        titulo = tk.Label(self, text="Cadastrar Novo Leitor", 
                         font=('Helvetica', 16, 'bold'))
        titulo.pack(pady=20)
        
        # Frame principal
        frame_principal = tk.Frame(self)
        frame_principal.pack(pady=10, padx=20, fill='both', expand=True)
        
        # Nome
        tk.Label(frame_principal, text="Nome Completo:", 
                font=('Helvetica', 10, 'bold')).pack(anchor='w', pady=(10, 5))
        self.entry_nome = tk.Entry(frame_principal, width=40, font=('Helvetica', 10))
        self.entry_nome.pack(anchor='w', pady=(0, 10))
        
        # Email
        tk.Label(frame_principal, text="Email:", 
                font=('Helvetica', 10, 'bold')).pack(anchor='w', pady=(10, 5))
        self.entry_email = tk.Entry(frame_principal, width=40, font=('Helvetica', 10))
        self.entry_email.pack(anchor='w', pady=(0, 10))
        
        # CPF
        tk.Label(frame_principal, text="CPF:", 
                font=('Helvetica', 10, 'bold')).pack(anchor='w', pady=(10, 5))
        self.entry_cpf = tk.Entry(frame_principal, width=40, font=('Helvetica', 10))
        self.entry_cpf.pack(anchor='w', pady=(0, 5))
        tk.Label(frame_principal, text="(Digite apenas números ou com formatação: 000.000.000-00)", 
                font=('Helvetica', 8), fg='gray').pack(anchor='w', pady=(0, 10))
        
        # Telefone
        tk.Label(frame_principal, text="Telefone:", 
                font=('Helvetica', 10, 'bold')).pack(anchor='w', pady=(10, 5))
        self.entry_telefone = tk.Entry(frame_principal, width=40, font=('Helvetica', 10))
        self.entry_telefone.pack(anchor='w', pady=(0, 5))
        tk.Label(frame_principal, text="(Digite apenas números ou com formatação: (00) 00000-0000)", 
                font=('Helvetica', 8), fg='gray').pack(anchor='w', pady=(0, 10))
        
        # Senha
        tk.Label(frame_principal, text="Senha:", 
                font=('Helvetica', 10, 'bold')).pack(anchor='w', pady=(10, 5))
        self.entry_senha = tk.Entry(frame_principal, width=40, show="*", font=('Helvetica', 10))
        self.entry_senha.pack(anchor='w', pady=(0, 5))
        tk.Label(frame_principal, text="(Mínimo 6 caracteres)", 
                font=('Helvetica', 8), fg='gray').pack(anchor='w', pady=(0, 10))
        
        # Confirmar Senha
        tk.Label(frame_principal, text="Confirmar Senha:", 
                font=('Helvetica', 10, 'bold')).pack(anchor='w', pady=(10, 5))
        self.entry_confirmar_senha = tk.Entry(frame_principal, width=40, show="*", font=('Helvetica', 10))
        self.entry_confirmar_senha.pack(anchor='w', pady=(0, 20))
        
        # Botões diretamente na janela principal
        # Botão Confirmar
        btn_confirmar = tk.Button(self, text="Confirmar", 
                                 command=self.confirmar_dados, width=15, height=2,
                                 bg='#4CAF50', fg='white', font=('Helvetica', 10, 'bold'))
        btn_confirmar.pack(side=tk.LEFT, padx=10, pady=20)
        
        # Botão Limpar
        btn_limpar = tk.Button(self, text="Limpar", 
                              command=self.limpar_campos, width=15, height=2,
                              bg='#FF9800', fg='white', font=('Helvetica', 10, 'bold'))
        btn_limpar.pack(side=tk.LEFT, padx=10, pady=20)
        
        # Botão Voltar
        btn_voltar = tk.Button(self, text="Voltar", 
                              command=self.fechar, width=15, height=2,
                              bg='#f44336', fg='white', font=('Helvetica', 10, 'bold'))
        btn_voltar.pack(side=tk.LEFT, padx=10, pady=20)
        
        print("Botões criados: Confirmar, Limpar, Voltar")  # Debug
        
        # Configurar foco inicial
        self.entry_nome.focus()
    
    def confirmar_dados(self):
        """Valida e armazena temporariamente os dados do leitor."""
        # Coleta dados dos campos
        nome = self.entry_nome.get().strip()
        email = self.entry_email.get().strip()
        cpf = self.entry_cpf.get().strip()
        telefone = self.entry_telefone.get().strip()
        senha = self.entry_senha.get()
        confirmar_senha = self.entry_confirmar_senha.get()
        
        # Validações básicas
        if not nome:
            messagebox.showerror("Erro", "Nome é obrigatório!")
            self.entry_nome.focus()
            return
        
        if not email:
            messagebox.showerror("Erro", "Email é obrigatório!")
            self.entry_email.focus()
            return
        
        if not cpf:
            messagebox.showerror("Erro", "CPF é obrigatório!")
            self.entry_cpf.focus()
            return
        
        if not telefone:
            messagebox.showerror("Erro", "Telefone é obrigatório!")
            self.entry_telefone.focus()
            return
        
        if not senha:
            messagebox.showerror("Erro", "Senha é obrigatória!")
            self.entry_senha.focus()
            return
        
        if senha != confirmar_senha:
            messagebox.showerror("Erro", "As senhas não coincidem!")
            self.entry_confirmar_senha.focus()
            return
        
        # Validações do controller
        if not self.controller.validar_email(email):
            messagebox.showerror("Erro", "Email inválido!")
            self.entry_email.focus()
            return
        
        if self.controller.email_ja_existe(email):
            messagebox.showerror("Erro", "Email já cadastrado!")
            self.entry_email.focus()
            return
        
        if not self.controller.validar_cpf(cpf):
            messagebox.showerror("Erro", "CPF inválido!")
            self.entry_cpf.focus()
            return
        
        if self.controller.cpf_ja_existe(cpf):
            messagebox.showerror("Erro", "CPF já cadastrado!")
            self.entry_cpf.focus()
            return
        
        # Armazena dados temporariamente
        self.leitor_temporario = {
            'nome': nome,
            'email': email,
            'cpf': cpf,
            'telefone': telefone,
            'senha': senha
        }
        
        # Abre tela de confirmação
        self.abrir_tela_confirmacao()
    
    def abrir_tela_confirmacao(self):
        """Abre a tela de confirmação dos dados."""
        TelaConfirmacaoLeitor(self, self.leitor_temporario)
    
    def limpar_campos(self):
        """Limpa todos os campos do formulário."""
        self.entry_nome.delete(0, tk.END)
        self.entry_email.delete(0, tk.END)
        self.entry_cpf.delete(0, tk.END)
        self.entry_telefone.delete(0, tk.END)
        self.entry_senha.delete(0, tk.END)
        self.entry_confirmar_senha.delete(0, tk.END)
        self.entry_nome.focus()
    
    def fechar(self):
        """Fecha a tela de cadastro."""
        self.destroy()


class TelaConfirmacaoLeitor(tk.Toplevel):
    """Tela para confirmar os dados do leitor antes de salvar."""
    
    def __init__(self, parent, dados_leitor):
        super().__init__(parent)
        self.parent = parent
        self.dados_leitor = dados_leitor
        self.controller = LeitorController()
        
        self.title("Confirmar Cadastro")
        self.geometry("500x400")
        self.resizable(False, False)
        
        # Configurar para fechar apenas esta janela
        self.protocol("WM_DELETE_WINDOW", self.fechar)
        
        self.criar_interface()
        centralizar_janela(self)
    
    def criar_interface(self):
        """Cria a interface da tela de confirmação."""
        # Título
        titulo = tk.Label(self, text="Confirmar Dados do Leitor", 
                         font=('Helvetica', 16, 'bold'))
        titulo.pack(pady=20)
        
        # Frame principal
        frame_principal = tk.Frame(self)
        frame_principal.pack(pady=10, padx=20, fill='both', expand=True)
        
        # Título da seção
        tk.Label(frame_principal, text="Revise os dados antes de confirmar:", 
                font=('Helvetica', 12, 'bold')).pack(anchor='w', pady=(0, 15))
        
        # Frame dos dados
        frame_dados = tk.Frame(frame_principal, relief=tk.RAISED, bd=2)
        frame_dados.pack(fill='both', expand=True, pady=(0, 20))
        
        # Exibir dados do leitor
        dados_texto = f"""
Nome: {self.dados_leitor['nome']}
Email: {self.dados_leitor['email']}
CPF: {self.dados_leitor['cpf']}
Telefone: {self.dados_leitor['telefone']}
        """
        
        tk.Label(frame_dados, text=dados_texto, 
                font=('Helvetica', 11), justify=tk.LEFT).pack(pady=20, padx=20)
        
        # Frame dos botões
        frame_botoes = tk.Frame(frame_principal)
        frame_botoes.pack(pady=10)
        
        # Botão Salvar
        btn_salvar = tk.Button(frame_botoes, text="Salvar Leitor", 
                              command=self.salvar_leitor, width=15, height=2,
                              bg='#4CAF50', fg='white', font=('Helvetica', 10, 'bold'))
        btn_salvar.pack(side=tk.LEFT, padx=10)
        
        # Botão Editar
        btn_editar = tk.Button(frame_botoes, text="Editar Dados", 
                              command=self.editar_dados, width=15, height=2,
                              bg='#FF9800', fg='white', font=('Helvetica', 10, 'bold'))
        btn_editar.pack(side=tk.LEFT, padx=10)
        
        # Botão Cancelar
        btn_cancelar = tk.Button(frame_botoes, text="Cancelar", 
                                command=self.fechar, width=15, height=2,
                                bg='#f44336', fg='white', font=('Helvetica', 10, 'bold'))
        btn_cancelar.pack(side=tk.LEFT, padx=10)
    
    def salvar_leitor(self):
        """Salva o leitor definitivamente."""
        sucesso, mensagem = self.controller.cadastrar_leitor(
            self.dados_leitor['nome'],
            self.dados_leitor['email'],
            self.dados_leitor['cpf'],
            self.dados_leitor['senha'],
            self.dados_leitor['telefone']
        )
        
        if sucesso:
            messagebox.showinfo("Sucesso", mensagem)
            self.parent.limpar_campos()  # Limpa o formulário original
            self.destroy()
        else:
            messagebox.showerror("Erro", mensagem)
    
    def editar_dados(self):
        """Volta para a tela de edição."""
        self.destroy()
    
    def fechar(self):
        """Fecha a tela de confirmação."""
        self.destroy()
