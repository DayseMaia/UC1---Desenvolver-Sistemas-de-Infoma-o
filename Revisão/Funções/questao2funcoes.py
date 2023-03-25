#Escreva uma função que receba uma lista de palavras e retorne uma lista contendo apenas as palavras que começam com a letra "a"

#Funão que recebe uma lista e retorna as palavras que começam com "a":
def letra_a(lista):
    lista_a = []
    for i in lista:
        if i.startswith("a"):
            lista_a.append(i)
    return lista_a

#Criando lista:
lista = ["aceitar", "aprender", "bola", "rede", "alegria"]

#Chamando a lista e imprimindo resultado:
print(letra_a(lista))
