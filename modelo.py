class Programa:
    def __init__(self, titulo, ano, duracao):
        self._titulo = titulo.title()
        self.ano = ano
        self._likes = 0


    @property
    def likes(self):
        return self._likes


    def dar_likes(self):
        self._likes += 1


    @property
    def titulo(self):
        return self._titulo

    @titulo.setter
    def titulo(self, novo_titulo):
        self._titulo = novo_titulo.title()


class Filme(Programa):
    def __init__(self, titulo, ano, duracao):
        self._titulo = titulo.title()
        self.ano = ano
        self.duracao = duracao
        self._likes = 0

class Serie(Programa):
    def __init__(self, titulo, ano, temporadas):
        self._titulo = titulo.title()
        self.ano = ano
        self.temporadas = temporadas
        self._likes = 0




vigadores = Filme("vigadores - guerra infinita", 2018, 160)

print(vigadores.titulo)

atlanta = Serie("atlanta", 2018, 2)
print(f'Nome: {atlanta.titulo} - Ano: {atlanta.ano} - Temporadas: {atlanta.temporadas}')
