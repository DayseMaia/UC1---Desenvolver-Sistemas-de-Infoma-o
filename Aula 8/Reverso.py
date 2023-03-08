#Faça uma função que retorne o reverso de um número inteiro
#informado. Por exemplo: 127 -> 721.

def reverso(n):
    inverte = str(n)
    return inverte

invertido = input("Digite um número inteiro: ")
print("Número invertido:", reverso(invertido[::-1]))