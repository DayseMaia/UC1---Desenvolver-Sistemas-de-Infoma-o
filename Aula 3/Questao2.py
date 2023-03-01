#2.Ler do teclado 10 números e imprima a quantidade de números entre 10 e 50.
numeroIntervalo = 0
for i in range(10):
    numero = float(input("Insira um número: "))
    if numero >= 10 and numero <= 50:
        numeroIntervalo += 1

print(f"Quantidade de números entre 10 e 50: {numeroIntervalo}")