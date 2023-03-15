class Pokemon:
    def __init__(self, nome, tipo, nivel):
        self.nome = nome
        self.tipo = tipo
        self.nivel = nivel

    def batalha(self, adversario):
        if self.nivel > adversario.nivel:
            print(f"{self.nome} ganhou a batalha.")
        elif self.nivel < adversario.nivel:
            print(f"{adversario.nome} ganhou a batalha.")
        else:
            print("Empate.")

pokemon1 = Pokemon("Pikachu", "Elétrico", 50)
pokemon2 = Pokemon("Squirtle", "Água", 50)

print(pokemon1.nome, pokemon1.tipo, pokemon1.nivel)
print(pokemon2.nome, pokemon2.tipo, pokemon2.nivel)

pokemon1.batalha(pokemon2)