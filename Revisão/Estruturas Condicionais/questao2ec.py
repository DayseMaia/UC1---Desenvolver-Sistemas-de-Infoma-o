'''2. Escreva um programa que leia o nome e a idade de uma pessoa e imprima uma mensagem personalizada com base na idade. 
Se a idade for menor que 18 anos, imprima "Você é menor de idade". Se a idade estiver entre 18 e 65 anos, imprima "Você é adulto". 
Caso contrário, imprima "Você é idoso".'''

#Solicitando nome e idade ao usuário:
nome = input("Digite seu nome: ")
idade = input("Digite sua idade: ")

#Verificando as condições solicitadas e imprimindo o resultado:
if nome and idade:
    idade = int(idade)
    if idade < 18:
        print(f"{nome}, você é menor de idade.")
    elif idade >= 18 and idade <= 65:
        print(f"{nome}, você é adulto.")
    else:
        print("Você é idoso.")
else:
    print("Valor inválido!")
    
