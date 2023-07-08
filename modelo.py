class Programa:
    def __init__(self, titulo, ano):
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
        super().__init__(titulo, ano)
        self.duracao = duracao

class Serie(Programa):
    def __init__(self, titulo, ano, temporadas):
        super().__init__(titulo, ano)
        self.temporadas = temporadas




vingadores = Filme("vigadores - guerra infinita", 2018, 160)
vingadores.dar_likes()
print(f'{vingadores.titulo} - {vingadores.duracao} : {vingadores.likes}')
atlanta = Serie("atlanta", 2018, 2)
atlanta.dar_likes()
atlanta.dar_likes()
print(f'{atlanta.titulo} - {atlanta.temporadas} - {atlanta.likes}')

filmes_e_series = [vingadores, atlanta]

for programa in filmes_e_series:
    detalhes = programa.duracao if hasattr(programa, 'duracao') else programa.temporadas
    print(f'{programa.titulo} - {detalhes} D {programa.likes}')
