import random

class Pokemon: #1. Modelar classe Pokemon
    def __init__(self, nome, tipo, ataque, defesa, hp):
        self._nome = nome
        self._tipo = tipo
        self._ataque = ataque
        self._defesa = defesa
        self._hp = hp

class PokemonAgua(Pokemon): #2. Subclasse Pokemon
    def __init__(self, nome, tipo, ataque, defesa, hp):
        super().__init__(nome, tipo, ataque, defesa, hp)
        self._tipo = "Água"

class PokemonFogo(Pokemon): #2. Subclasse Pokemon
    def __init__(self, nome, tipo, ataque, defesa, hp):
        super().__init__(nome, tipo, ataque, defesa, hp)
        self._tipo = "Fogo"

class PokemonGrama(Pokemon): #2. Subclasse Pokemon
    def __init__(self, nome, tipo, ataque, defesa, hp):
        super().__init__(nome, tipo, ataque, defesa, hp)
        self._tipo = "Grama"

class PokemonEletrico(Pokemon): #2. Subclasse Pokemon
    def __init__(self, nome, tipo, ataque, defesa, hp):
        super().__init__(nome, tipo, ataque, defesa, hp)
        self._tipo = "Elétrico"

class Treinador: #Modelar classe Treinador
    def __init__(self, nome, lista_pokemons):
        self._nome = nome
        self._lista_pokemons = lista_pokemons

    def escolher_pokemon(self):
        return random.choice(self._lista_pokemons)

class Jogador(Treinador): #Subclasse Jogador
    def __init__(self, nome, lista_pokemons):
        super().__init__(nome, lista_pokemons)

    def capturar_pokemon(self, novo_pokemon):
        self._lista_pokemons.append(novo_pokemon)
        print(f"Você capturou o {novo_pokemon._nome}")

class Inimigo(Treinador): #Subclasse Inimigo
    def __init__(self, nome, lista_pokemons):
        super().__init__(nome, lista_pokemons)


def batalha_pokemon(self):
    pass
