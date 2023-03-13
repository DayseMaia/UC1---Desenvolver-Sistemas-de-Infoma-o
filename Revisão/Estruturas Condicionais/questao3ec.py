#3. Escreva um programa que solicite ao usuário a nota de um aluno em uma prova e imprima a mensagem 
# "Aprovado" se a nota for maior ou igual a 7, 
# "Reprovado" se a nota for menor que 5 e 
# "Recuperação" se a nota estiver entre 5 e 7.

nota = input("Insira sua nota: ")

if nota:
    nota = float(nota)
    if nota >= 7:
        print("Aprovado.")
    elif nota < 5:
        print("Reprovado.")
    else:
        print("Recuperação.")
else:
    print("Valor inválido!")