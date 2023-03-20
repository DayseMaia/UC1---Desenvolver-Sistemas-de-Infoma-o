# Q.1 Construa um algoritmo para ler um número inteiro, positivo de três dígitos, e gerar outro número formado pelos dígitos 
# invertidos do número lido. 
#  Ex: 
# NumeroLido = 123 
# NumeroGerado = 321 
# Dica: Observe os resultados das funções Quociente e Resto de um número por 10.

def reverso(numero1, numero2, numero3):
    inverte = str(numero1, numero2, numero3)
    return inverte

num1 = input("Digite um número inteiro: ")
num2 = input("Digite o segundo número inteiro: ")
num3 = input("Digite o terceiro número inteiro: ")

print("Número invertido:", reverso(num1, num2, num3[::-1]))
