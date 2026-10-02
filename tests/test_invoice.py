from boutik.invoice import build_invoice, format_price

PRODUCTS = [{"id": 1, "name": "Stylo", "category": "Test", "price_ht": 10.0, "stock": 50}]


def test_format_avec_deux_decimales():
    assert format_price(5) == "5.00 €"
    assert format_price(19.9) == "19.90 €"
    assert format_price(71.63999999999999) == "71.64 €"


def test_la_facture_contient_le_total():
    text = build_invoice({1: 2}, PRODUCTS)
    assert "Stylo x2" in text
    assert "TOTAL TTC" in text
