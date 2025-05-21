
# Sistema de Gerenciamento de Funcionários

Um sistema simples em Python para gerenciar funcionários, com funcionalidades de cadastro, listagem, busca, edição e exclusão.

## Funcionalidades

- **Cadastro de Funcionários**: Adicione novos funcionários com nome, idade, cargo e salário
- **Listagem de Funcionários**: Visualize todos os funcionários cadastrados
- **Busca por Nome**: Encontre funcionários específicos pelo nome
- **Edição de Dados**: Atualize informações de funcionários existentes
- **Exclusão de Registros**: Remova funcionários do sistema
- **Persistência de Dados**: Armazenamento em arquivo CSV

## Estrutura do Projeto

```
Sistema-Gerenciamento-Funcionarios/
│
├── models/                    # Classes de entidades
│   ├── funcionario.py         # Classe base para funcionários
│   ├── gerente.py             # Classe específica para gerentes
│   ├── desenvolvedor.py       # Classe específica para desenvolvedores
│   └── estagiario.py          # Classe específica para estagiários
│
├── services/                  # Lógica de negócios
│   ├── sistema.py             # Funções principais do sistema
│   └── persistencia.py        # Funções para salvar/carregar dados
│
├── db/                        # Armazenamento de dados
│   ├── funcionarios.py        # Módulo para acesso aos dados
│   └── funcionarios.csv       # Arquivo de dados
│
├── utils/                     # Utilitários
│   └── visuais.py             # Funções para visualização de dados
│
└── main.py                    # Ponto de entrada do programa
```

## Como Instalar

1. Clone o repositório:
   ```bash
   git clone https://github.com/seu-usuario/Sistema-Gerenciamento-Funcionarios.git
   cd Sistema-Gerenciamento-Funcionarios
   ```

2. Não são necessárias bibliotecas externas além do Python 3.10+

## Como Usar

1. Execute o programa principal:
   ```bash
   python main.py
   ```

2. Use o menu interativo para navegar pelas opções:
   - **Cadastrar**: Adicione novos funcionários ao sistema
   - **Listar**: Veja todos os funcionários cadastrados
   - **Buscar**: Encontre, edite ou exclua um funcionário específico
   - **Sair**: Encerre o programa

## Exemplos de Uso

### Cadastrar Funcionário
1. Selecione a opção "1" no menu principal
2. Informe o nome, idade e cargo do funcionário
3. O sistema calculará o salário base de acordo com o cargo

### Buscar e Editar Funcionário
1. Selecione a opção "3" no menu principal
2. Digite o nome do funcionário que deseja encontrar
3. Após localizar, escolha a opção para editar ou excluir

## Tecnologias Utilizadas

- Python 3.10+
- Módulo CSV para persistência de dados
- Programação Orientada a Objetos
- Herança de classes para diferentes tipos de funcionários

## Autores

- Desenvolvido como projeto de estudo em Python


