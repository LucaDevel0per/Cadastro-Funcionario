class Funcionario:
    def __init__(self, nome, idade, salario_base) -> None:
        self.nome = nome
        self.idade = idade
        self.salario_base = salario_base

    def calcular_salario(self):
        return self.salario_base
    
    def __str__(self) -> str:
        return f'{self.nome} ({self.__class__.__name__}) - R${self.calcular_salario():.2f}'
    
luca = Funcionario('Luca', 19, 2000)
