#Dado o nome de uma pessoa, retorne o número de letras do nome e a primeira
#letra do nome.
def Questao1():

    nome = input("Digite um nome: ")

    numeroDeLetras = len(nome) - nome.count(" ")
    
    print("Número de letras:", numeroDeLetras)
    print("Primeira letra do nome:", nome[0])



#Dada uma palavra, retorna a palavra invertida
def Questao2():

    palavra = input("Digite uma palavra: ")
    print("Palavra invertida:", palavra[::-1])

    palavraInvertida = ""

    for i in range(len(palavra)):
        palavraInvertida = palavraInvertida + palavra[len(palavra)-1-i]
        print(palavraInvertida)



#Dada uma palavra, retorna os caracteres nas posições ímpares
def Questao3():
    nome = input("Digite um nome: ")

    for i in range(len(nome)):
        if i % 2 == 0:
            print(f"{i+1} {nome[i]}")

