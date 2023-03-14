#1. Escreva um programa que leia uma lista de números inteiros e imprima o maior e o menor número da lista.

lista_numeros = []
qtd_numeros = int(input("Quantos números deseja na lista? "))

for i in range(qtd_numeros):
    numero = int(input("Digite um número inteiro: "))
    lista_numeros.append(numero)
    
maior = max(lista_numeros)
menor = min(lista_numeros)

print("O maior número é:", maior, "\nO menor número é:", menor)
