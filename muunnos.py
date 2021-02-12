# Luetaan arvo näppäimistöltä (merkkijono)
syntymavuosi_str = input('Minä vuonna olet syntynyt? ')

# Muutetaan kokonaisluvuksi
syntymavuosi = int(syntymavuosi_str)

ika = 2021 - syntymavuosi
print('täytät tänä vuonna', ika, 'vuotta')

luku = 313

# Muunnetaan kokonaisluku merkkijonoksi
numerosarja = str(luku)
print('numerosarjassa', luku,  'on', len(numerosarja), 'numeroa' )

# Muunnetaan kokonaisluku liukuluvuksi 
print(luku, 'on desimaalilukuna', float(luku))

