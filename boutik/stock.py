"""Stock : disponibilité et réservation des produits."""


def is_available(product, quantity):
    """Indique si on peut vendre `quantity` exemplaires de ce produit."""
    return product["stock"] >= quantity


def reserve(product, quantity):
    """Retire `quantity` exemplaires du stock (erreur si le stock est insuffisant)."""
    if not is_available(product, quantity):
        raise ValueError(f"Stock insuffisant pour {product['name']}")
    product["stock"] -= quantity
    

def low_stock(products, threshold=3):
#Renvoie les produits dont le stock est <= au seuil, du plus urgent au moinsurgent.
    low = [p for p in products if p["stock"] <= threshold]
    return sorted(low, key=lambda p: p["stock"])

