'''Problema: Crie uma classe "Pessoa" com os atributos "nome" e "idade". 
Crie um método "apresentar" que imprime na tela uma mensagem com o nome e a idade da pessoa.

Instruções: Crie um objeto da classe "Pessoa" com nome "Maria" e idade 30. Chame o método "apresentar" do objeto criado.

Resultado esperado: "Meu nome é Maria e tenho 30 anos."
'''

class Pessoa:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade

    def apresentar(self):
        print(f"Meu nome é {self.nome} e tenho {self.idade} anos.")
    
pessoa1 = Pessoa("Maria", 30)

print('-' * 33)
pessoa1.apresentar()

'''Problema: Crie uma classe "Circulo" com o atributo "raio". Crie um método "calcularArea" que retorna a área do círculo. 
Considere π = 3.14.

Instruções: Crie um objeto da classe "Circulo" com raio 5. Calcule e imprima a área do círculo usando o método "calcularArea".

Resultado esperado: 78.5
'''

class Circulo:
    def __init__(self, raio):
        self.raio = raio
    
    def calcular_area(self):
        area = 3.14 * (self.raio ** 2)
        return area
    
circulo1 = Circulo(5)

print('-' * 33)
print(circulo1.calcular_area())

'''Problema: Crie uma classe "Livro" com os atributos "titulo", "autor" e "ano". 
Crie um método "informacoes" que retorna uma string com as informações do livro no formato "titulo - autor (ano)".

Instruções: Crie um objeto da classe "Livro" com título "O Senhor dos Anéis", autor "J. R. R. Tolkien" e ano 1954. 
Chame o método "informacoes" do objeto criado e imprima o resultado.

Resultado esperado: O resultado esperado é que o método "informacoes" retorne a string "O Senhor dos Anéis - J. R. R. Tolkien (1954)".

'''

class Livro:
    def __init__(self, titulo, autor, ano):
        self.titulo = titulo
        self.autor = autor
        self.ano = ano

    def informacoes(self):
        print(f"{self.titulo} - {self.autor} ({self.ano})")

livro1 = Livro("O Senhor dos Anéis", "J. R. R. Tolkien", 1954)

print('-' * 33)
livro1.informacoes()

'''Problema: Crie uma classe "Funcionario" com os atributos "nome", "salario" e "departamento". 
Crie um método "aumentarSalario" que recebe um valor percentual como parâmetro e 
aumenta o salário do funcionário de acordo com o valor informado. 
Crie também um método "informacoes" que retorna uma string com as informações do funcionário no formato "nome - departamento - salario".

Instruções: Crie um objeto da classe "Funcionario" com nome "João", salário 3000 e departamento "Vendas". 
Aumente o salário do funcionário em 10% usando o método "aumentarSalario". 
Chame o método "informacoes" do objeto criado e imprima o resultado.

Resultado esperado:O resultado esperado é que o método "informacoes" retorne a string "João - Vendas - 3300.0".
'''

class Funcionario:
    def __init__(self, nome, salario, departamento):
        self.nome = nome
        self.salario = salario
        self.departamento = departamento

    def aumentar_salario(self, percentual):
        self.salario = self.salario * (percentual/100) + self.salario

    def informacoes(self):
        print(f"{self.nome} - {self.departamento} - {self.salario}")

funcionario1 = Funcionario("João", 3000, "Vendas")

funcionario1.aumentar_salario(10)
print('-' * 33)
funcionario1.informacoes()

'''Problema: Crie uma classe "Carro" com os atributos "marca", "modelo" e "ano". 
Crie um método "informacoes" que retorna uma string com as informações do carro no formato "marca - modelo - ano". 
Crie também um método "acelerar" que recebe uma velocidade como parâmetro e imprime uma mensagem indicando que o carro 
acelerou para a velocidade informada.

Instruções: Crie um objeto da classe "Carro" com marca "Fiat", modelo "Uno" e ano 2000. 
Chame o método "informacoes" do objeto criado e imprima o resultado. 
Em seguida, chame o método "acelerar" do objeto criado com uma velocidade de 80 km/h e imprima a mensagem retornada pelo método.

Resultado esperado: O resultado esperado é que o método "informacoes" retorne a string "Fiat - Uno - 2000". 
O resultado esperado é que o método "acelerar" imprima na tela a mensagem "O carro Fiat Uno acelerou para 80 km/h".
'''

class Carro:
    def __init__(self, marca, modelo, ano):
        self.marca = marca
        self.modelo = modelo
        self.ano = ano

    def informacoes(self):
        return (f"{self.marca} - {self.modelo} - {self.ano}")

    def acelerar(self, velocidade):
        return (f"O carro {self.marca} {self.modelo} acelerou para {velocidade} km/h")

carro1 = Carro("Fiat", "Uno", 2000)

print('-' * 33)
print(carro1.informacoes())
print(carro1.acelerar(80))

'''Problema: Crie uma classe chamada "Agenda" que tenha como atributos uma lista de contatos e o número máximo de contatos permitidos. 
Cada contato deve ser um objeto da classe "Contato", que deve ter como atributos o nome e o telefone. 
A classe "Agenda" deve ter os métodos "adicionar_contato", que deve receber um objeto "Contato" e adicioná-lo à lista de contatos, 
e "remover_contato", que deve receber um nome e remover da lista de contatos o contato que tiver esse nome. 
Além disso, crie o método "informacoes" que retorna uma string contendo o nome e o telefone de cada contato.
'''

class Contato:
    def __init__(self, nome, telefone):
        self.nome = nome
        self.telefone = telefone

class Agenda:
    def __init__(self, max_contatos):
        self.contatos = []
        self.max_contatos = max_contatos

    def adicionar_contato(self, contato):
        if len(self.contatos) < self.max_contatos:
            self.contatos.append(contato)
            print(f"Contato {contato.nome} adicionado com sucesso!")
        else:
            print("A agenda está cheia. Não é possível adicionar mais contatos.")

    def remover_contato(self, nome):
        for contato in self.contatos:
            if contato.nome == nome:
                self.contatos.remove(contato)
                print(f"Contato {nome} removido com sucesso!")
                return
        print(f"Contato {nome} não encontrado na agenda.")

    def informacoes(self):
        info = ""
        for contato in self.contatos:
            info += f"Nome: {contato.nome}\nTelefone: {contato.telefone}\n\n"
        return info

# Criando uma agenda com capacidade para 3 contatos
agenda = Agenda(3)

# Criando alguns contatos
contato1 = Contato("João", "1111-1111")
contato2 = Contato("Maria", "2222-2222")
contato3 = Contato("José", "3333-3333")
contato4 = Contato("Ana", "4444-4444")

# Adicionando os contatos à agenda
agenda.adicionar_contato(contato1)
agenda.adicionar_contato(contato2)
agenda.adicionar_contato(contato3)

# Tentando adicionar um quarto contato (deve exibir uma mensagem de erro)
agenda.adicionar_contato(contato4)

# Exibindo as informações dos contatos na agenda
print(agenda.informacoes())

# Removendo o contato "João" da agenda
agenda.remover_contato("João")

# Exibindo as informações dos contatos na agenda novamente (sem o contato removido)
print(agenda.informacoes())

'''Problema: Crie uma classe chamada "Funcionario" que tenha como atributos o nome, o salário e a quantidade de faltas no mês. 
Crie os métodos "aumentar_salario", que deve receber um valor e somá-lo ao salário atual, 
e "descontar_falta", que deve receber um valor e subtraí-lo do salário, 
proporcionalmente à quantidade de faltas no mês (cada falta equivale a 1/30 do salário). 
Além disso, crie o método "informacoes" que retorna uma string contendo o nome, o salário atual e a quantidade de faltas no mês.'''

class Funcionario:
    def __init__(self, nome, salario, faltas):
        self.nome = nome
        self.salario = salario
        self.faltas = faltas

    def aumentar_salario(self, valor):
        self.salario = self.salario + valor

    def descontar_falta(self, valor):
        valor = (self.salario * 1/30) * self.faltas
        self.salario = self.salario - valor
        return self.salario

    def informacoes(self):
        return f"{self.nome} - Salário atual: {self.salario} - Quantidade de faltas no mês: {self.faltas}"
    
funcionario2 = Funcionario("João", 1000, 0)
funcionario2.aumentar_salario(100)
funcionario3 = Funcionario("Maria", 1000, 3)
funcionario3.descontar_falta(3)

print('-' * 33)
print(funcionario2.informacoes())
print(funcionario3.informacoes())

'''Problema: Crie uma classe chamada "Pessoa" que tenha como atributos o nome, a idade e o peso. 
Crie também os métodos "comer", que deve receber um valor em gramas e 
adicionar ao peso da pessoa, e "envelhecer", que deve aumentar a idade em um ano e, se a idade for maior ou igual a 18, 
aumentar o peso em 1 kg. Além disso, crie o método "informacoes" que retorna uma string contendo o nome, a idade e o peso atual.
'''

class Pessoa:
    def __init__(self, nome, idade, peso):
        self.nome = nome
        self.idade = idade
        self.peso = peso

    def comer(self, gramas):
        self.peso = self.peso + gramas

    def envelhecer(self):
        self.idade = self.idade + 1
        if self.idade >= 18:
            self.peso += 1000
        return self.peso
    
    def informacoes(self):
        return "Nome: {} \nIdade: {} \nPeso atual: {:,} gramas".format(self.nome, self.idade, self.peso).replace(',', '.')
    
pessoa2 = Pessoa("João", 20, 100000)
pessoa2.comer(100)
pessoa3 = Pessoa("Maria", 20, 100000)
pessoa3.envelhecer()

print('-' * 33)
print(pessoa2.informacoes())
print(pessoa3.informacoes())