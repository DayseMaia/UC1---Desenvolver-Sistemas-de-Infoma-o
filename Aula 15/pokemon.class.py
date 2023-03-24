'''Utilize o conceito de herança para criar a
Classe Pokemon e as subclasses de tipo
de Pokemon

ex: PokemonAquatico, PokemonFogo,
PokemonEletrico'''

'''Utilize o conceito de polimorfismo para
criar um método checarVantagem na
Classe Pokemon e modifique esse método
nas subclasses de acordo com as
vantagens e desvantagens daquele tipo.'''

class Pokemon:
    def __init__(self, nome, nivel):
        self._nome = nome
        self._nivel = nivel
        self._hp = nivel * 5

    def informacoes(self):
            return self._nome, self._nivel, self._tipo

    def checar_vantagem(self, vantagem):
        return vantagem
    
class PokemonAgua(Pokemon):
    def __init__(self, nome, nivel):
        super().__init__(nome, nivel)
        self._tipo = "Água"

    def informacoes(self):
        return super().informacoes()
    
    def checar_vantagem(self):
        print("Água tem vantagem contra Fogo.")
        print("Água tem desvantagem contra Planta.")

class PokemonFogo(Pokemon):
    def __init__(self, nome, nivel):
        super().__init__(nome, nivel)
        self._tipo = "Fogo"

    def informacoes(self):
        return super().informacoes()

    def checar_vantagem(self):
        print("Fogo tem vantagem contra Planta.")
        print("Fogo tem desvantagem contra Água.")
    
class PokemonElerico(Pokemon):
    def __init__(self, nome, nivel):
        super().__init__(nome, nivel)
        self._tipo = "Elétrico"

    def informacoes(self):
        return super().informacoes()
    
    def checar_vantagem(self):
        print("Elétrico tem vantagem contra Água.")
        print("Elétrico tem desvantagem contra Fogo.")

if __name__ == "__main__":
    squirtle = PokemonAgua("Squirtle", 2)
    chamander = PokemonFogo("Chamander", 3)
    pikachu = PokemonElerico("Pikachu", 5)

    print(squirtle.informacoes())
    print(chamander.informacoes())
    print(pikachu.informacoes())
    print("-" * 33)
    squirtle.checar_vantagem()
    print("-" * 33)
    chamander.checar_vantagem()
    print("-" * 33)
    pikachu.checar_vantagem()
