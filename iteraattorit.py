# Luodaan ostoslista
ostoslista = ('maitoa', 'voita', 'juustoa', 'kahvia')

# Määritellään iteraattori iter-funktion avulla
ostoslista_iteraattori = iter(ostoslista)

# Tulostetaan listan 3 ensimmäistä alkiota next-funktion avulla
print('osta ensin', next(ostoslista_iteraattori)) # maitoa
print('ja sitten', next(ostoslista_iteraattori)) # voita
print('ja sitten', next(ostoslista_iteraattori)) # juustoa

# Merkkijonot ovat myös iteroitavissa
elain = 'hippopotamus'
merkeittain = iter(elain)
print(next(merkeittain)) # h
print(next(merkeittain)) # i
print(next(merkeittain)) # p

class Muistutus:

    # Konstruktori
    def __init__(self, viesti):
        self.viesti = viesti

    # Funktio iteraattorin luomiseksi. Sen avulla seurataan katsomiskertojen määrää, alkaa 1:stä
    def __iter__(self):
        self.luku_kertoja = 1
        return self

    # Funktio katsomiskertojen määrän kasvattamiseen, kasvaa 1:llä
    def __next__(self):
        katsottu = self.luku_kertoja
        self.luku_kertoja += 1
        return katsottu

# Luodaan olio
muistutus1 = Muistutus('Käy kaupassa')
iteraattori1 = iter(muistutus1)

# Tulostetaan muistutus kahdesti
print('Katsottu', next(iteraattori1), 'kertaa ja viesti on:', muistutus1.viesti)
print('Katsottu', next(iteraattori1), 'kertaa ja viesti on:', muistutus1.viesti)

print('muistutus1-olion luku_kertoja-ominaisuus on', muistutus1.luku_kertoja)