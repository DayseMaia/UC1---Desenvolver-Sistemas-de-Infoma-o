#Dicionário
dados_cliente = {
    "Nome": "Renan",
    "Endereço": "Rua Cruzeiro do Sul",
    "Telefone": "982503645"
}

print(dados_cliente["Nome"])
print(dados_cliente)

#Adicionar itens

dados_cliente["Idade"] = 40

print(dados_cliente)

#Remover itens
del dados_cliente["Telefone"]
print(dados_cliente)
print(len(dados_cliente))