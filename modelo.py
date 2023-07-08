class Filme:
    def __init__(self, titulo, ano, duracao):
        self.titulo = titulo
        self.ano = ano
        self.duracao = duracao


class Serie:
    def __init__(self, titulo, ano, temporadas):
        self.titulo = titulo
        self.ano = ano
        self.temporadas = temporadas


vigadores = Filme("vigadores - guerra infinita", 2018, 160)

print(vigadores.titulo)

atlanta = Serie("atlanta", 2018, 2)
print(f'Nome: {atlanta.titulo} - Ano: {atlanta.ano} - Temporadas: {atlanta.temporadas}')
