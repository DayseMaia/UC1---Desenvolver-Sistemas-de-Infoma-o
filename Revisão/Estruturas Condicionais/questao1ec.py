#1. Escreva um programa que solicite ao usuário um número e imprima se ele é positivo, negativo ou zero.

numero = input("Digite um numero: ")

if numero:
    numero = float(numero)
    if numero > 0:
        print(f"O número {numero} é positivo.")
    elif numero < 0:
        print(f"O número {numero} é negativo.")
    else:
        print("É zero.")
else:
    print("Valor inválido!")