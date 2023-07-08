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

    def __str__(self):
        return f'{self._titulo} - {self.ano} - {self._likes}'

class Filme(Programa):
    def __init__(self, titulo, ano, duracao):
        super().__init__(titulo, ano)
        self.duracao = duracao
    def __str__(self):
        return f'{self.titulo} - {self.ano} - {self.duracao} min - {self.likes} Likes'

class Serie(Programa):
    def __init__(self, titulo, ano, temporadas):
        super().__init__(titulo, ano)
        self.temporadas = temporadas

    def __str__(self):
        return f'{self.titulo} - {self.ano} - {self.temporadas} Temporadas - {self.likes} Likes'

class Playlist(list):
    def __init__(self, nome, programas):
        self.nome = nome
        super().__init__(programas)

    def tamanho(self):
        return len(self.programas)




vingadores = Filme("vigadores - guerra infinita", 2018, 160)
vingadores.dar_likes()
# print(f'{vingadores.titulo} - {vingadores.duracao} : {vingadores.likes}')
atlanta = Serie("atlanta", 2018, 2)
atlanta.dar_likes()
atlanta.dar_likes()
# print(f'{atlanta.titulo} - {atlanta.temporadas} - {atlanta.likes}')
tmep = Filme('Todo mundo em pânico', 1999, 100)
demolidor = Serie('Demolidor', 2016, 2)
tmep.dar_likes()
tmep.dar_likes()
tmep.dar_likes()
demolidor.dar_likes()
demolidor.dar_likes()
demolidor.dar_likes()
filmes_e_series = [vingadores, atlanta, demolidor, tmep]

playlist_fim_de_semana = Playlist('fim de semana', filmes_e_series)

for programa in playlist_fim_de_semana:
    print(programa)
