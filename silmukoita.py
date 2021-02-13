# 10 kierroksen While laskuri, kierrokset 0-9
laskuri = 0
while laskuri < 10:
    print('nyt on menossa kierros', laskuri)
    laskuri += 1

# Laskurin ehto on täynnä jo ennen silmukkaa, simukkaa ei suoriteta

laskuri = 10
while laskuri < 10:
    print('nyt on menossa kierros', laskuri)
    laskuri += 1

# Silmukka, jota toistetaan kunnes käyttäjä ei enää halua jatkaa
jatketaan = 'K'
while jatketaan == 'K':
    print('hippopotamus')
    jatketaan = input('Paina K, jos haluat jatkaa :').upper()

