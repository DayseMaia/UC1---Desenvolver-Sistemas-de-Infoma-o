#Escreva uma função que, dado o valor da conta de um restaurante, calcule e exiba a gorjeta
#do garçom, considerando 10% do valor da conta.

def gorjeta_garcom(valor_conta):
    gorjeta = float(valor_conta) * 0.1
    return gorjeta

conta = float(input("Digite o valor da conta: "))

gorjeta_conta = gorjeta_garcom(conta)

total_conta = conta + gorjeta_conta

print("O valor da gorjeta é R$", gorjeta_conta)
print("O valor da conta é R$", total_conta)
