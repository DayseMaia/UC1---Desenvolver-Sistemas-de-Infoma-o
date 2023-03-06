#Faça um programa, com uma função que necessite de um argumento. A função retorna o valor de caractere ‘P’, se seu argumento for positivo, e ‘N’, se seu argumento for zero ou negativo.
def argumento (numero):
    num = float(numero)
    if num >= 0:
        print("P")
    else:
        print("N")
    return num

num_informado = float(input("Digite um número: "))
print(argumento(num_informado))