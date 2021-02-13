lintuaanet = {'varis':'raakkuu', 'harakka':'räkättää', 'lokki':'kirkuu'}
lintu = input('Mikä lintu? ')

# Yleistetty versio select-case-rakennetta vastaavasta funktiosta
def select_case(sanakirja, avain, oletus):
    return sanakirja.get(avain, oletus)

print('On kamala kuunnella, kun', lintu, select_case(lintuaanet, lintu, 'pitää pahaa ääntä'), ', eikä saan kunnolla nukuttua')

