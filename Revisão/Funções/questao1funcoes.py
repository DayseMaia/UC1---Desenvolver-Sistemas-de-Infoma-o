#1. Escreva uma função que receba uma lista de números inteiros e retorne o maior número da lista.

#Função que retorna o maior número:
def maior_numero(numeros):
    numeros = max(numeros)
    return numeros

#Criando uma lista:
lista_numeros = [10, 20, 30, 40, 50]

#Chamando a função e imprimindo o resultado:
print("Maior número:", maior_numero(lista_numeros))
