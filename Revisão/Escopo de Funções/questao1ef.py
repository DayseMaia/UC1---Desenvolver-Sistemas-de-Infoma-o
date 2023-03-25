'''Escreva um programa que solicite ao usuário dois números e imprima a soma, a subtração, a multiplicação e a divisão desses números.
Crie funções separadas para cada operação matemática.'''

#Função para calcular a soma:
def calcular_soma(num1, num2):
    num1 = float(num1)
    num2 = float(num2)
    soma = num1 + num2
    return soma

#Função para calcular a subtração:
def calcular_subtracao(num1, num2):
    num1 = float(num1)
    num2 = float(num2)
    subtracao = num1 - num2
    return subtracao

#Função para calcular a multiplicação:
def calcular_multiplicação(num1, num2):
    num1 = float(num1)
    num2 = float(num2)
    multiplicacao = num1 * num2
    return multiplicacao

#Função para calcular a divisão:
def calcular_divisao(num1, num2):
    num1 = float(num1)
    num2 = float(num2)
    if num2 != 0:
        divisao = num1 / num2
        return divisao    
    else:
        return "Não é possível dividir por 0"

#Solicitando os dois números ao usuário:
numero1 = input("Digite o primeiro número: ")
numero2 = input("Digite o segundo número: ")

#Imprindo resultado:
print(f"A soma de {numero1} + {numero2} é igual a:", calcular_soma(numero1, numero2))
print(f"A subtração de {numero1} - {numero2} é igual a:", calcular_subtracao(numero1, numero2))
print(f"A multiplicação de {numero1} * {numero2} é igual a:", calcular_multiplicação(numero1, numero2))
print(f"A divisão de {numero1} / {numero2} é igual a:", calcular_divisao(numero1, numero2))
