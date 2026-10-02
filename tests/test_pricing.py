from boutik.pricing import TVA, price_ttc


def test_taux_de_tva():
    assert TVA == 0.20


def test_prix_ttc():
    # 10 € HT + 20 % de TVA = 12 € TTC
    assert price_ttc(10) == 12.0
    assert price_ttc(19.90) == 23.88
