#Escreva um programa que solicite ao usuário dois números e imprima a soma, a subtração, a multiplicação e a divisão desses números.
# Crie funções separadas para cada operação matemática.

def calcular_soma(num1, num2):
    num1 = float(num1)
    num2 = float(num2)
    soma = num1 + num2
    return soma

def calcular_subtracao(num1, num2):
    num1 = float(num1)
    num2 = float(num2)
    subtracao = num1 - num2
    return subtracao

def calcular_multiplicação(num1, num2):
    num1 = float(num1)
    num2 = float(num2)
    multiplicacao = num1 * num2
    return multiplicacao

def calcular_divisao(num1, num2):
    num1 = float(num1)
    num2 = float(num2)
    divisao = num1 / num2
    return divisao

numero1 = input("Digite o primeiro número: ")
numero2 = input("Digite o segundo número: ")

print(f"A soma de {numero1} + {numero2} é igual a:", calcular_soma(numero1, numero2))
print(f"A subtração de {numero1} - {numero2} é igual a:", calcular_subtracao(numero1, numero2))
print(f"A multiplicação de {numero1} * {numero2} é igual a:", calcular_multiplicação(numero1, numero2))
print(f"A divisão de {numero1} / {numero2} é igual a:", calcular_divisao(numero1, numero2))