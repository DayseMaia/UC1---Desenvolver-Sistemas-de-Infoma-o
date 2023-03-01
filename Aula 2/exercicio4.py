A = int(input("Insira um número inteiro: "))
B = int(input("Insira o segundo número inteiro: "))
C = int(input("Insira o terceiro número inteiro: "))

primeiro = A
segundo = B
terceiro = C

if A == B or A == C:
    print("Eles são iguais.")
elif (A>=B and A>=C):
    primeiro = A
    if (B>=C):
        segundo = B
        terceiro = C
    else:
        segundo = C
        terceiro = B

valores = [30,50,20]
valores.sort(reverse=True)
print(valores)