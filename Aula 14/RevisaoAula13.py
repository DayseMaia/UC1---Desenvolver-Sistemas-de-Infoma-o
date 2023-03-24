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
print('-' * 33)
#################################################################################################
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
            print("Agenda cheia. Não é possível adicionar mais contatos.")

    def remover_contato(self, nome):
        for contato in self.contatos:
            if contato.nome == nome:
                self.contatos.remove(contato)
                print(f"Contato {nome} removido com sucesso!")
                return
        print(f"Contato {nome} não encontrado na agenda.")

    def informacoes(self):
        informacao = ""
        for contato in self.contatos:
            informacao += f"Nome: {contato.nome}\nTelefone: {contato.telefone}\n"
        return informacao

agenda = Agenda(3)

contato1 = Contato("João", "1111-1111")
contato2 = Contato("Maria", "2222-2222")
contato3 = Contato("José", "3333-3333")

agenda.adicionar_contato(contato1)
agenda.adicionar_contato(contato2)
agenda.adicionar_contato(contato3)

print('-' * 33)
print(agenda.informacoes())

agenda.remover_contato("João")

print(agenda.informacoes())
print('-' * 33)
#################################################################################################
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

print(funcionario2.informacoes())
print(funcionario3.informacoes())
print('-' * 33)
#################################################################################################
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

print(pessoa2.informacoes())
print(pessoa3.informacoes())
print('-' * 33)
#################################################################################################