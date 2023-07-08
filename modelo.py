class Filme:
    def __init__(self, titulo, ano, duracao):
        self.__titulo = titulo.title()
        self.ano = ano
        self.duracao = duracao
        self.__likes = 0


    @property
    def likes(self):
        return self.__likes


    def dar_likes(self):
        self.__likes += 1


    @property
    def titulo(self):
        return self.__titulo

    @titulo.setter
    def titulo(self, novo_titulo):
        self.__titulo = novo_titulo.title()


class Serie:
    def __init__(self, titulo, ano, temporadas):
        self.__titulo = titulo.title()
        self.ano = ano
        self.temporadas = temporadas
        self.__likes = 0

    @property
    def likes(self):
        return self.__likes

    def dar_like(self):
        self.__likes +=1

    @property
    def titulo(self):
        return self.__titulo

    @titulo.setter
    def titulo(self, novo_titulo):
        self.__titulo = novo_titulo.title()



vigadores = Filme("vigadores - guerra infinita", 2018, 160)

print(vigadores.titulo)

atlanta = Serie("atlanta", 2018, 2)
print(f'Nome: {atlanta.titulo} - Ano: {atlanta.ano} - Temporadas: {atlanta.temporadas}')
