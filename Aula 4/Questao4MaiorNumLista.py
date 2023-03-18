#4. Escreva um programa em Python para obter o maior número de uma lista.

lista = [1, 10, 20, 30, 40, 50]

print(max(lista))

maior = lista[0]

for numero in lista:
    if numero > maior:
        maior = numero

print(maior)
