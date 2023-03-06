def intervalo(lista, limite_inf, limite_sup):
    nova_lista = []

    for n in lista:
        if n >= limite_inf and n <= limite_sup:
            nova_lista.append(n)

    return nova_lista
    
lista_inicial = [12,14,15,16,18,20,24,26,28,32,34,38]
lista_inicial.sort()
print("Lista antiga:", lista_inicial)
print("Lista nova:", intervalo(lista_inicial, 13, 26))