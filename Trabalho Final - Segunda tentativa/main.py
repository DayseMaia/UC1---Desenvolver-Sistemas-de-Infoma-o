import random
import time
import sys
sys.path.append(".")
import pokemons                             #Importando lista de pokemons do arquivo pokemons.py

class Pokemon:                              #Requisito 1: Modelar classe Pokemon
    def __init__(self, nome, tipo, ataque, hp):
        self.nome = nome
        self.tipo = tipo
        self.ataque = ataque
        self.hp = hp
        
    def atacar(self, outro_pokemon):        #Método atacar para usar na batalha
        dano = self.ataque - outro_pokemon.defender(self)
        outro_pokemon.hp -= dano
        print(f"{self.nome} atacou {outro_pokemon.nome} causando {dano} de dano.")
        if outro_pokemon.hp <= 0:
            print(f"{outro_pokemon.nome} foi derrotado!")
    
    def defender(self, outro_pokemon):      #Método defender para usar na batalha de acordo com a vantagem de cada tipo do pokemon
        if self.tipo == "planta" and outro_pokemon.tipo == "água":
            return outro_pokemon.ataque * 0.5
        elif self.tipo == "água" and outro_pokemon.tipo == "fogo":
            return outro_pokemon.ataque * 0.5
        elif self.tipo == "fogo" and outro_pokemon.tipo == "planta":
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

def adicionar_pokemon(self, novo_pokemon):  #Método de adicionar pokemon a lista do Jogador após vitória em uma batalha
    self.pokemons.append(novo_pokemon)
    print(f"{novo_pokemon.nome} foi adicionado à sua lista de pokemons!")

class Jogador(Treinador):                   #Requisito 4: Modelar subclasse de Treinador
    def escolher_pokemon(self):             #Método escolher pokemon do Jogador para a batalha
        print("Escolha um pokemon para usar na batalha:")
        print('-'*60)
        for i, pokemon in enumerate(self.pokemons):
            print(f"{i + 1}: {pokemon.nome} ({pokemon.tipo}, {pokemon.hp} HP, {pokemon.ataque} de ataque)")
        escolha = int(input("\nDigite o número do pokemon: "))
        return self.pokemons[escolha - 1]


class Inimigo(Treinador):                   #Requisito 4: Modelar subclasse de Treinador
    def escolher_pokemon(self):             #Método escolher pokemon do Inimigo para a batalha usando random e a lista de pokemons importada.
        return random.choice(pokemons.pokemons_lista)

def batalha(jogador, inimigo):              #Requisito 5: Criar método de batalha
    print(f"{jogador.nome} escolha seu pokemon para a batalha:")
    pokemon_jogador = jogador.escolher_pokemon()
    pokemon_inimigo = inimigo.escolher_pokemon()
    print(f"{jogador.nome} escolheu {pokemon_jogador.nome} ({pokemon_jogador.tipo}, {pokemon_jogador.hp} HP, {pokemon_jogador.ataque} de ataque) para a batalha!")
    print(f"{inimigo.nome} escolheu {pokemon_inimigo.nome} ({pokemon_inimigo.tipo}, {pokemon_inimigo.hp} HP, {pokemon_inimigo.ataque} de ataque) para a batalha!")
    print('-'*60)
    while pokemon_jogador.hp > 0 and pokemon_inimigo.hp > 0:
        pokemon_jogador.atacar(pokemon_inimigo)
        if pokemon_inimigo.hp > 0:
            pokemon_inimigo.atacar(pokemon_jogador)
        print(f"{pokemon_jogador.nome} ({pokemon_jogador.tipo}, {pokemon_jogador.hp} HP) vs {pokemon_inimigo.nome} ({pokemon_inimigo.tipo}, {pokemon_inimigo.hp} HP)")
        time.sleep(3)
    if pokemon_jogador.hp > 0:
        print(f"{jogador.nome}, parabéns! Você venceu a batalha!")
        print(f"{jogador.nome} venceu a batalha e capturou {pokemon_inimigo.nome}!")
        adicionar_pokemon(jogador, pokemon_inimigo)
    elif pokemon_inimigo.hp > 0:
        print(f"{inimigo.nome} venceu a batalha. Tente novamente!")
    else:
        print("A batalha terminou em empate!")

def listar_pokemon(jogador):                #Requisito 7: Criar método para listar Pokemóns do Jogador
    print('-'*60)
    print("- Seus Pokemons:\n")
    for i, pokemon in enumerate(jogador.pokemons):
        print(f"{i+1}: {pokemon.nome} ({pokemon.tipo})")
    print('-'*60)

def capturar_pokemon(self, novo_pokemon):   #Requisito 6: Criar método para capturar um novo pokemón
    novo_pokemon = random.choice(pokemons.pokemons_lista)
    escolha = input(f"Você encontrou o {novo_pokemon.nome}. Deseja capturá-lo? (S/N) ")
    if novo_pokemon in self.pokemons:
        print("Não foi possível capturar o pokemón, a pokebola escorregou...")
    else:
        if escolha.upper() == "S" or escolha == "SIM":
            self.pokemons.append(novo_pokemon)
            print(f"{novo_pokemon.nome} foi capturado!")
        elif escolha.upper() == "N" or escolha == "NAO":
            print(f"{novo_pokemon.nome} não foi capturado!")
        else:
            print(f"{novo_pokemon.nome} escapou!")


def main():                                 #Função para iniciar o jogo
    print("\n----- BEM VINDO AO JOGO POKEMÓN -----")
    pokemons = [
        Agua("Squirtle", 50, 150),
        Fogo("Charmander", 60, 150),
        Planta("Bulbasaur", 40, 200),
    ]

    jogador = Jogador("Jogador")
    jogador.pokemons = pokemons
    inimigo = Inimigo("Inimigo")
    inimigo.pokemons = pokemons
    
    while True:
        print('''

        - MENU -

        1: Lista de Pokemóns
        2: Iniciar Batalha
        3: Capturar Pokemón
        0: Sair do Jogo
        
        ''')
        print("Escolha uma opção: ")
        opcao = input()
        if opcao == "1":
            listar_pokemon(jogador)
        elif opcao == "2":
            batalha(jogador, inimigo)
        elif opcao == "3":
            capturar_pokemon(jogador, inimigo.pokemons)
        elif opcao == "0":
            print("Saindo do jogo...")
            print('-'*60)
            time.sleep(1)
            print("Obrigada por jogar!!! Até a próxima!")
            print('-'*60)
            break
        else:
            print("Opção inválida! Escolha uma opção válida.")

if __name__ == "__main__":
    main()
