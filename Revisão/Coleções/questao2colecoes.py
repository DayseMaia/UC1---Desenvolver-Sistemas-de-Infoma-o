'''2. Escreva um programa que leia uma lista de nomes e crie um dicionário onde a chave é o nome e o valor é o número de vezes que o nome aparece na lista.'''

#Criando uma lista:
lista_nomes = ["A", "aranha", "arranha", "a", "rã", "A", "rã", "arranha", "a", "aranha", "Nem", "a", "aranha", "arranha", "a", "rã", "Nem", "a", "rã", "arranha", "a", "aranha",]

#Criando um dicionário:
contagem_nomes = {}
for nome in lista_nomes:
    if nome in contagem_nomes:
        contagem_nomes[nome] += 1
    else:
        contagem_nomes[nome] = 1
        
#Imprimindo resultado:
print(contagem_nomes)
