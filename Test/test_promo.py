from boutik.pricing import apply_promo

def test_code_bienvenue():
    assert apply_promo(100, "BIENVENUE10") == 90.0

def test_code_en_minuscules():
    assert apply_promo(100, "etudiant15") == 85.0

def test_code_inconnu_ou_vide():
    assert apply_promo(100, "FAUXCODE") == 100
    assert apply_promo(100, "") == 100