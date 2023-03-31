import random
import time

class Pokemon:                              #Requisito 1: Modelar classe Pokemon
    def __init__(self, nome, tipo, ataque, hp):
        self.nome = nome
        self.tipo = tipo
        self.ataque = ataque
        self.hp = hp
        
    def atacar(self, outro_pokemon):
        dano = self.ataque - outro_pokemon.defender(self)
        outro_pokemon.hp -= dano
        print(f"{self.nome} atacou {outro_pokemon.nome} causando {dano} de dano.")
        print('-'*60)
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

class Agua(Pokemon):                        #Requisito 2: Modelar subclasse de Pokemon
    def __init__(self, nome, ataque, hp):
        super().__init__(nome, "água", ataque, hp)

class Fogo(Pokemon):                        #Requisito 2: Modelar subclasse de Pokemon
    def __init__(self, nome, ataque, hp):
        super().__init__(nome, "fogo", ataque, hp)

class Planta(Pokemon):                      #Requisito 2: Modelar subclasse de Pokemon
    def __init__(self, nome, ataque, hp):
        super().__init__(nome, "planta", ataque, hp)

class Treinador:                            #Requisito 3: Modelar classe Treinador
    def __init__(self, nome):               #Requisito 3: atributo lista de pokemóns na classe Treinador
        self.nome = nome
        self.pokemons = []
        
    def adicionar_pokemon(self, pokemon):
        self.pokemons.append(pokemon)
        print(f"{pokemon.nome} foi adicionado à sua lista de pokemons!")
        
    def listar_pokemons(self):
        print(f"Lista de pokemons de {self.nome}:")
        for pokemon in self.pokemons:
            print(pokemon.nome)

class Jogador(Treinador):                   #Requisito 4: Modelar subclasse de Treinador
    def escolher_pokemon(self):
        print("Escolha um pokemon para usar na batalha:")
        for i, pokemon in enumerate(self.pokemons):
            print(f"{i + 1}: {pokemon.nome} ({pokemon.tipo}, {pokemon.hp} HP, {pokemon.ataque} de ataque)")
        escolha = int(input("Digite o número do pokemon: "))
        return self.pokemons[escolha - 1]

class Inimigo(Treinador):                   #Requisito 4: Modelar subclasse de Treinador
    def escolher_pokemon(self):
        return random.choice(self.pokemons)

def batalha(jogador, inimigo):              #Requisito 5: Criar método de batalha
    print(f"{jogador.nome} escolha seu pokemon para a batalha:")
    pokemon_jogador = jogador.escolher_pokemon()
    pokemon_inimigo = inimigo.escolher_pokemon()
    print(f"{inimigo.nome} escolheu {pokemon_inimigo.nome} ({pokemon_inimigo.tipo}, {pokemon_inimigo.hp} HP, {pokemon_inimigo.ataque} de ataque) para a batalha!")
    while pokemon_jogador.hp > 0 and pokemon_inimigo.hp > 0:
        pokemon_jogador.atacar(pokemon_inimigo)
        if pokemon_inimigo.hp > 0:
            pokemon_inimigo.atacar(pokemon_jogador)
        print(f"{pokemon_jogador.nome} ({pokemon_jogador.tipo}, {pokemon_jogador.hp} HP) vs {pokemon_inimigo.nome} ({pokemon_inimigo.tipo}, {pokemon_inimigo.hp} HP)")
        time.sleep(2)
    if pokemon_jogador.hp > 0:
        print(f"{jogador.nome}, parabéns! Você venceu a batalha!")
    elif pokemon_inimigo.hp > 0:
        print(f"{inimigo.nome} venceu a batalha. Tente novamente!")
    else:
        print("A batalha terminou em empate!")

def capturar_pokemon(jogador, pokemon):     #Requisito 6: Criar método para capturar um novo pokemón
    jogador.pokemons.append(pokemon)
    print(f"{pokemon.nome} foi capturado!")

def listar_pokemon(jogador):                #Requisito 7: Criar método para listar Pokemóns do Jogador
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
        print('''
        POKEMÓN

        1: Lista Pokemóns
        2: Iniciar Batalha
        3: Capturar Pokemón
        0: Sair do Jogo
        ''')
        print("Escolha uma opção: ")
        opcao = int(input())
        if opcao == 1:
            listar_pokemon(jogador)
        elif opcao == 2:
            pokemon_capturado = batalha(jogador, inimigo)
            if pokemon_capturado:
                capturar_pokemon(jogador, pokemon_capturado)
        elif opcao == 0:
            print("Saindo do jogo...")
            print('-'*60)
            time.sleep(1)
            print("Obrigada por jogar!!! Até a próxima!")
            break

if __name__ == "__main__":
    main()