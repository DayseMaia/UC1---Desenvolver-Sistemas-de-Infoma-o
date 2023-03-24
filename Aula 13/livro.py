class Livro:
    def __init__(self, nome, qtd_paginas, autor, preco):
        self.nome = nome
        self.qtd_paginas = qtd_paginas
        self.autor = autor
        self.preco = preco

    def get_preco(self):
        return self.preco
    
    def set_preco(self, novo_preco):
        self.preco = novo_preco

livro1 = Livro("Senhor dos anéis", "999", "Tolkion", 30)

print(livro1.preco)