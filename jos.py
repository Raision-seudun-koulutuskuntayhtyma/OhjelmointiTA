# IF-rakenne kun vaihtoehtoja on vähän
elain = input('Mikä on suosikki lemmikkieläimesi? ')

if elain == 'koira':
    print(elain, 'se on ihmisen paras ystävä, älykäs ja uskollinen')
elif elain == 'kissa':
    print(elain, 'se on veikeä ja itsenäinen otus, joka tappaa hiiret')
else:
    print(elain, 'ei ole niin yleinen, kuin koira tai kissa, mutta ihan OK lemmikki sekin')

# Simuloitu SELRCT-rakenne, antaa virheen, jos syötettyä arvoa vastaavaa avainta ei löydy
elainten_aanet = {'koira':'hakkuu', 'kissa':'naukuu', 'lammas':'määkii', 'lehmä':'ammuu'}
kotielain = input('Mikä on suosikkikotieläimesi? ')
print('On hauska kuunnella kun', kotielain, elainten_aanet[kotielain])

# Puuttuvan avaimen ongelman voi ratkaista try-except-rakenteella
try:
  print('On hauska kuunnella kun', kotielain, elainten_aanet[kotielain])
except:
  print('On hauska kuunnella kun', kotielain, 'pitää sille luonteenomaista ääntä')

# Parannettu versio funktiona, jossa käytetään sanakirjan get-metodin oletusarvoa
def hae_aani(kotielain):
    return elainten_aanet.get(kotielain, 'pitää sille luonteenomaista ääntä')

print('On hauska kuunnella kun', hae_aani(kotielain))

# Yleistetty versio select-case-rakennetta vastaavasta funktiosta
def select_case(sanakirja, avain, oletus):
    return sanakirja.get(avain, oletus)

print('On hauska kuunnella kun', select_case(elainten_aanet, kotielain, 'pitää meteliä'))
    

