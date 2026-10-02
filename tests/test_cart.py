from boutik.cart import add_to_cart, cart_count, cart_total, remove_from_cart
from boutik.pricing import price_ttc

PRODUCTS = [
    {"id": 1, "name": "Stylo", "category": "Test", "price_ht": 10.0, "stock": 50},
    {"id": 2, "name": "Cahier", "category": "Test", "price_ht": 5.0, "stock": 50},
]


def test_ajouter_un_produit():
    cart = {}
    add_to_cart(cart, 1, 2)
    assert cart == {1: 2}


def test_ajouter_deux_fois_le_meme_produit():
    cart = {}
    add_to_cart(cart, 1, 1)
    add_to_cart(cart, 1, 2)
    assert cart == {1: 3}


def test_retirer_un_produit():
    cart = {1: 2, 2: 1}
    remove_from_cart(cart, 1)
    assert cart == {2: 1}


def test_nombre_d_articles():
    assert cart_count({1: 2, 2: 3}) == 5


def test_total_du_panier():
    cart = {1: 2, 2: 1}
    expected = round(price_ttc(10.0) * 2 + price_ttc(5.0), 2)
    assert cart_total(cart, PRODUCTS) == expected
