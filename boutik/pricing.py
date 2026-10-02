"""Prix : TVA, codes promo et frais de livraison."""

TVA = 0.20


def price_ttc(price_ht):
    """Renvoie le prix TTC (toutes taxes comprises) d'un prix HT, arrondi au centime."""
    return round(price_ht * (1 + TVA), 2)


# TODO (mission F1) : ajouter ici PROMO_CODES et la fonction apply_promo(total, code)

PROMO_CODES = {"BIENVENUE10": 10, "ETUDIANT15": 15}

def apply_promo(total, code):
    """Applique un code promo (en %). Code vide ou inconnu : total inchangé."""
    percent = PROMO_CODES.get(code.strip().upper(), 0)
    return round(total * (100 - percent) / 100, 2)


# TODO (mission F2) : ajouter ici la fonction shipping_cost(total)

FREE_SHIPPING_FROM = 50
SHIPPING_PRICE = 4.90

def shipping_cost(total):
    """Livraison offerte dès 50 € d'achat, sinon 4,90 €."""
    if total >= FREE_SHIPPING_FROM:
        return 0.0
    return SHIPPING_PRICE
