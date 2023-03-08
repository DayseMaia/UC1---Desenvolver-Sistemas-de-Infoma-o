# Criar um programa calculadora:
    #Receber dois números e uma operação (+, -, *, /)
    # Dependendo da operação escolhida, passar dois números para uma das funções
    # No final imprime o resultado e a função escolhida

# Criar função para soma
# Criar função para subtração
# Criar função para multiplicação
# Criar função para divisão

operador = input('''Digite o operador: 
+ para adição
- para subtração
* para multiplicação
/ para divisão
''')

numero1 = input("Digite o número 1: ")
numero2 = input("Digite o número 2: ")

numero1 = float(numero1)
numero2 = float(numero2)

def soma(num1, num2):
    total_soma = float(num1 + num2)
    return total_soma

def subtracao(num1, num2):
    total_subtracao = float(num1 - num2)
    return total_subtracao

def multiplicacao(num1, num2):
    total_multiplicacao = float(num1 * num2)
    return total_multiplicacao

def divisao(num1, num2):
    total_divisao = float(num1 / num2)
    return total_divisao

if operador == "+" or "-" or "*" or "/":
    if operador == "+":
        print(f"A soma dos números {numero1} + {numero2} é igual a:", soma(numero1, numero2))
    elif operador == "-":
        print(f"A subtração dos números {numero1} - {numero2} é igual a:", subtracao(numero1, numero2))
    elif operador == "*":
        print(f"A multiplicação dos números {numero1} * {numero2} é igual a:", multiplicacao(numero1, numero2))
    elif operador == "/":
        if numero2 == 0:
            print("Não é possível dividir por 0.")
        else:
            print(f"A divisão dos números {numero1} / {numero2} é igual a:", divisao(numero1, numero2))
else:
    print("Operador inválido!")