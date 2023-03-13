#2. Escreva um programa que solicite ao usuário um número e imprima se esse número é par ou ímpar. 
#Crie uma função para determinar se um número é par e outra função para determinar se um número é ímpar.

def numero_par(num):
    if num % 2 == 0:
        print("É par")

def numero_impar(num):
    if num % 2 != 0:
        print("É ímpar")

numero = float(input("Digite um número: "))

print