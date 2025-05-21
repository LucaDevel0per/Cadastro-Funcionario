from models.funcionario import Funcionario

class Desenvolvedor(Funcionario):

    def __init__(self, nome, idade, salario_base, projetos) -> None:
        super().__init__(nome, idade, salario_base)
        self.projetos = projetos

    def calcular_salario(self):
        return self.salario_base + 100 * len(self.projetos)