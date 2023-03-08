def soma():
    num1 = float(input("Digite o número 1: "))
    num2 = float(input("Digite o número 2: "))
    print(f"A soma dos números {num1} + {num2} é igual a:", num1 + num2)

def subtracao():
    num1 = float(input("Digite o número 1: "))
    num2 = float(input("Digite o número 2: "))
    print(f"A subtração dos números {num1} - {num2} é igual a:", num1 - num2)

def multiplicacao():
    num1 = float(input("Digite o número 1: "))
    num2 = float(input("Digite o número 2: "))
    print(f"A multiplicação dos números {num1} * {num2} é igual a:", num1 * num2)

def divisao():
    num1 = float(input("Digite o número 1: "))
    num2 = float(input("Digite o número 2: "))
    if num2 == 0:
        print("Não é possível dividir por 0.")
    else:
        print(f"A divisão dos números {num1} / {num2} é igual a:", num1 / num2)

opcao = 1
print("0. Sair \n1. Somar \n2. Subtrair \n3. Multiplicação \n4. Divisão")

while opcao:
    opcao = int(input("Selecione uma opção: "))
    if opcao > 4 or opcao < 0:
        print("Opção inválida!")

    if opcao == 1:
        soma()
    if opcao == 2:
        subtracao()
    if opcao == 3:
        multiplicacao()
    if opcao == 4:
        divisao()