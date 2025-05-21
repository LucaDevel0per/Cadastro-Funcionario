from services.sistema import cadastrar_Funcionario, listar_funcionarios
import sys
from db.funcionarios import funcionarios

def menu():
    print("--- Bem-vindo ao sistema de gerenciamento GoLIve ---")
    while True:
        print("1. Cadastrar")
        print("2. Listar")
        print("3. Buscar")
        print("4. Sair")
        escolha = input("O que será feito? ")

        match escolha:
            case '1':
                cadastrar_Funcionario()
                continue
            case '2':
                listar_funcionarios(funcionarios)
                continue
            case '1':
                cadastrar_Funcionario()
                continue
            case '4':
                print("Obrigado por usar o ERP GoLive!")
                sys.exit()

if __name__ == '__main__':
    menu()