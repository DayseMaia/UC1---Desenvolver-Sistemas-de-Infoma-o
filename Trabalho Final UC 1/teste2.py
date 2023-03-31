import random

class Pokemon:
    def __init__(self, nome, tipo, ataque, hp):
        self.nome = nome
        self.tipo = tipo
        self.ataque = ataque
        self.hp = hp
        
    def atacar(self, outro_pokemon):
        dano = self.ataque - outro_pokemon.defender(self)
        outro_pokemon.hp -= dano
        print(f"{self.nome} atacou {outro_pokemon.nome} causando {dano} de dano.")
        if outro_pokemon.hp <= 0:
            print(f"{outro_pokemon.nome} foi derrotado!")
    
    def defender(self, outro_pokemon):
        if self.tipo == "água" and outro_pokemon.tipo == "planta":
            return outro_pokemon.ataque * 0.5
        elif self.tipo == "fogo" and outro_pokemon.tipo == "água":
            return outro_pokemon.ataque * 0.5
        elif self.tipo == "planta" and outro_pokemon.tipo == "fogo":
            return outro_pokemon.ataque * 0.5
        else:
            return 0

class Agua(Pokemon):
    def __init__(self, nome, ataque, hp):
        super().__init__(nome, "água", ataque, hp)

class Fogo(Pokemon):
    def __init__(self, nome, ataque, hp):
        super().__init__(nome, "fogo", ataque, hp)

class Planta(Pokemon):
    def __init__(self, nome, ataque, hp):
        super().__init__(nome, "planta", ataque, hp)

class Treinador:
    def __init__(self, nome):
        self.nome = nome
        self.pokemons = []
        
    def adicionar_pokemon(self, pokemon):
        self.pokemons.append(pokemon)
        print(f"{pokemon.nome} foi adicionado à sua lista de pokemons!")
        
    def listar_pokemons(self):
        print(f"Lista de pokemons de {self.nome}:")
        for pokemon in self.pokemons:
            print(pokemon.nome)

class Jogador(Treinador):
    def escolher_pokemon(self):
        print("Escolha um pokemon para usar na batalha:")
        for i, pokemon in enumerate(self.pokemons):
            print(f"{i + 1}: {pokemon.nome} ({pokemon.tipo}, {pokemon.hp} HP, {pokemon.ataque} de ataque)")
        escolha = int(input("Digite o número do pokemon: "))
        return self.pokemons[escolha - 1]

class Inimigo(Treinador):
    def escolher_pokemon(self):
        return random.choice(self.pokemons)

def batalha(jogador, inimigo):
    print(f"{jogador.nome} escolha seu pokemon para a batalha:")
    pokemon_jogador = jogador.escolher_pokemon()
    pokemon_inimigo = inimigo.escolher_pokemon()
    print(f"{inimigo.nome} escolheu {pokemon_inimigo.nome} ({pokemon_inimigo.tipo}, {pokemon_inimigo.hp} HP, {pokemon_inimigo.ataque} de ataque) para a batalha!")
    while pokemon_jogador.hp > 0 and pokemon_inimigo.hp > 0:
        pokemon_jogador.atacar(pokemon_inimigo)
        if pokemon_inimigo.hp > 0:
            pokemon_inimigo.atacar(pokemon_jogador)
        print(f"{pokemon_jogador.nome} ({pokemon_jogador.tipo}, {pokemon_jogador.hp} HP) vs {pokemon_inimigo.nome} ({pokemon_inimigo.tipo}, {pokemon_inimigo.hp} HP)")
    if pokemon_jogador.hp > 0:
        print(f"{jogador.nome}, parabéns! Você venceu a batalha!")
    elif pokemon_inimigo.hp > 0:
        print(f"{inimigo.nome} venceu a batalha. Tente novamente!")
    else:
        print("A batalha terminou em empate!")

#Este método recebe como parâmetros um objeto da classe Jogador e um objeto da classe Inimigo. Durante a batalha, o jogador escolhe um dos seus pokemons para lutar e o inimigo escolhe um de forma aleatória. Em seguida, os dois pokemons lutam em turno, até que um deles tenha o HP reduzido a zero. Se o pokemon do jogador vencer a batalha, a mensagem "parabéns! Você venceu a batalha!" é exibida. Se o pokemon do inimigo vencer, a mensagem "venceu a batalha. Tente novamente!" é exibida. Caso a batalha termine em empate, a mensagem "A batalha terminou em empate!" é exibida.
def capturar_pokemon(jogador, pokemon):
    jogador.pokemons.append(pokemon)
    print(f"{pokemon.nome} foi capturado!")

def listar_pokemon(jogador):
    print("Seus Pokemons:")
    for i, pokemon in enumerate(jogador.pokemons):
        print(f"{i+1}: {pokemon.nome} ({pokemon.tipo})")

def main():
    pokemons = [
        Agua("Squirtle", 5, 30),
        Fogo("Charmander", 7, 25),
        Planta("Bulbasaur", 4, 35),
        Agua("Magikarp", 1, 10),
        Fogo("Vulpix", 6, 20),       
        Planta("Oddish", 3, 15)
    ]
    jogador = Jogador("Jogador")
    jogador.pokemons = pokemons
    inimigo = Inimigo("Inimigo")
    inimigo.pokemons = pokemons
    while True:
        print("1: Lista Pokemóns")
        print("2: Batalha")
        print("3: Sair")
        opcao = int(input())
        if opcao == 1:
            listar_pokemon(jogador)
        elif opcao == 2:
            pokemon_capturado = batalha(jogador, inimigo)
            if pokemon_capturado:
                capturar_pokemon(jogador, pokemon_capturado)
        elif opcao == 3:
            break

if __name__ == "__main__":
    main()
