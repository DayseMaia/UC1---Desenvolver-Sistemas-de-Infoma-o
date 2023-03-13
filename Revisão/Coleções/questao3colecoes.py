#3. Escreva um programa que leia uma lista de números inteiros e remova todos os valores duplicados. 
#Em seguida, imprima a lista sem os valores duplicados.

lista = [5, 5, 9, 7, 5, 2, 4, 7, 5, 4, 1, 8, 4, 7, 2, 1]

def remover_duplicatas(lista):
    r = []
    r.append(lista[0])
    for i in range(1, len(lista)):
        s = True
        for j in range(len(r)):
            if lista[i] == r[j]:
                s = False
        if s:
            r.append(lista[i])
    return r
print("Lista original:", lista)
print("Lista sem duplicatas:", remover_duplicatas(lista))