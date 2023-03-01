#1. Escreva um programa Python para calcular o comprimento de uma string.
def Questao1():

    palavra = input("Digite uma palavra: ")
    print("O comprimento da string é de:", len(palavra))


#2. Escreva um programa em Python para somar todos os itens de uma lista.
def Questao2():

    #Modo 1:
    lista_numeros = [10, 20, 30, 40, 50]
    soma_lista = 0

    for numero in lista_numeros:
        soma_lista += numero

    print("A soma dos itens da lista é igual a:", soma_lista)

    #Modo 2:
    lista_numeros = [10, 20, 30, 40, 50]

    print("A soma dos itens da lista é igual a:", sum(lista_numeros))


#3. Escreva um programa em Python para multiplicar todos os itens de uma lista.
def Questao3():

    lista_numeros = [10, 20, 30, 40, 50]
    mult_lista = 1

    for numero in lista_numeros:
        mult_lista *= numero

    print("A multiplicação dos itens da lista é igual a:", mult_lista)


#4. Escreva um programa em Python para obter o maior número de uma lista.
def Questao4():

    #Modo 1: 
    lista_numeros = [10, 20, 30, 40, 50]
    maximo = lista_numeros[0]

    for i in lista_numeros:
        if i > maximo:
            maximo = i
        
    print("O maior número da lista é:", maximo)

    #Modo 2: 
    lista_numeros = [10, 20, 30, 40, 50]

    print("O maior número da lista é:", max(lista_numeros))


#5. Escreva um programa Python para obter o menor número de uma lista.
def Questao5():

    #Modo 1: 
    lista_numeros = [10, 20, 30, 40, 50]
    minimo = lista_numeros[0]

    for i in lista_numeros:
        if i < minimo:
            minimo = i
            
    print("O menor número da lista é:", minimo)

    #Modo 2: 
    lista_numeros = [10, 20, 30, 40, 50]

    print("O menor número da lista é:", min(lista_numeros))


#2. Escreva um programa em Python para converter temperaturas de e para Celsius e Fahrenheit.
#Saída esperada: 60°C é 140 em Fahrenheit 45°F é 7 em Celsius

def Questao6():

    #Fahrenheit para Celsius:
    temperatura_f = float(input('Informe a temperatura em Fahrenheit: '))
    temperatura_c = (5/9) * (temperatura_f - 32)
    print('A temperatura é:', temperatura_c, '°C')

    #Celsius para Fahrenheit:
    temperatura_c = float(input('Informe a temperatura em Celsius: '))
    temperatura_f = 9/5 * temperatura_c + 32
    print('A temperatura é:', temperatura_f, '°F')


#5. Escreva um programa Python que aceite uma palavra do usuário e a inverta.

def Questao7():

    palavra = input("Digite uma palavra: ")
    print("Palavra invertida:", palavra[::-1])

    palavraInvertida = ""

    for i in range(len(palavra)):
        palavraInvertida = palavraInvertida + palavra[len(palavra)-1-i]
        print(palavraInvertida)


#34. Escreva um programa Python para somar dois inteiros. No entanto, se a soma estiver entre 15 e 20, retornará 20.

def Questao8():
    num1 = int(input("Digite um número inteiro: "))
    num2 = int(input("Digite outro número inteiro: "))

    soma = num1 + num2

    if soma >= 15 and soma <= 20:
        print("O resultado é 20.")
    else:
        print("Resultado é diferente de 20.")


#43. Escreva um programa Python para criar a tabela de multiplicação (de 1 a 10) de um número.
def Questao9():
    tabuada = int(input("Digite um número: "))
    for i in range(1,11):
        print(f"{tabuada} X {i} = {tabuada*i}")
Questao9()