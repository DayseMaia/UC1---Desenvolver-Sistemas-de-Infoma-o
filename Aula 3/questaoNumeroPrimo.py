numero = int(input("Digite um número inteiro: "))
contador = 0

for i in range(1, numero + 1):
    if numero % i == 0:
        contador = contador + 1

if contador <= 2:
    print(numero, "é primo.")
else:
    print(numero, "não é primo.")

numero = int(input("Digite um número inteiro: "))

ehPrimo = True

for i in range(2, numero):
    if numero % i == 0:
        ehPrimo = False

if ehPrimo:
    print("É primo.")
else:
    print("Não é primo.")