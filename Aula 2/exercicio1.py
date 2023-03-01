#Faça um algorítimo que leia os valores A, B, C e imprima na tela se a soma de A + B é menor que C.
A = int(input("Insira o primeiro número: "))
B = int(input("Insira o segundo número: "))
C = int(input("Insira o terceiro número: "))

resultado = A+B

if resultado < C:
    print(f"A soma de {A} + {B} é igual a: {resultado}, logo é menor que {C}.")
else:
    print(f"A soma de {A} + {B} é igual a: {resultado}, logo é maior ou igual a {C}")