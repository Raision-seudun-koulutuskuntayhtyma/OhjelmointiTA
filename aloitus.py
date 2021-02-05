def ympyran_ala(halkaisija):
    """Funtio laskee ympyrän pinta-alan halkaisijan perusteella

    Args:
        halkaisija (float): ympyrän halkaisija

    Returns:
        float: ympyrän pinta-ala
    """
    sade = halkaisija / 2
    pinta_ala = sade ** 2 * 3.14159
    joku = 22
    return pinta_ala


kayttaja = 'Markku'
kaupungit = ['Raisio', 'Turku', 'Lieto', 'Kaarina']
print('Metrisen ympyrän halkaisija on', ympyran_ala(1))
