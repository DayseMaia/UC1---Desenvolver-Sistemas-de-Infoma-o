'''1. Escreva um programa que leia uma lista de números inteiros e imprima o maior e o menor número da lista.'''

#Criando uma lista vazia e solicitando ao usuário o tamanho da lista:
lista_numeros = []
qtd_numeros = int(input("Quantos números deseja na lista? "))

#Adicionado os números a uma lista de acordo com o tamanho da lista digitado pelo usuário:
for i in range(qtd_numeros):
    numero = int(input("Digite um número inteiro: "))
    lista_numeros.append(numero)

#Calculando o maior e menor número da lista:
maior = max(lista_numeros)
menor = min(lista_numeros)

#Imprimindo resultado:
print("O maior número é:", maior, "\nO menor número é:", menor)
