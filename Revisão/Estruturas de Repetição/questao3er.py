#3. Escreva um programa que solicite ao usuário um número e imprima a tabuada desse número até o valor 10.

#Solicitando ao usuário um número:
tabuada = int(input("Digite um número: "))

#Gerando uma lista de 1 a 10 para calcular com o valor digitado pelo usuário e imprimindo os resultados:
for i in range(1,11):
    print(f"{tabuada} X {i} = {tabuada*i}")
