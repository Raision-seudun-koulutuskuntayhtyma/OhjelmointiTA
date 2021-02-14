class Ostolista:
    # Konstruktori eli olionmuodostin
    def __init__(self, numero, kauppa, ostokset):
        self.numero = numero
        self.kauppa = kauppa
        self.ostokset = ostokset

    # Funktio, jolla lasketaan olion ostosten määrä -> metodi
    def nimikkeita(self):
        maara = len(self.ostokset)
        print(maara)
        
# Luodaan ostoslista1-objekti
ostoslista1 = Ostolista(1, 'X-market', ['Maksalaatikkoa', 'Pullaa', 'Keksejä'])

# Kutsutaan ostoslista1:n nimikkeita()-metodia
ostoslista1.nimikkeita()