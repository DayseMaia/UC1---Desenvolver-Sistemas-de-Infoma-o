class Funcionario:
    def __init__(self, nome, salario):
        self.nome = nome
        self.salario = salario

    def aumentar_salario(self, percentual_aumento):
        self.salario = self.salario * (100 + percentual_aumento)/100
        return self.salario
    
harry = Funcionario("Harry", 3000)
harry.aumentar_salario(10)

print("Salário com aumento:", harry.salario)