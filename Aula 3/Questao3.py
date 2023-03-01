#3.Ler do teclado uma lista com 5 inteiros e imprimir o menor valor.
for i in range(5):
    numero = int(input("Insira um número inteiro: "))
    
    if i == 0:
        menor = numero
    else:
        if numero < menor:
            menor = numero
print("O menor número digitado foi:", menor)