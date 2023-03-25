'''Escreva uma função que receba como parâmetro uma lista de números inteiros e retorne o número máximo na lista. 
Em seguida, utilize uma estrutura de repetição para solicitar ao usuário uma lista de números inteiros, chame a função e imprima o resultado. 
Se a lista estiver vazia, a função deve retornar None e o programa deve imprimir uma mensagem informando que a lista está vazia.'''

#Função que retorna o maior número:
def maior_numero(lista):
    if len(lista) == 0:
        return None
    return max(lista)

lista = []

#Solicitando ao usuário os números inteiros e adicionando a lista:
while True:
    numero = input("Digite um número inteiro (ou 'sair' para terminar): ")
    if numero == "sair" or numero == "Sair":
        break
    lista.append(int(numero))

resultado = maior_numero(lista)

#Verificando se a lista é vazia ou não e imprimindo o resultado:
if resultado is None:
    print("Lista vazia.")
else:
    print("O maior número na lista é:", resultado)
