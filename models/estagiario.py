from models.funcionario import Funcionario

class Estagiario(Funcionario):

    def __init__(self, nome, idade, salario_base, bolsa) -> None:
        super().__init__(nome, idade, salario_base=0)
        self.bolsa = bolsa

    def calcular_salario(self):
        return self.bolsa