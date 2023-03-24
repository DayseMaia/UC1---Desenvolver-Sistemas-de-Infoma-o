class Triangulo:
    def __init__(self, ladoA, ladoB, ladoC):
        self.ladoA = ladoA
        self.ladoB = ladoB
        self.ladoC = ladoC

    def maior_lado(self):
        maior = max(self.ladoA, self.ladoB, self.ladoC)
        return maior
    
    def calcular_perimetro(self):
        perimetro = (self.ladoA + self.ladoB + self.ladoC)
        return perimetro
    
lado1 = float(input("Insira o valor do lado A: "))
lado2 = float(input("Insira o valor do lado B: "))
lado3 = float(input("Insira o valor do lado C: "))

triangulo1 = Triangulo(lado1, lado2, lado3)

print("Maior lado:", triangulo1.maior_lado())
print("Perímetro:", triangulo1.calcular_perimetro())