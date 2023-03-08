#Faça uma função que informe a quantidade de dígitos de um
#determinado número inteiro informado.

def digitos(n):
    s = str(n)
    return len(s)

numero = input("Digite um número: ")
print(f"O {numero} tem {digitos(numero)} dígitos.")