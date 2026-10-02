from boutik.catalog import load_products
from boutik.stock import low_stock






def test_produits_presque_en_rupture():
    names = [p["name"] for p in low_stock(load_products())]
    assert names == ["Hub USB-C", "Disque SSD 1 To", "Écouteurs Bluetooth", "Support pour laptop"]




def test_seuil_personnalise():
    assert len(low_stock(load_products(), threshold=0)) == 1
