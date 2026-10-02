from boutik.stock import is_available, reserve


def test_disponible_si_stock_suffisant():
    assert is_available({"name": "A", "stock": 5}, 2)


def test_indisponible_si_stock_insuffisant():
    assert not is_available({"name": "A", "stock": 1}, 2)


def test_on_peut_acheter_le_dernier_exemplaire():
    assert is_available({"name": "A", "stock": 1}, 1)


def test_reserver_diminue_le_stock():
    product = {"name": "A", "stock": 5}
    reserve(product, 2)
    assert product["stock"] == 3


def test_reserver_trop_leve_une_erreur():
    product = {"name": "A", "stock": 1}
    try:
        reserve(product, 3)
    except ValueError:
        return
    raise AssertionError("reserve() aurait dû lever une ValueError")
