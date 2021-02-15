# PÄÄOHJELMA

# Otetaan modulista yksittäinen funktio käyttöön
from ympyra import pinta_ala

# Kysytään käyttäjältä ympyrän halkaisija
halkaisija = float(input('Syötä ympyrän halkaisija metreinä: '))

# Käytetään tuodun modulin pinta_ala-funktiota
pinta_ala = pinta_ala(halkaisija)

# Tuostetaan tulokset ruudulle
print('Halkaisijaltaan', halkaisija, 'metrisen ympyrän pinta-ala on ', pinta_ala, 'neliömetriä')

