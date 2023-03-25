'''Escreva uma função que receba como parâmetro uma lista de números inteiros e retorne a soma dos números pares na lista. 
Em seguida, utilize um laço de repetição para solicitar ao usuário uma lista de números inteiros, chame a função e imprima o resultado.'''

#Função que retorna a soma dos números pares na lista:
def somar_pares(lista):
    soma = 0
    for num in lista:
        if num % 2 == 0:
            soma += num
    return soma

lista = []

#Solicitando ao usuário os números inteiros:
while True:
    numero = input("Digite um número inteiro (ou 'sair' para terminar): ")
    if numero == "sair" or numero == "Sair":
        break
    lista.append(int(numero))
    
#Imprimindo o resultado com a função:
print(f"A soma dos números pares é: {somar_pares(lista)}")
