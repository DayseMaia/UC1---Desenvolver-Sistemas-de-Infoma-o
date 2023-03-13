#4. Escreva um programa que solicite ao usuário a idade e o sexo de uma pessoa e imprima uma mensagem 
# personalizada com base nas seguintes condições:
# Se a pessoa for do sexo feminino e tiver menos de 25 anos, imprima "Você é uma jovem mulher".
# Se a pessoa for do sexo feminino e tiver 25 anos ou mais, imprima "Você é uma mulher adulta".
# Se a pessoa for do sexo masculino e tiver menos de 25 anos, imprima "Você é um jovem homem".
# Se a pessoa for do sexo masculino e tiver 25 anos ou mais, imprima "Você é um homem adulto".

idade = input("Insira sua idade: ")
sexo = input("Insira seu sexo: \nM - Masculino \nF - Feminino \n")

if idade and sexo:
    idade = int(idade)
    if sexo == "F" and idade < 25:
        print("Você é uma jovem mulher.")
    elif sexo == "F" and idade >= 25:
        print("Você é uma mulher adulta.")
    elif sexo == "M" and idade < 25:
        print("Você é um jovem homem.")
    elif sexo == "M" and idade >= 25:
        print("Você é um homem adulto.")
    else:
        print("Valor inválido!")
else:
    print("Valor inválido!")