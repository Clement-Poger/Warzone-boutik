"""Facture : mise en forme du récapitulatif de commande."""

from boutik.cart import cart_total
from boutik.catalog import find_product
from boutik.pricing import price_ttc
from datetime import datetime
from pathlib import Path


def format_price(amount):
    """Met en forme un montant en euros, avec 2 décimales : 5 -> '5.00 €'."""
    return f"{amount:.2f} €"


def build_invoice(cart, products):
    """Renvoie le texte de la facture du panier."""
    lines = ["========== FACTURE BOUTIK =========="]
    for product_id, quantity in cart.items():
        product = find_product(products, product_id)
        amount = price_ttc(product["price_ht"]) * quantity
        lines.append(f"{product['name']} x{quantity} : {format_price(amount)}")
    lines.append(f"TOTAL TTC : {format_price(cart_total(cart, products))}")
    return "\n".join(lines)


def save_invoice(text, folder="invoices"):
    """Enregistre la facture dans un fichier texte et renvoie son chemin."""
    Path(folder).mkdir(exist_ok=True)
    name = datetime.now().strftime("facture_%Y%m%d_%H%M%S.txt")
    path = Path(folder) / name
    path.write_text(text, encoding="utf-8")
    return path
