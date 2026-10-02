from boutik.catalog import filter_by_category, load_products

def test_filtrer_une_categorie():
    names = [p["name"] for p in filter_by_category(load_products(), "audio")]
    assert names == ["Casque audio", "Écouteurs Bluetooth"]

def test_categorie_inconnue():
    assert filter_by_category(load_products(), "Jardin") == []