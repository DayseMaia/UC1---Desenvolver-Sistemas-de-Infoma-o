nome = input("Digite seu nome: ")
nota1 = float(input("Digite sua primeira nota: "))
nota2 = float(input("Digite sua segunda nota: "))
nota3 = float(input("Digite sua terceira nota: "))

media = (nota1 + nota2 + nota3)/3

if media >= 7:
    print(f"{nome} está aprovado com média: {media}")
elif media <= 5:
    print(f"{nome} está reprovado com média: {media}")
elif media >= 5.1 and <= 6.9:
    print(f"{nome} está de recuperação com média: {media}")
