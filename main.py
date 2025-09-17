# --- main.py ---
from views.tela_login import TelaLogin
from views.tela_leitor import TelaLeitor
from views.tela_admin import TelaAdmin

if __name__ == '__main__':
    # Loop principal que permite a navegação e o ciclo de logout -> login
    while True:
        # 1. Cria a tela de login e espera ela ser fechada
        tela_login = TelaLogin()
        tela_login.mainloop()

        # 2. Pega o resultado que a tela de login guardou
        resultado = tela_login.resultado

        # 3. Decide o que fazer
        if resultado['tipo'] == 'SAIR':
            # Se o usuário fechou o login, encerra o programa
            break 
        
        elif resultado['tipo'] == 'Leitor':
            # Cria a tela do leitor e espera ela ser fechada (logout)
            tela_leitor = TelaLeitor(resultado['nome'])
            tela_leitor.mainloop()

        elif resultado['tipo'] == 'Administrador':
            # Cria a tela do admin e espera ela ser fechada (logout)
            tela_admin = TelaAdmin(resultado['nome'])
            tela_admin.mainloop()
            
    print("Programa finalizado.")