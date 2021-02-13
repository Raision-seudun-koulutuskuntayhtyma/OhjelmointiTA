# Täytetään listaa kunnens käyttäjä syöttää tyhjän arvon
kauppalista = []
while True:
    ostos = input('Mitä pitää tuoda kaupasta? ')
    if ostos == '':
        break
    kauppalista.append(ostos)

print('Ja tuo kaupasta:', kauppalista)

# Luetaan kauppalista FOR-silmukassa, merkinta-muuttuja viittaa listan jäseneen
for merkinta in kauppalista:
    print('Osta', merkinta )

# Kierrosmääräinen FOR-silmukka: lista parillista numeroista välilta 20 - 30
parilliset = []
alku = 20
loppu = 30
askel = 2
for luku in range(alku, loppu, askel):
     parilliset.append(luku)

print('parilliset luvut välitä', alku, '-', loppu, 'ovat', parilliset)
 
# Kaikkia argumentteja ei tarvitse kirjoittaa 
 
for x in range(6): # 1 argumentti loppuarvo, x = 0...6
 print(x)

for x in range(2, 6): # argumenttia alku ja loppuarvo, x = 2...6
 print(x)