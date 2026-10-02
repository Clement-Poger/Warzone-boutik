from boutik.pricing import shipping_cost

def test_livraison_payante_sous_50_euros():
    assert shipping_cost(49.99) == 4.90

def test_livraison_offerte_des_50_euros():
    assert shipping_cost(50) == 0
    assert shipping_cost(120) == 0
