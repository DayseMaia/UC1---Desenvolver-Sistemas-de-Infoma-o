#1. Escreva uma função que receba uma lista de números inteiros e retorne o maior número da lista.

def maior_numero(numeros):
    numeros = max(numeros)
    return numeros

lista_numeros = [10, 20, 30, 40, 50]
print("Maior número:", maior_numero(lista_numeros))