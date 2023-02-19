class Filme:

    def __init__(self, nome, ano, duracao):
        self.__nome = nome.title()
        self.ano = ano
        self.duracao = duracao
        self.likes = 0

    @property
    def likes(self):
        return self.likes

    @property
    def nome(self):
        return self.__nome

    @nome.setter
    def nome(self, novo_nome):
        self.nome = novo_nome.title

    def darlike(self):
        return self.__Likes += 1

