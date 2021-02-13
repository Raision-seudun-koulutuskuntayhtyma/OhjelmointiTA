# Silmukka, johon on sijoitettu erillinen poistumismekanismi ((tyhjä vastaus)
arvattava_nimi = 'Iines'
arvaus =  'x'
arvausten_maara = 0
while arvaus != arvattava_nimi:
    arvaus = input('Arvaa mikä mun nimi on? ').capitalize()
    arvausten_maara += 1
    if arvaus != arvattava_nimi:
        print('Väärin')
    else:
        print('Arvasit oikein')
    
    # Jos vastaus on tyhjä merkkijono, poistutaan silmukasta
    if arvaus == '':
        break
print('Arvasit', arvausten_maara, 'kertaa')

        