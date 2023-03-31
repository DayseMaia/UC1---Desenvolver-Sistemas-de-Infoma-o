import random

class Pokemon:
    def __init__(self, nome, tipo, ataque, hp):
        self.nome = nome
        self.tipo = tipo
        self.ataque = ataque
        self.hp = hp

class PokemonAgua(Pokemon):
    def __init__(self, nome, ataque, hp):
        super().__init__(nome, "água", ataque, hp)

class PokemonFogo(Pokemon):
    def __init__(self, nome, ataque, hp):
        super().__init__(nome, "fogo", ataque, hp)

class PokemonPlanta(Pokemon):
    def __init__(self, nome, ataque, hp):
        super().__init__(nome, "planta", ataque, hp)

class Treinador:
    def __init__(self):
        self.pokemons = []

class Jogador(Treinador):
    def escolher_pokemon(self):
        print("Escolha seu Pokemon:")
        for i, pokemon in enumerate(self.pokemons):
            print(f"{i+1}: {pokemon.nome} ({pokemon.tipo})")
        escolha = int(input()) - 1
        return self.pokemons[escolha]

class Inimigo(Treinador):
    def escolher_pokemon(self):
        return random.choice(self.pokemons)

def batalhar(jogador, inimigo):
    jogador_pokemon = jogador.escolher_pokemon()
    inimigo_pokemon = inimigo.escolher_pokemon()
    print("="*7, "Batalha iniciada!!!", "="*7)
    print(f"Jogador escolheu {jogador_pokemon.nome} ({jogador_pokemon.tipo})")
    print(f"Inimigo escolheu {inimigo_pokemon.nome} ({inimigo_pokemon.tipo})")
    while jogador_pokemon.hp > 0 and inimigo_pokemon.hp > 0:
        jogador_pokemon.hp -= inimigo_pokemon.ataque
        inimigo_pokemon.hp -= jogador_pokemon.ataque
        print(f"{jogador_pokemon.nome} ({jogador_pokemon.tipo}) Ataque: {jogador_pokemon.ataque} HP: {jogador_pokemon.hp}")
        print(f"{inimigo_pokemon.nome} ({inimigo_pokemon.tipo}) Ataque: {inimigo_pokemon.ataque} HP: {inimigo_pokemon.hp}")
    if jogador_pokemon.hp <= 0:
        print("Jogador perdeu!")
        print("Inimigo ganhou!")
    else:
        print("Jogador ganhou!")
        print("Inimigo perdeu!")
        return inimigo_pokemon

def capturar_pokemon(jogador, pokemon):
    jogador.pokemons.append(pokemon)
    print(f"{pokemon.nome} foi capturado!")

def listar_pokemon(jogador):
    print("Seus Pokemons:")
    for i, pokemon in enumerate(jogador.pokemons):
        print(f"{i+1}: {pokemon.nome} ({pokemon.tipo})")

def main():
    pokemons = [
        PokemonAgua("Squirtle", 5, 30),
        PokemonFogo("Charmander", 7, 25),
        PokemonPlanta("Bulbasaur", 4, 35),
        PokemonAgua("Magikarp", 1, 10),
        PokemonFogo("Vulpix", 6, 40),       
        PokemonPlanta("Oddish", 4, 20)
    ]
    jogador = Jogador()
    jogador.pokemons = pokemons
    inimigo = Inimigo()
    inimigo.pokemons = pokemons

    while True:
        print("="*12, "POKEMÓN", "="*12)
        print("1: Lista de Pokemons")
        print("2: Iniciar batalha")
        print("3: Sair do jogo")
        escolha = input()
        if escolha == "1":
            listar_pokemon(jogador)
        elif escolha == "2":
            pokemon_capturado = batalhar(jogador, inimigo)
            if pokemon_capturado:
                capturar_pokemon(jogador, pokemon_capturado)
        elif escolha == "3":
            break
        else:
            print("Opção inválida!")

if __name__ == "__main__":
    main()
