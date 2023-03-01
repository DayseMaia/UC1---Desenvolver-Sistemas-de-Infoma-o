#5.Receba dois números inteiros correspondentes à largura e altura. Devolva uma
#cadeia de caracteres # que representa um retângulo com as medidas fornecidas.

altura = int(input("Escreva a altura do retângulo: "))
largura = int(input("Escreva a largura do retângulo: "))

linha = ""
for i in range(largura):
    linha = linha + "#"

retangulo = ""
for i in range(largura):
    retangulo = retangulo + "\n" + linha

print(retangulo)