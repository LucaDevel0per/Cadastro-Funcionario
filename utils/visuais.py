from tabulate import tabulate

def exibir_tabela(lista_funcionarios):
    if not lista_funcionarios:
        print("Nenhum dado para exibir")
        return
    print("\n📋 Funcionários Cadastrados:\n")
    print(tabulate(lista_funcionarios, headers="keys", tablefmt="fancy_grid", numalign="center", stralign="center"))