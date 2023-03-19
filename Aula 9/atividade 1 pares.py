'''Problema: Crie uma classe "Pessoa" que represente uma pessoa, com os atributos "nome" e "idade".

Classe a ser criada: Pessoa

Métodos a serem criados: construtor (init) que recebe nome e idade como parâmetros e atribui aos atributos da classe; 
método "getNome" que retorna o nome da pessoa; método "getIdade" que retorna a idade da pessoa.

Instruções: Crie um objeto da classe "Pessoa" com nome "João" e idade "25". Imprima o nome e idade da pessoa usando os métodos criados.
'''

class Pessoa:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade

    def get_nome(self):
        return self.nome
    
    def get_idade(self):
        return self.idade
    
pessoa1 = Pessoa("João", 25)

print('-' * 33)
print("Nome:", pessoa1.get_nome(), "\nIdade:", pessoa1.get_idade())

'''Problema: Crie uma classe "Círculo" que represente um círculo, com o atributo "raio".

Classe a ser criada: Círculo

Métodos a serem criados: construtor (init) que recebe o raio como parâmetro e atribui ao atributo da classe; 
método "calcularArea" que retorna a área do círculo; método "calcularCircunferencia" que retorna a circunferência do círculo.

Instruções: Crie um objeto da classe "Círculo" com raio igual a 5. 
Calcule e imprima a área e circunferência do círculo usando os métodos criados.
'''

class Circulo:
    def __init__(self, raio):
        self.raio = raio

    def calcular_area(self):
        area = 3.14 * (self.raio ** 2)
        return area
    
    def calcular_circunferencia(self):
        circunferencia = 2 * 3.14 * self.raio
        return circunferencia
    
raio1 = Circulo(5)

print('-' * 33)
print(f"Área: {raio1.calcular_area():.2f} \nCircunferência: {raio1.calcular_circunferencia():.2f}")

'''Problema: Crie uma classe "ContaBancaria" que represente uma conta bancária, com os atributos "saldo" e "titular".

Classe a ser criada: ContaBancaria

Métodos a serem criados: construtor (init) que recebe o titular como parâmetro e atribui ao atributo da classe, 
inicializando o saldo com zero; método "depositar" que recebe um valor como parâmetro e adiciona ao saldo da conta; 
método "sacar" que recebe um valor como parâmetro e subtrai do saldo da conta, se o saldo for suficiente; 
método "consultarSaldo" que retorna o saldo da conta.

Instruções: Crie um objeto da classe "ContaBancaria" com titular "Maria". Deposite 100 reais na conta e depois faça um saque de 50 reais. Imprima o saldo da conta usando o método "consultarSaldo".
'''

class Conta_Bancaria:
    def __init__(self, titular, saldo):
        self.saldo = saldo
        self.titular = titular

    def depositar(self, valor):
        self.saldo = self.saldo + valor

    def sacar(self, valor):
        self.saldo = self.saldo - valor

    def consultar_saldo(self):
        return self.saldo
    
contabancaria1 = Conta_Bancaria("Maria", 0)

contabancaria1.depositar(100)

contabancaria1.sacar(50)

print('-' * 33)
print("Saldo:", contabancaria1.consultar_saldo())

'''Problema: Crie uma classe "Livro" que represente um livro, com os atributos "titulo", "autor" e "ano".

Classe a ser criada: Livro

Métodos a serem criados: construtor (init) que recebe o título, autor e ano como parâmetros e atribui aos atributos da classe; 
método "getTitulo" que retorna o título do livro; método "getAutor" que retorna o autor do livro; método "getAno" que retorna o ano do livro.

Instruções: Crie um objeto da classe "Livro" com título "O Senhor dos Anéis", autor "J.R.R. Tolkien" e ano "1954". 
Imprima o título, autor e ano do livro usando os métodos criados.
'''

class Livro:
    def __init__(self, titulo, autor, ano):
        self.titulo = titulo
        self.autor = autor
        self.ano = ano

    def get_titulo(self):
        return self.titulo
    
    def get_autor(self):
        return self.autor
    
    def get_ano(self):
        return self.ano
    
livro1 = Livro("O Senhor dos Anéis", "J.R.R. Tolkien", 1954)

print('-' * 33)
print(livro1.get_titulo(),",", livro1.get_autor(),",", livro1.get_ano())

'''Problema: Crie uma classe "Aluno" que represente um aluno, com os atributos "nome", "matrícula" e "notas".

Classe a ser criada: Aluno

Métodos a serem criados: construtor (init) que recebe o nome e a matrícula como parâmetros e atribui aos atributos da classe, 
inicializando a lista de notas com uma lista vazia; método "adicionarNota" que recebe uma nota como parâmetro e 
adiciona à lista de notas do aluno; método "calcularMedia" que calcula a média das notas do aluno e retorna o resultado.

Instruções: Crie um objeto da classe "Aluno" com nome "Ana" e matrícula "12345". Adicione notas 7, 8 e 9 ao objeto criado usando o 
método "adicionarNota". Calcule e imprima a média das notas do aluno usando o método "calcularMedia".
'''

class Aluno:
    def __init__(self, nome, matricula):
        self.nome = nome
        self.matricula = matricula
        self.notas = []

    def adicionar_nota(self, nota):
        self.notas.append(nota)

    def calcular_media(self):
        return sum(self.notas) / len(self.notas)
    
aluno1 = Aluno("Ana", "12345")
aluno1.adicionar_nota(7)
aluno1.adicionar_nota(8)
aluno1.adicionar_nota(9)

print('-' * 33)
print(f"{aluno1.nome} tem média: {aluno1.calcular_media()}")