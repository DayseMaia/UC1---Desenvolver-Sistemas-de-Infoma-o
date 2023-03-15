# Q.2 Elabore um algoritmo que receba como entrada o valor do saque realizado pelo cliente de um banco e retorne quantas notas de 
# cada valor serão necessárias para atender ao saque com a menor quantidade de notas possível. Serão utilizadas notas de 
# 100, 50, 20, 10, 5, 2 e 1 reais.

numero = int(input("Digite o valor do saque: "))

while numero == "" or numero == 0:
    print("Valor inválido!")
    numero = int(input("Digite o valor do saque: "))

cem = int(numero / 100)
numero = numero - (cem * 100)

cinquenta = int(numero / 50)
numero = numero - (cinquenta * 50)

vinte = int(numero / 20)
numero = numero - (vinte * 20)

dez = int(numero / 10)
numero = numero - (dez * 10)

cinco = int(numero / 5)
numero = numero - (cinco * 5)

dois = int(numero / 2)
numero = numero - (dois * 2)

um = numero

print(f'''Notas R$100,00 = {cem}.\nNotas R$50,00 = {cinquenta}.\nNotas R$20,00 = {vinte}.\nNotas R$10,00 = {dez}.
Notas R$5,00 = {cinco}.\nNotas R$2,00 = {dois}.\nNotas R$1,00 = {um}.''')