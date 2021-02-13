# Kirjasto, jossa on tietojen järkevyystarkistukseen soveltuvia funktioita

# 1. Poistetaan tekstistä ylimääräiset merkit, kuten välilyönnit alusta ja lopusta
# 2. Vaihdetaan vahingossa syötetty desimaalipilkku (,) desimaalipisteeksi (.)
# 3. Määritellään järkevän arvon alaraja (pienin hyväksyttävä arvo)
# 4. Määritellään järkevän arvon yläraja (suurin hyväksyttävä arvo)

def on_jarkeva(syote, alaraja, ylaraja):
    """
    Puhdistaa merkkijonosta ylimääräiset tulostumattomat merkit ja välilyönnit sekä selvittää onko syötetty arvo annettujen rajojen sisällä. Funktio muutta desimaali pilkun desimaalipisteeksi.


    Args:
        syote (string): Näppäimistöltä syötetty arvo
        alarja (float): pienin sallittu arvo
        ylaraja (float): suurin sallittu arvo
    """

    # Poistetaan whitespace merkit merkkijonon alusta
    puhdistettu_syote = syote.lstrip()

    #  Poistetaan whitespace merkit merkkijonon alusta
    puhdistettu_syote = puhdistettu_syote.rstrip()

    # Selvitetään onko merkkijonossa pilkku (,)
    pilkunpaikka = puhdistettu_syote.find(',')

    # Jos pilkku löytyy, korvataan pisteellä
    if pilkunpaikka != -1:
        korjattu_syote = puhdistettu_syote.replace(',', '.')
    else:
      korjattu_syote = puhdistettu_syote

    # Muutetaan korjattu syöte merkkijonosta liukuluvuksi
    try:
        luku = float(korjattu_syote)
    except:
        print('Syötetyssä tiedossa on ylimääräisiä merkkejä, vain numerot sallittu')
        luku = 0
    # Tarkistetaan, ettei syöte ole alarajan alapuolella
    try:
        if luku < alaraja:
            raise Exception('Syöttämäsi arvo on alle sallitun')
    except Exception as virheilmoitus:
        print(virheilmoitus)

    # Tarkistetaan, ettei syöte ole ylärajan yläpuolella
    try:
        if luku > ylaraja:
            raise Exception('Syöttämäsi arvo on yli sallitus')
    except Exception as virheilmoitus:
        print(virheilmoitus)
    
    # Palautetaan luku
    return luku


# Testataan toimintaa
tulos = on_jarkeva('sata', 1, 500)
print(tulos)

# Parannettu versio järkevyystarkistuksesta
'''
Edellisen version ominaisuuksien lisäksi haluamme tarkistaa, että mahdollisen desimaalin
lisäksi syötteessä on vain numeroita. Idea: jaetaan merkkijono pisteestä kahteen osaan ja tarkistetaan että niissä on vain numeroita

Funktio palauttaa luvun lisäksi virhekoodin ja virheilmoituksen. Pääohjelman koodissa voidaan sillon tarkistaa, onko tapahtunut virhe. Jos on kysytään tieto uudelleen
'''

def syote_ok(merkkijono, alaraja, ylaraja):
    """Funktio palauttaa listan, jonka arvoina ovat virhekoodi, virhesanoma ja syöte numeerisessa muodossa

    Args:
        merkkijono (string): Näppäimistöltä syötettu numeerinen arvo merkkijonona
        alaraja (float):  Syötteen pienin sallittu arvo
        ylaraja (float): Syötteen suurin sallittu arvo

    Returns:
        list: [error (int), error_msg (string), arvo (float)]
    """
    