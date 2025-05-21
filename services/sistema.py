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
#         "Salario base": 800
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
    print(f"Idade: {idade} | Cargo: {cargo} | Salário base: R${salario:.2f}")


def listar_funcionarios(lista):
    if not lista:
        print("\nNão há funcionários cadastrados!")
        return
    
    exibir_tabela(lista)
    
    # print("\n=== Lista de Funcionários ===")
    # for i, f in enumerate(lista, 1):
    #     # Formatação amigável dos dados do funcionário
    #     nome = f.get("nome", "N/A")
    #     idade = f.get("idade", "N/A")
    #     cargo = f.get("cargo", "N/A")
    #     # Verificar se a chave é "Salario base" ou "salario" ou "salario_base"
    #     salario = f.get("Salario base") or f.get("salario") or f.get("salario_base", 0)
        
    #     print(f"{i}. Nome: {nome} | Idade: {idade} | Cargo: {cargo} | Salário: R${salario:.2f}")
    # print("=============================")

def buscar_por_nome(nome, lista):
    if not lista:
        print("\nNão há funcionários cadastrados!")
        return
    for f in lista:
        if f['nome'] == nome:
            print(f"Nome: {nome} | Idade: {f['idade']} | Cargo: {f['cargo']} | Salário: R${f['salario_base']:.2f}")
            return
    print("Funcionario não cadastrado.")

