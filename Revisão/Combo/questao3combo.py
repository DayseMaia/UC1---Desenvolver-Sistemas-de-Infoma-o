'''Escreva uma função que receba como parâmetro uma lista de strings e retorne a quantidade de strings que possuem mais de 5 caracteres. 
Em seguida, utilize uma estrutura condicional para perguntar ao usuário se ele deseja adicionar mais strings à lista, 
e utilize um laço de repetição para solicitar ao usuário as novas strings, chame a função e imprima o resultado.'''

#Função que retorna se a string tem mais de 5 caracteres:
def contar_strings(lista):
    contador = 0
    for string in lista:
        if len(string) > 5:
            contador += 1
    return contador

lista = []

#Solicitando ao usuário as strings e adicionando a uma lista:
while True:
    lista_string = input("Digite uma string (ou 'sair' para terminar: )")
    if lista_string == "sair" or lista_string == "Sair":
        break
    lista.append(lista_string)

resultado = contar_strings(lista)

print(f"A lista têm {resultado} strings com mais de 5 caracteres.")

#Perguntando ao usuário se ele deseja adicionar mais strings na lista:
adicionar = input("Deseja adicionar mais strings? (s/n) ")

while adicionar == "s" or adicionar == "sim":
    entrada = input("Digite uma string: ")
    lista.append(entrada)
    resultado = contar_strings(lista)
    print(f"A lista têm {resultado} strings com mais de 5 caracteres.")
    adicionar = input("Deseja adicionar mais strings? (s/n) ")
