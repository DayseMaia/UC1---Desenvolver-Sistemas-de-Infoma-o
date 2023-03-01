#5. Escreva um programa Python para obter o menor número de uma lista.

lista = [1, 10, 20, 30, 40, 50]

print(min(lista))

menor = lista[0]

for numero in lista:
    if numero < menor:
        menor = numero

print(menor)