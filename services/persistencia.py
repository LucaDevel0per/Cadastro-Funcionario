import csv

CAMINHO_CSV = 'db/funcionarios.csv'
CAMPOS = ['nome', 'idade', 'cargo', 'salario_base']

def salvar_funcionarios_csv(funcionarios):
    with open(CAMINHO_CSV, mode='w', newline='', encoding='utf-8') as arquivo:
        escritor = csv.DictWriter(arquivo, fieldnames=CAMPOS)
        escritor.writeheader()
        escritor.writerows(funcionarios)

def carregar_funcionarios_csv():
    try:
        with open(CAMINHO_CSV, mode='r', encoding='utf-8') as arquivo:
            leitor = csv.DictReader(arquivo)
            return [
                {
                    'nome': linha['nome'],
                    'idade': int(linha['idade']), 
                    'cargo': linha['cargo'], 
                    'salario_base': float(linha['salario_base']) 
                }
                for linha in leitor
            ]
    except FileNotFoundError:
        return []