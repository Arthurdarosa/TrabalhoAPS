# tela_registrar_coleta.py
import tkinter as tk
from tkinter import messagebox
from controllers.registro_de_emprestimo_controller import SistemaController 
from models.estado import StatusEmprestimo 

# (Sua função centralizar_janela fica aqui)
def centralizar_janela(janela):
    janela.update_idletasks()
    largura = janela.winfo_width()
    altura = janela.winfo_height()
    x = (janela.winfo_screenwidth() // 2) - (largura // 2)
    y = (janela.winfo_screenheight() // 2) - (altura // 2)
    janela.geometry(f'{largura}x{altura}+{x}+{y}')

class TelaRegistraremprestimo(tk.Toplevel): 
    
    # 1. __init__ agora recebe o controller
    def __init__(self, parent): 
        super().__init__(parent) 
        
        # Armazena a referência do controller
        self.controller = SistemaController()
        
        self.title("Registrar Coleta de Livro")
        self.geometry("600x300")
        
        self.emprestimo_encontrado = None 

        # --- (O restante da UI é idêntico) ---
        frame_busca = tk.Frame(self)
        frame_busca.pack(pady=10, padx=10, fill='x')
        tk.Label(frame_busca, text="ID do Empréstimo:", font=('Helvetica', 10)).pack(side=tk.LEFT, padx=5)
        self.entry_busca = tk.Entry(frame_busca, font=('Helvetica', 10), width=30)
        self.entry_busca.pack(side=tk.LEFT, fill='x', expand=True, padx=5)
        tk.Button(frame_busca, text="Buscar", command=self.buscar_emprestimo).pack(side=tk.LEFT)
        tk.Label(self, text="Resultado da Busca", font=('Helvetica', 14)).pack(pady=5)
        frame_lista = tk.Frame(self)
        frame_lista.pack(pady=10, padx=10, expand=True, fill='both')
        self.listbox_resultado = tk.Listbox(frame_lista, font=('Consolas', 10), height=3)
        self.listbox_resultado.pack(side=tk.LEFT, expand=True, fill='both')
        scrollbar = tk.Scrollbar(frame_lista, orient='vertical', command=self.listbox_resultado.yview)
        scrollbar.pack(side=tk.RIGHT, fill='y')
        self.listbox_resultado.config(yscrollcommand=scrollbar.set)
        frame_botoes = tk.Frame(self)
        frame_botoes.pack(pady=10)
        tk.Button(frame_botoes, text="Registrar Coleta", command=self.registrar_coleta).pack(side=tk.LEFT, padx=5)
        tk.Button(self, text="Voltar", command=self.destroy).pack(pady=5)
        
        centralizar_janela(self)
        self.transient(parent)
        self.grab_set()

    # 2. Método de busca MODIFICADO
    def buscar_emprestimo(self):
        self.listbox_resultado.delete(0, tk.END)
        self.emprestimo_encontrado = None
        
        emprestimo_id_str = self.entry_busca.get().strip()
        if not emprestimo_id_str:
            messagebox.showwarning("Entrada Inválida", "Por favor, digite um ID de empréstimo.")
            return
            
        try:
            # O ID do empréstimo agora é um INT
            emprestimo_id = int(emprestimo_id_str)
        except ValueError:
            messagebox.showwarning("Entrada Inválida", "O ID deve ser um número.")
            return

        # --- LÓGICA REAL (chamando o controller) ---
        emprestimo = self.controller.buscar_emprestimo_por_id(emprestimo_id)
        # --- FIM DA LÓGICA REAL ---

        # Validação 1: o empréstimo existe?
        if not emprestimo:
            messagebox.showwarning("Aviso", f"Empréstimo com esse ID não foi encontrado.")
            return
        
        # Validação 2: o empréstimo está no estado PENDENTE?
        if emprestimo.status != StatusEmprestimo.PENDENTE:
            messagebox.showwarning("Aviso", f"O empréstimo não está pendente")
            return
        
        # Se chegou até aqui, o empréstimo existe E está pendente - exibe os dados
        self.emprestimo_encontrado = emprestimo
        
        # Usando os atributos reais do objeto
        livro = emprestimo.livro.titulo
        usuario = emprestimo.leitor.email
        status = emprestimo.status.value # .value pega o texto "Pendente"
        
        texto = f"ID: {emprestimo.id} | LIVRO: {livro:<20} | USUÁRIO: {usuario:<20} | ESTADO: {status}"
        self.listbox_resultado.insert(tk.END, texto)

    # 3. Método de registro MODIFICADO
    def registrar_coleta(self):
        if not self.emprestimo_encontrado:
            messagebox.showerror("Erro", "Nenhum empréstimo selecionado. Busque um ID válido primeiro.")
            return

        emprestimo_id = self.emprestimo_encontrado.id
        livro_titulo = self.emprestimo_encontrado.livro.titulo

        # --- LÓGICA REAL (chamando o controller) ---
        try:
            # O controller faz todo o trabalho pesado
            self.controller.registrar_coleta(emprestimo_id)
            
            messagebox.showinfo("Sucesso", f"Coleta do livro '{livro_titulo}' (ID: {emprestimo_id}) registrada com sucesso!")
            
            # Limpa a tela
            self.listbox_resultado.delete(0, tk.END)
            self.entry_busca.delete(0, tk.END)
            self.emprestimo_encontrado = None
            
        except Exception as e:
            # Captura qualquer erro de negócio (ex: "não está pendente")
            messagebox.showerror("Erro na Coleta", str(e))

