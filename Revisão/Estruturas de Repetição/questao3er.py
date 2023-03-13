#3. Escreva um programa que solicite ao usuário um número e imprima a tabuada desse número até o valor 10.

tabuada = int(input("Digite um número: "))

for i in range(1,11):
    print(f"{tabuada} X {i} = {tabuada*i}")