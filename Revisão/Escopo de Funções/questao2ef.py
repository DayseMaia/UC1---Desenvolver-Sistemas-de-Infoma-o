'''2. Escreva um programa que solicite ao usuário um número e imprima se esse número é par ou ímpar. 
Crie uma função para determinar se um número é par e outra função para determinar se um número é ímpar.'''

#Função que verifica se o número é par:
def num_par(numero):
    return numero % 2 == 0

#Função que verifica se o número é ímpar:
def num_impar(numero):
    return numero % 2 == 1

#Solicitando número ao usuário:
numero = int(input("Digite um número: "))

#Verificando e imprimindo se o número é par ou ímpar:
if num_par(numero):
    print(f"O número {numero} é par.")
elif num_impar(numero):
    print(f"O número {numero} é ímpar.")
else:
    print("Número inválido!")
    
