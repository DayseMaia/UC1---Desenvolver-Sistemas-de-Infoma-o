#Lista
programadores = ["Victor", "Juliana", "Samuel", "Caio", "Luana"]
print(type(programadores))
print(len(programadores))
print(programadores[4])

aluno = ["Murilo", 19, 1.79]
print(type(aluno))
print(len(aluno))
print(aluno[1])

lugares = ["Brasil", "Itália", "França"]
print(len(lugares))
print(lugares)
lugares.append("Uruguai")
print(lugares)

programadores = ["Victor", "Juliana", "Samuel", "Caio", "Luana"]

nome = input("Digite um nome: ")

if nome in programadores:
    print(nome, "está na lista.")
else:
    print(nome, "não está na lista.")