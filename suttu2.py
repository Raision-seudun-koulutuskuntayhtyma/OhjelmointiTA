# Toinen suttupaperi
# Toinen kommentti

def bmi(paino, pituus):
    """Lasketaan painoideksi jakamalla pituus painon neliöllä

    Args:
        paino (float): paino kilogrammoina
        pituus (float): pituus metreinä

    Returns:
        float: painoindeksi
    """
    return paino / pituus**2


oma_bmi = bmi(74, 1.71)

print('Hoh-hoijaa taas on lihottu, painoindeksi on', oma_bmi)

try:
    print(x)
except:
    print('Something went wrong')
finally:
    print('The try except is finished')
