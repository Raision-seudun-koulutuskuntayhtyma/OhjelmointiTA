# PÄÄOHJELMA

# Tuodaan kaikki modulin toiminnot suoraan pääohjelman nimiavaruuteen
import ympyra as *

# Kysytään käyttäjältä ympyrän halkaisija
halkaisija = float(input('Syötä ympyrän halkaisija metreinä: '))

# Käytetään tuodun modulin pinta_ala-funktiota
pinta_ala = pinta_ala(halkaisija)

# Tuostetaan tulokset ruudulle
print('Halkaisijaltaan', halkaisija, 'metrisen ympyrän pinta-ala on ', pinta_ala, 'neliömetriä \n')

print('Laskennassa käytetty piin arvo on', pii)