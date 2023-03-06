def soma_imposto(taxa_imposto, custo):
    imposto = float(taxa_imposto)
    custo_produto = float(custo)
    imposto_venda = custo_produto / imposto
    return imposto_venda

valor_produto = float(input("Insira o valor do produto: "))
taxa_produto = float(input("Digite a taxa do produto: "))

valor_total = valor_produto + soma_imposto(taxa_produto, valor_produto)
print("Valor do produto com imposto R$", valor_total)