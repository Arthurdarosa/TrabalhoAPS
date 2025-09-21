# import tkinter as tk
# from tkinter import messagebox

# def centralizar_janela(janela):
#     janela.update_idletasks()
#     largura = janela.winfo_width()
#     altura = janela.winfo_height()
#     x = (janela.winfo_screenwidth() // 2) - (largura // 2)
#     y = (janela.winfo_screenheight() // 2) - (altura // 2)
#     janela.geometry(f'{largura}x{altura}+{x}+{y}')

# class TelaGerenciarUsuarios(tk.Toplevel):
#     def __init__(self, parent):
#         super().__init__(parent)
#         self.title("Gerenciar Usuários")
#         self.geometry("500x400")
        
#         tk.Label(self, text="Lista de Usuários Cadastrados", font=('Helvetica', 16)).pack(pady=10)

#         # Frame da lista
#         frame_lista = tk.Frame(self)
#         frame_lista.pack(pady=10, padx=10, expand=True, fill='both')
        
#         self.listbox_usuarios = tk.Listbox(frame_lista, font=('Consolas', 10))
#         self.listbox_usuarios.pack(side=tk.LEFT, expand=True, fill='both')

#         scrollbar = tk.Scrollbar(frame_lista, orient='vertical', command=self.listbox_usuarios.yview)
#         scrollbar.pack(side=tk.RIGHT, fill='y')
#         self.listbox_usuarios.config(yscrollcommand=scrollbar.set)
        
#         # Frame de botões
#         frame_botoes = tk.Frame(self)
#         frame_botoes.pack(pady=10)
#         tk.Button(frame_botoes, text="Editar Selecionado", command=self.funcao_placeholder).pack(side=tk.LEFT, padx=5)
#         tk.Button(frame_botoes, text="Excluir Selecionado", command=self.funcao_placeholder).pack(side=tk.LEFT, padx=5)
#         tk.Button(self, text="Voltar", command=self.destroy).pack(pady=5)

#         self.popular_lista()
#         centralizar_janela(self)
#         self.transient(parent)
#         self.grab_set()

#     def popular_lista(self):
#         # --- LÓGICA SIMULADA ---
#         usuarios_falsos = [("ana@email.com", "Leitor"), ("carlos@admin.com", "Administrador"), ("joao@leitor.com", "Leitor")]
#         for email, tipo in usuarios_falsos:
#             self.listbox_usuarios.insert(tk.END, f"{email:<30} | Tipo: {tipo}")

#     def funcao_placeholder(self):
#         messagebox.showinfo("Em Breve", "Funcionalidade a ser implementada!")