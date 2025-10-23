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

# MUDANÇA 1: Deve ser Toplevel, não Tk
class TelaDevolverEmprestimo(tk.Toplevel): 
    """
    Esta tela é uma JANELA FILHA (Toplevel) para "Registrar Devolução".
    """
    # MUDANÇA 2: Deve aceitar 'parent' no __init__
    def __init__(self, parent): 
        super().__init__(parent) # MUDANÇA 3: Inicia o Toplevel com o parent
        
        self.title("Registrar Devolução")
        self.geometry("800x500")

        # --- Variável de Estado ---
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
        
        tk.Button(frame_botoes, text="Marcar como Devolvido", command=self.marcar_devolvido).pack(side=tk.LEFT, padx=5)
        
        # MUDANÇA 4: O botão volta a ser "Voltar" (para fechar o Toplevel)
        tk.Button(self, text="Voltar", command=self.destroy).pack(pady=5)
        
        centralizar_janela(self)
        
        # MUDANÇA 5: Essas linhas são necessárias para Toplevel (janela modal)
        self.transient(parent)
        self.grab_set()

    def buscar_emprestimo(self):
        """
        Busca o empréstimo pelo ID digitado.
        (Isto deve chamar o seu controller no futuro)
        """
        self.listbox_resultado.delete(0, tk.END)
        self.emprestimo_encontrado = None
        
        emprestimo_id = self.entry_busca.get().strip()
        if not emprestimo_id:
            messagebox.showwarning("Entrada Inválida", "Por favor, digite um ID de empréstimo.")
            return

        # --- LÓGICA SIMULADA ---
        emprestimos_falsos_db = {
            "12345": {"id": 12345, "livro": "Duna", "usuario": "ana@email.com", "estado": "Ativo"},
            "67890": {"id": 67890, "livro": "1984", "usuario": "bruno@email.com", "estado": "Atrasado"},
        }
        
        self.emprestimo_encontrado = emprestimos_falsos_db.get(emprestimo_id)
        # --- FIM DA LÓGICA SIMULADA ---

        if self.emprestimo_encontrado:
            emp = self.emprestimo_encontrado
            texto = f"ID: {emp['id']} | LIVRO: {emp['livro']:<20} | USUÁRIO: {emp['usuario']:<20} | ESTADO: {emp['estado']}"
            self.listbox_resultado.insert(tk.END, texto)
        else:
            messagebox.showwarning("Não Encontrado", f"Empréstimo com ID '{emprestimo_id}' não foi encontrado ou já foi devolvido.")

    def marcar_devolvido(self):
        """
        Registra a devolução do empréstimo atualmente em exibição.
        """
        if not self.emprestimo_encontrado:
            messagebox.showerror("Erro", "Nenhum empréstimo selecionado. Busque um ID válido primeiro.")
            return

        emprestimo_id = self.emprestimo_encontrado['id']
        livro_titulo = self.emprestimo_encontrado['livro']

        # --- LÓGICA SIMULADA ---
        # No seu app real, você chamaria: self.controller.registrar_devolucao(emprestimo_id)
        
        messagebox.showinfo("Sucesso", f"Devolução do livro '{livro_titulo}' (ID: {emprestimo_id}) registrada!")
        
        self.listbox_resultado.delete(0, tk.END)
        self.entry_busca.delete(0, tk.END)
        self.emprestimo_encontrado = None
        # --- FIM DA LÓGICA SIMULADA ---

# --- O 'if __name__ == "__main__":' foi removido ---
# Este arquivo agora deve ser apenas importado, e não executado diretamente.