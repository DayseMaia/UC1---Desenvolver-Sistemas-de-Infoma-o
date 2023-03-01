a = int(input("Insira o primeiro número: "))
b = int(input("Insira o segundo número: "))
c = int(input("Insita o terceiro número: "))

if a > b and a > c:
    print(f"O maior número é: {a}")
elif b > a and b > c:
    print(f"O maior número é: {b}")
elif c > a and c > b:
    print(f"O maior número é: {c}")