from models.funcionario import Funcionario

class Gerente(Funcionario):
    def __init__(self, nome, idade, salario_base, equipe) -> None:
        super().__init__(nome, idade, salario_base)
        self.equipe = equipe

    def calcular_salario(self):
        return self.salario_base + 100 * len(self.equipe)