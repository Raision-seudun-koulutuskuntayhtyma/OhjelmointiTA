# Otetaan Winsound-kirjasto käyttöön, jotta sen funktioita voidaan käyttää
import winsound

# Määritellään varoitus-funktio, jolla ei ole argumentteja eikä palautsarvoa
def varoitus():
    winsound.Beep(2000, 1000) # Windows-koneessa 2 kHz ääni 1000 ms
    print('VARO alieni!') # tulostetaan vakiovaroitus ruudulle
    
# Kutsutaan varoitus-funktiota
varoitus()

# Määritellään varoitus2-funktio jolla on kaksi argumenttia korkeus ja viesti
def varoitus2(korkeus, viesti):
    """Antaa halutun korkuisen äänimerkin ja tulostaa viestin ruudulle

    Args:
        korkeus (float): äänen taajuus Hz
        viesti (string): viestin sisältö
    """
    winsound.Beep(korkeus, 1000)
    print(viesti)

# Kutsutaan varoitus2-funktiota
varoitus2(600, 'UFO styyrpuurissa')

# Määritellään laske_kirjaimet-funktio, joka palauttaa merkkijonon kirjainten määrän
def laske_kirjaimet(merkkijono):
    """Lasketaan merkkijonoon kuuluvien kirjainten määrä ja palautetaan se

    Args:
        merkkijono (string): tutkittava merkkijono

    Returns:
        int: kirjainten lukumäärä
    """
    kirjaimia = len(merkkijono)
    return kirjaimia

# Kutsutaan laske_kirjaimet-funktiota
print(laske_kirjaimet('Äteritsiputeritsipuolilautatsijänkä')) 

# Määritellään Lambda-funktio jakojäännös, huom se on tyypiltään muuttuja
jakojaannos = lambda jaettava, jakaja : jaettava % jakaja

# Käytetään funktiota
print(jakojaannos(7, 3))

# Tyypillinen lambda-funktion määrittely käyttää yhden kirjaimen muuttujanimiä -> vaikealukuinen
x = lambda a, b, c : a * b + c
print(x(3, 5, 1))
