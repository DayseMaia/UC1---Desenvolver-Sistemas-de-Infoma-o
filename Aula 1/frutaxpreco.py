'''Criar uma lista de compra com as seguintes regras:
• É necessário um total de 5 frutas;

• A primeira fruta deve custar 1,00;
• A segunda fruta deve custar o dobro do valor da primeira;
• A terceira fruta deve custar metade do valor da primeira;
• A quarta fruta deve custar 3 vezes o valor da terceira fruta;
• A quinta fruta deve custar metade do valor da quarta;

• Cada fruta deve possuir uma variável;
• Usar a menor quantidade possível de variáveis;
• Todas as frutas e seus valores devem ser impressos no seguinte
formato:

“A fruta ________ custa ______”'''

Fruta1 = input("Digite o nome da Fruta 1: ")
Fruta2 = input("Digite o nome da Fruta 2: ")
Fruta3 = input("Digite o nome da Fruta 3: ")
Fruta4 = input("Digite o nome da Fruta 4: ")
Fruta5 = input("Digite o nome da Fruta 5: ")

Fruta1Preco = 1
Fruta2Preco = Fruta1Preco*2
Fruta3Preco = Fruta1Preco/2
Fruta4Preco = Fruta3Preco*3
Fruta5Preco = Fruta4Preco/2

print(f"A fruta {Fruta1} custa R$ {Fruta1Preco}")
print(f"A fruta {Fruta2} custa R$ {Fruta2Preco}")
print(f"A fruta {Fruta3} custa R$ {Fruta3Preco}")
print(f"A fruta {Fruta4} custa R$ {Fruta4Preco}")
print(f"A fruta {Fruta5} custa R$ {Fruta5Preco}")
