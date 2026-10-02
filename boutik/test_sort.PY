from boutik.catalog import load_products, sort_by_price




def test_tri_croissant():
    assert sort_by_price(load_products())[0]["name"] == "Clé USB 64 Go"



def test_tri_decroissant():
    assert sort_by_price(load_products(), descending=True)[0]["name"] == "Disque SSD 1To"



def test_la_liste_d_origine_ne_change_pas():
    products = load_products()
    sort_by_price(products)
    assert products[0]["name"] == "Clavier mécanique"