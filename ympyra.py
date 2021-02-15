# Moduli, joka sisältää muuttujia ja funktioita ympyrägeometrian laskutoimituksiin

"""Joukko funktioita ja vakioita, joita voidaan käyttää hyäksi ympyrägeometrian laskutoimistuksissa: 
        keha(halkaisija) -> laskee ympyrän kehän pituuden, 
        pinta_ala(halkaisija) -> laskee ympyrän pinta-alan
"""
# Muuttujat
pii = 3.14159

# Funktioiden määritykset
def keha(halkaisija):
    """Laskee ympyrän kehän pituuden halkaisijan perusteella

    Args:
        halkaisija (float): Ympyrän halkaisija 

    Returns:
        float: Ympyrän kehän pituus
    """
    keha = pii * halkaisija
    return keha

def pinta_ala(halkaisija):
    sade = halkaisija / 2
    ala = pii * sade ** 2
    return ala

def modulin_nimi():
    print('Funktiot on määritelty paikassa', __name__)

 
# Jos tämä tiedosto suoritetaan yksinään (pääohjelmana), eika tuotuna modulina, tulostetaan tietoja funktioista
if __name__ == '__main__':
    print('Tässä tiedostossa on määritelty funktioita, joiden avulla voi tehdä ympyröihin liittyvää laskentaa. \n')

    print('Modulissa on seuraavat muuttujat ja funktiot, kaksoisalaviivalla varusetut ovat sisäisiä toimintoja: \n')
    
    # Kaikki funktiot ja muuttujat, myös sisäänrakennetut
    toiminnot = dir()
    print(toiminnot)
