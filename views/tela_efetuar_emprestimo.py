import tkinter as tk
from tkinter import messagebox

def centralizar_janela(janela):
    """Função auxiliar para centralizar a janela no monitor."""
    janela.update_idletasks()
    largura = janela.winfo_width()
    altura = janela.winfo_height()
    x = (janela.winfo_screenwidth() // 2) - (largura // 2)
    y = (janela.winfo_screenheight() // 2) - (altura // 2)
    janela.geometry(f'{largura}x{altura}+{x}+{y}')

class TelaRegistrarColeta(tk.Toplevel): 
    """
    Esta tela é uma JANELA FILHA (Toplevel) para "Registrar Coleta".
    Ela busca um empréstimo em "Espera" e o marca como "Ativo".
    """
    def __init__(self, parent): 
        super().__init__(parent) 
        
        self.title("Registrar Coleta de Livro")
        self.geometry("600x300")

        # --- Variável de Estado ---
        # Armazena o objeto do empréstimo encontrado na busca
        self.emprestimo_encontrado = None 

        # --- Frame de Busca ---
        frame_busca = tk.Frame(self)
        frame_busca.pack(pady=10, padx=10, fill='x')
        
        tk.Label(frame_busca, text="ID do Empréstimo:", font=('Helvetica', 10)).pack(side=tk.LEFT, padx=5)
        
        self.entry_busca = tk.Entry(frame_busca, font=('Helvetica', 10), width=30)
        self.entry_busca.pack(side=tk.LEFT, fill='x', expand=True, padx=5)
        
        tk.Button(frame_busca, text="Buscar", command=self.buscar_emprestimo).pack(side=tk.LEFT)

        # --- Frame da Lista (Resultado) ---
        tk.Label(self, text="Resultado da Busca", font=('Helvetica', 14)).pack(pady=5)
        
        frame_lista = tk.Frame(self)
        frame_lista.pack(pady=10, padx=10, expand=True, fill='both')
        
        self.listbox_resultado = tk.Listbox(frame_lista, font=('Consolas', 10), height=3)
        self.listbox_resultado.pack(side=tk.LEFT, expand=True, fill='both')

        scrollbar = tk.Scrollbar(frame_lista, orient='vertical', command=self.listbox_resultado.yview)
        scrollbar.pack(side=tk.RIGHT, fill='y')
        self.listbox_resultado.config(yscrollcommand=scrollbar.set)
        
        # --- Botoes de Ação ---
        frame_botoes = tk.Frame(self)
        frame_botoes.pack(pady=10)
        
        # Botão modificado para "Registrar Coleta"
        tk.Button(frame_botoes, text="Registrar Coleta", command=self.registrar_coleta).pack(side=tk.LEFT, padx=5)
        
        tk.Button(self, text="Voltar", command=self.destroy).pack(pady=5)
        
        centralizar_janela(self)
        
        self.transient(parent)
        self.grab_set()

    def buscar_emprestimo(self):
        """
        Busca o empréstimo pelo ID e verifica se está "Em Espera".
        """
        self.listbox_resultado.delete(0, tk.END)
        self.emprestimo_encontrado = None
        
        emprestimo_id = self.entry_busca.get().strip()
        if not emprestimo_id:
            messagebox.showwarning("Entrada Inválida", "Por favor, digite um ID de empréstimo.")
            return

        # --- LÓGICA SIMULADA ---
        # No seu app real, você chamaria o controller para buscar o empréstimo
        # ex: emprestimo = self.controller.consultar_emprestimo_por_id(emprestimo_id)
        
        # Dados falsos para simulação
        emprestimos_falsos_db = {
            "12345": {"id": 12345, "livro": "Duna", "usuario": "ana@email.com", "estado": "Ativo"},
            "67890": {"id": 67890, "livro": "1984", "usuario": "bruno@email.com", "estado": "Atrasado"},
            "55555": {"id": 55555, "livro": "Neuromancer", "usuario": "carla@email.com", "estado": "Espera"},
        }
        
        emprestimo = emprestimos_falsos_db.get(emprestimo_id)
        # --- FIM DA LÓGICA SIMULADA ---

        # Validação crucial: o empréstimo existe E está no estado "Espera"
        if emprestimo and emprestimo['estado'] == "Espera":
            self.emprestimo_encontrado = emprestimo
            emp = self.emprestimo_encontrado
            texto = f"ID: {emp['id']} | LIVRO: {emp['livro']:<20} | USUÁRIO: {emp['usuario']:<20} | ESTADO: {emp['estado']}"
            self.listbox_resultado.insert(tk.END, texto)
        else:
            # Mensagem de erro específica
            messagebox.showwarning("Não Encontrado", f"Empréstimo com ID '{emprestimo_id}' não foi encontrado ou não está aguardando coleta.")

    def registrar_coleta(self):
        """
        Registra a coleta do empréstimo (muda de "Espera" para "Ativo").
        """
        # Verifica se um empréstimo foi buscado e encontrado
        if not self.emprestimo_encontrado:
            messagebox.showerror("Erro", "Nenhum empréstimo selecionado. Busque um ID válido primeiro.")
            return

        emprestimo_id = self.emprestimo_encontrado['id']
        livro_titulo = self.emprestimo_encontrado['livro']

        # --- LÓGICA SIMULADA ---
        # No seu app real, você chamaria o controller:
        # try:
        #   self.controller.registrar_coleta(emprestimo_id) # Um novo método no seu controller
        #   messagebox.showinfo("Sucesso", f"Coleta do livro '{livro_titulo}' (ID: {emprestimo_id}) registrada!")
        #   ... (limpar tela) ...
        # except Exception as e:
        #   messagebox.showerror("Erro na Coleta", str(e))
        
        # Simulação de sucesso
        messagebox.showinfo("Sucesso", f"Coleta do livro '{livro_titulo}' (ID: {emprestimo_id}) registrada com sucesso!")
        
        # Limpa a tela
        self.listbox_resultado.delete(0, tk.END)
        self.entry_busca.delete(0, tk.END)
        self.emprestimo_encontrado = None
        # --- FIM DA LÓGICA SIMULADA ---


# --- Bloco para testar esta janela individualmente ---
if __name__ == "__main__":
    
    # Cria uma janela raiz falsa para ser a 'parent'
    root = tk.Tk()
    root.title("Tela Principal (Mock)")
    root.geometry("300x200")
    centralizar_janela(root)
    
    def abrir_tela_coleta():
        # Abre a tela de coleta, passando a raiz como 'parent'
        tela = TelaRegistrarColeta(root)
        root.wait_window(tela) # Espera a tela de coleta fechar
        
    tk.Button(root, text="Abrir Tela de Coleta", command=abrir_tela_coleta).pack(pady=50)

    root.mainloop()