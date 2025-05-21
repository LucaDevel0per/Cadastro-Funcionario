from services.sistema import cadastrar_Funcionario, listar_funcionarios, buscar_por_nome
import sys
from db.funcionarios import funcionarios

def menu():
    while True:
        print("--- Bem-vindo ao sistema de gerenciamento GoLIve ---")
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
                print("1. Linha")
                print("2. Tabela")
                try:
                    escolha2 = int(input("Gostaria de visualizar em: "))
                    listar_funcionarios(funcionarios, escolha2)
                    continue
                except ValueError:
                    print("Escolha apenas números.")
                    break
            case '3':
                nome = input("Qual é o nome do funcionario que você deseja buscar? ")
                buscar_por_nome(nome, funcionarios)
                continue
            case '4':
                print("Obrigado por usar o ERP GoLive!")
                sys.exit()

if __name__ == '__main__':
    menu()
