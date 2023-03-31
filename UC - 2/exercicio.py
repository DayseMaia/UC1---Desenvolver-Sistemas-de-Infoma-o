import json

def lista_atualizada():

    with open("lista_funcionario.json", "r") as funcionarios_json:
        lista = json.load(funcionarios_json)
    return lista

def ver_funcionarios():
    lista_funcionarios = lista_atualizada()
    print("Lista de funcionários: ")

    for funcionario in lista_funcionarios:

        print(f'Nome: {funcionario["nome"]} | Idade: {funcionario["idade"]} | Cargo: {funcionario["cargo"]}')

def inserir_funcionario():

    funcionario = {}

    print("Cadastrar novo usuário: ")

    nome_funcionario = input("Insira o nome do novo funcionário: ")
    idade_funcionario = input("Insira a idade do novo funcionário: ")
    cargo_funcionario = input("Insira o cargo do novo funcionário: ")

    print("Novo funcionário cadastrado.")

    funcionario["nome"] = nome_funcionario
    funcionario["idade"] = idade_funcionario
    funcionario["cargo"] = cargo_funcionario

    lista_funcionarios = lista_atualizada()
    lista_funcionarios.append(funcionario)

    with open("lista_funcionario.json", "w") as funcionarios_json:
        json.dump(lista_funcionarios, funcionarios_json, indent=2)

while True:

    print('''

    Menu:

    1. Visualizar Funcionários
    2. Cadastrar Novo Funcionário
    3. Remover Funcionário
    0. Sair
    
    ''')

    opcao = input("Escolha uma opção: ")

    match opcao:
        case "1":
            ver_funcionarios()
        case "2":
            inserir_funcionario()
        case "0":
            print("Saindo do Programa...")
            break