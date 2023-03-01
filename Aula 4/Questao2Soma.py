#2. Escreva um programa em Python para somar todos os itens de uma lista.

lista = [10, 20, 30, 40, 50]

print(sum(lista))

soma = 0

for i in lista:
    soma += i

print("A soma dos itens da lista é igual a:", soma)