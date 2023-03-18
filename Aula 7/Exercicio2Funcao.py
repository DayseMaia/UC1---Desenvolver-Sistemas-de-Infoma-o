#Crie uma função que permita contar o número de vezes que aparece uma letra em uma
#string.

def contar_letra(palavra, letra):
    contador = 0

    for l in palavra:
        if l == letra:
            contador += 1

    return contador

pal = input("Digite uma palavra: ")
let = input("Digite uma letra: ")

contagem = contar_letra(pal, let)
#Modo 2:
contagem2 = pal.count(let)

print(f"A letra {let} aparece {contagem} vezes na palavra {pal}")
#Modo 2:
print(contagem2)
