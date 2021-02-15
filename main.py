# TÄMÄ ON PÄÄOHJELMA

# Kirjastojen ja modulien lataukset

# Ladataa moduli ympyra.py ja annetaan nimiavaruudelle alias ymp
import ympyra as ymp

# Kysytään käyttäjältä ympyrän halkaisija
halkaisija = float(input('Syötä ympyrän halkaisija metreinä: '))

# Käytetään tuodun modulin pinta_ala-funktiota
pinta_ala = ymp.pinta_ala(halkaisija)

# Tuostetaan tulokset ruudulle
print('Halkaisijaltaan', halkaisija, 'metrisen ympyrän pinta-ala on ', pinta_ala, 'neliömetriä')

# Selvitetään modulin keskeiset attribuutit
print('Modulin nimi __name__ on', ymp.__name__)
print('Tiedoston nimi __file__ on', ymp.__file__)
print('Paketti __package__ on', ymp.__package__)
print('Dokumentaatio __doc__-attribuutissa on:', ymp.__doc__)
ymp.ke