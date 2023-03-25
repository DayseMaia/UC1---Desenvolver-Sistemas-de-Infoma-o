#3. Escreva uma função que receba uma lista de números inteiros e retorne a soma dos números pares da lista.

#Função que retorna a soma dos números pares:
def soma_pares(lista):
    soma = 0
    for numero in lista:
        if numero % 2 == 0:
            soma += numero
    return soma

#Criando uma lista:
lista = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

#Chamando a função e imprimindo o resultado:
print(soma_pares(lista))
