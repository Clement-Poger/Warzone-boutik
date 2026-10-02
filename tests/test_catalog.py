from boutik.catalog import categories, find_product, load_products, search


def test_le_catalogue_contient_10_produits():
    assert len(load_products()) == 10


def test_types_des_champs():
    product = load_products()[0]
    assert isinstance(product["price_ht"], float)
    assert isinstance(product["stock"], int)


def test_trouver_un_produit_par_son_identifiant():
    products = load_products()
    product = find_product(products, 2)
    assert product is not None
    assert product["name"] == "Souris sans fil"


def test_produit_inconnu():
    assert find_product(load_products(), 999) is None


def test_recherche_exacte():
    assert len(search(load_products(), "Hub")) == 1


def test_recherche_sans_tenir_compte_des_majuscules():
    products = load_products()
    assert [p["name"] for p in search(products, "clavier")] == ["Clavier mécanique"]
    assert len(search(products, "SOURIS")) == 2


def test_categories():
    assert categories(load_products()) == ["Accessoires", "Audio", "Périphériques", "Stockage"]
