         

# class Pessoa():
#     def __init__(self, nome, idade):
#         self.nome = nome
#         self.idade = idade

#     def getNome(self):
#          return self.nome
#     def getIdade(self):
#         return self.idade
    
# pessoa1 = Pessoa("Maria", 30)

# print(f"Meu nome é {pessoa1.getNome()} e eu tenho {pessoa1.getIdade()}")


#  Crie uma classe "Circulo" com o atributo "raio". Crie um método "calcularArea" que retorna a área do círculo. Considere π = 3.14.

# class Circulo:
#     def __init__(self, raio):
#         self.raio = raio

#     def area(self):
#         area = 3.14 * (self.raio**2)
#         return area
    
# circulo = Circulo(5)

# print(circulo.area())


# class Livro:
#     def __init__(self, titulo, autor, ano):
#         self.titulo = titulo
#         self.autor = autor
#         self.ano = ano

#     def informacoes(self):
#         print(f"{self.titulo} - {self.autor} ({self.ano})")


# livro1 = Livro("O Senhor dos Anéis", "J. R. R. Tolkien", 1954 )

# livro1.informacoes()


class Funcionario:
    def __init__(self, nome, salario, departamento):
        self.nome = nome
        self.salario = salario
        self.departamento = departamento

    def aumentoSalario(self):
        self.salario = self.salario + self.salario/100 * 10
       
    
    def informacoe(self):
        a = print(f"{self.nome} - {self.departamento} - {self.salario}") 
        return a
    




funcionario1 = Funcionario("João", 3000, "Vendas")


funcionario1.aumentoSalario()
print(funcionario1.informacoe())




