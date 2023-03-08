# Faça uma função que computa a potência ab
# para valores a e b
# (assuma números inteiros) passados por parâmetro (não use o
# operador **).

def potencia(base,expoente):
    resultado = 1
    for numero in range(1,expoente+1):
# base ** expoente = base * base (expoente vezes)
        resultado = resultado * base
    return resultado

a = int(input("Digite a base: "))
b = int(input("Digite a potência: "))
print(potencia(a, b))