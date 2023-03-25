'''Escreva uma função que receba como parâmetro uma string e verifique se a string é um palíndromo (ou seja, pode ser lida da mesma forma de trás para frente). 
Em seguida, utilize uma estrutura de repetição para solicitar ao usuário uma string, chame a função e imprima se a string é um palíndromo ou não.'''

#Função que verifica se a string é um palíndromo:
def palindromo(palavra):
    return palavra == palavra[::-1]

#Solicitando ao usuário uma string:
while True:
    palavra = input("Digite uma palavra (ou 'sair' para terminar): ")
    if palavra == "sair" or palavra == "Sair":
        break
        
    #Chamando a função para verificar se a string digitada pelo usuário é um palíndromo:
    resultado = palindromo(palavra)

    #Imprimindo o resultado:    
    if resultado:
        print(f"A string {palavra} é um palíndromo.")
    else:
        print(f"A string {palavra} não é um palíndromo.")
