from models.gerente import Gerente
from models.desenvolvedor import Desenvolvedor
from models.estagiario import Estagiario
from services.persistencia import salvar_funcionarios_csv
from db.funcionarios import funcionarios
from utils.visuais import exibir_tabela


cargos = ['Gerente', 'Desenvolvedor', 'Estagiario']

salarios_base = {
    "Gerente": 8000,
    "Desenvolvedor": 5000,
    "Estagiario": 1500
}

# funcionarios = [
#     {
#         "nome": "Jonas",
#         "idade": 19,
#         "cargo": "Estagiario",
#         "salario_base": 800
#     }
# ]


def cadastrar_Funcionario():
    nome = input("Qual é o nome do funcionario? ").capitalize()
    try:
        idade = int(input(f"Qual é a idade do funcionário '{nome}'? "))
    except ValueError:
        print("Coloque uma idade válida.")
        return
    for idx, cargo in enumerate(cargos, start=1):
        print(f'{idx}. {cargo}')

    try:
        cargo_idx = int(input(f"Qual cargo do funcionário {nome}? "))
    except ValueError:
        print('Cargo inválido.')
        return

    if cargo_idx not in range(1, len(cargos) + 1):
        print(f"Cargo inválido.")
        return
    
    # adicionando elementos a dict

    cargo = cargos[cargo_idx - 1]
    salario = salarios_base[cargo]

    if cargo == 'Gerente':
        funcionario = Gerente(nome, idade, 8000, len(funcionarios)-1)
    elif cargo == 'Desenvolvedor':
        funcionario = Desenvolvedor(nome, idade, 5000, 3)
    elif cargo == 'Estagiario':
        funcionario = Estagiario(nome, idade, 1500, bolsa=2)


    funcionarios.append({
        "nome": funcionario.nome,
        "idade": funcionario.idade,
        "cargo": cargo,
        "salario_base": funcionario.salario_base
    })

    salvar_funcionarios_csv(funcionarios)

    print(f"\nFuncionário '{nome}' cadastrado com sucesso!")
    print(f"Idade: {idade} | Cargo: {cargo} | Salário: R${salario:.2f}")


def listar_funcionarios(lista, escolha):
    if not lista:
        print("\nNão há funcionários cadastrados!")
        return
    if escolha == 2:
        exibir_tabela(lista)
    elif escolha == 1:
        print("\n=== Lista de Funcionários ===")
        for i, f in enumerate(lista, 1):
            # Formatação amigável dos dados do funcionário
            nome = f.get("nome", "N/A")
            idade = f.get("idade", "N/A")
            cargo = f.get("cargo", "N/A")
            # Verificar todas as possíveis chaves de salário para compatibilidade
            salario = f.get("salario_base") or f.get("Salario base") or f.get("salario", 0)
            
            print(f"{i}. Nome: {nome} | Idade: {idade} | Cargo: {cargo} | Salário: R${salario:.2f}")
        print("=============================")
    else:
        print("Escolha 1 ou 2.")
        return

def buscar_por_nome(nome, lista):
    if not lista:
        print("\nNão há funcionários cadastrados!")
        return
    
    for idx, f in enumerate(lista):
        if f['nome'].lower() == nome.lower():
            print(f"\nFuncionário encontrado:")
            print(f"Nome: {f['nome']} | Idade: {f['idade']} | Cargo: {f['cargo']} | Salário: R${f['salario_base']:.2f}")
            
            while True:
                print("\nO que deseja fazer?")
                print("1. Editar funcionário")
                print("2. Excluir funcionário")
                print("3. Voltar ao menu principal")
                
                opcao = input("Escolha uma opção: ")
                
                if opcao == "1":
                    editar_funcionario(lista, idx)
                    return
                elif opcao == "2":
                    if confirmar_exclusao(f['nome']):
                        lista.pop(idx)
                        salvar_funcionarios_csv(lista)
                        print(f"\nFuncionário {f['nome']} excluído com sucesso!")
                    return
                elif opcao == "3":
                    return
                else:
                    print("Opção inválida!")
    
    print("Funcionário não encontrado.")

def editar_funcionario(lista, idx):
    f = lista[idx]
    print(f"\nEditando dados de {f['nome']}:")
    
    # Nome
    novo_nome = input(f"Nome ({f['nome']}): ") or f['nome']
    
    # Idade
    while True:
        nova_idade_str = input(f"Idade ({f['idade']}): ") or str(f['idade'])
        try:
            nova_idade = int(nova_idade_str)
            break
        except ValueError:
            print("Digite uma idade válida!")
    
    # Cargo
    print("Cargos disponíveis:")
    for idx, cargo in enumerate(cargos, start=1):
        print(f"{idx}. {cargo}")
    while True:
        cargo_idx_str = input(f"Cargo ({f['cargo']}): ") or "0"
        try:
            cargo_idx = int(cargo_idx_str)
            if cargo_idx == 0:
                novo_cargo = f['cargo']
                break
            elif cargo_idx in range(1, len(cargos) + 1):
                novo_cargo = cargos[cargo_idx - 1]
                break
            else:
                print("Cargo inválido!")
        except ValueError:
            print("Digite um número válido!")
    
    # Salário
    while True:
        novo_salario_str = input(f"Salário (R${f['salario_base']:.2f}): ") or str(f['salario_base'])
        try:
            novo_salario = float(novo_salario_str)
            break
        except ValueError:
            print("Digite um valor válido!")
    
    # Atualizar dados
    f['nome'] = novo_nome
    f['idade'] = nova_idade
    f['cargo'] = novo_cargo
    f['salario_base'] = novo_salario
    
    # Salvar alterações
    salvar_funcionarios_csv(lista)
    print(f"\nDados de {f['nome']} atualizados com sucesso!")

def confirmar_exclusao(nome):
    while True:
        confirma = input(f"Tem certeza que deseja excluir {nome}? (s/n): ").lower()
        if confirma in ['s', 'sim']:
            return True
        elif confirma in ['n', 'não', 'nao']:
            return False
        print("Por favor, responda com 's' ou 'n'.")