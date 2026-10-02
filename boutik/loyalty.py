"""Fidélité : points gagnés à chaque commande"""

def points_for(total):
    """1 point par euro dépensé (arrondi en dessous). Points doublés dès 100$"""
    points = int(total)
    if total >= 100:
        points = points * 2
    return points