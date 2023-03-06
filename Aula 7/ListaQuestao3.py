#Faça um programa, com uma função que necessite de três argumentos, e que forneça a soma desses três argumentos.

def soma (a, b, c):
    total_soma = float(a + b + c)
    return total_soma

a = float(input("Digite o primeiro número: "))
b = float(input("Digite o segundo número: "))
c = float(input("Digite o terceiro número: "))

print(f"A soma de {a} + {b} + {c} é igual a", soma(a, b, c))