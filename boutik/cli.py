"""Interface en ligne de commande de Boutik."""

from boutik import __version__
from boutik import cart as panier
from boutik import catalog, invoice, pricing, stock


def show_products(products, cart):
    """Affiche une liste de produits."""
    for p in products:
        prix = invoice.format_price(pricing.price_ttc(p["price_ht"]))
        print(f"  [{p['id']}] {p['name']} : {prix} (stock : {p['stock']})")
def do_sort(products, cart):
#Affiche le catalogue trié par prix."""
    answer = input("Du moins cher au plus cher ? (o/n) : ").strip().lower()
    show_products(catalog.sort_by_price(products, descending=(answer == "n")), cart)


def do_search(products, cart):
    """Recherche un produit par son nom."""
    text = input("Rechercher : ").strip()
    results = catalog.search(products, text)
    if not results:
        print("Aucun produit trouvé.")
    show_products(results, cart)


def do_add(products, cart):
    """Ajoute un produit au panier."""
    product_id = int(input("Identifiant du produit : "))
    product = catalog.find_product(products, product_id)
    if product is None:
        print("Produit introuvable.")
        return
    quantity = int(input("Quantité : "))
    if not stock.is_available(product, cart.get(product_id, 0) + quantity):
        print("Stock insuffisant.")
        return
    panier.add_to_cart(cart, product_id, quantity)
    print(f"{product['name']} ajouté au panier ({panier.cart_count(cart)} article(s)).")


def do_remove(products, cart):
    """Retire un produit du panier."""
    product_id = int(input("Identifiant du produit à retirer : "))
    panier.remove_from_cart(cart, product_id)
    print("Produit retiré.")


def show_cart(products, cart):
    """Affiche le contenu du panier."""
    if not cart:
        print("Panier vide.")
        return
    print(invoice.build_invoice(cart, products))

def do_alerts(products, cart):
#Affiche les produits presque en rupture de stock.
    for p in stock.low_stock(products):
        print(f" ALERTE : {p['name']}, plus que {p['stock']} en stock")

def checkout(products, cart):
    """Valide la commande : facture, paiement et mise à jour du stock."""
    if not cart:
        print("Panier vide.")
        return
    total = panier.cart_total(cart, products)
    text = invoice.build_invoice(cart, products)
    print(text)

    code = input("Code promo (Entrée si aucun) : ")
    total = pricing.apply_promo(total, code)


    shipping = pricing.shipping_cost(total)
    print(f"Livraison : {invoice.format_price(shipping)}")
    total = round(total + shipping, 2)


    print(f"À PAYER : {invoice.format_price(total)}")

    # [F4] sauvegarde de la facture

    # [F5] points de fidélité

    for product_id, quantity in cart.items():
        stock.reserve(catalog.find_product(products, product_id), quantity)
    cart.clear()
    print("Merci pour votre commande !")


MENU = [
    ("1", "Voir le catalogue", show_products),
    ("2", "Rechercher un produit", do_search),
    ("3", "Ajouter au panier", do_add),
    ("4", "Retirer du panier", do_remove),
    ("5", "Voir le panier", show_cart),
    ("6", "Valider la commande", checkout),
    ("7", "Trier par prix", do_sort),
    ("8", "Alertes de stock", do_alerts)
]


def run():
    """Lance la boutique."""
    products = catalog.load_products()
    cart = {}
    print(f"Bienvenue chez Boutik v{__version__} !")
    while True:
        print()
        for key, label, _ in MENU:
            print(f"  {key}. {label}")
        print("  0. Quitter")
        choice = input("> ").strip()
        if choice == "0":
            print("À bientôt !")
            break
        for key, _, action in MENU:
            if key == choice:
                action(products, cart)
                break
        else:
            print("Choix inconnu.")
