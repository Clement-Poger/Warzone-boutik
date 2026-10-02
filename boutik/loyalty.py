"""Fidélité : points gagnés à chaque commande."""

def points_for(total):
    """1 point par euro dépensé (arrondi en dessous). points doublés dès 100EUR"""
    points = int(total)
    if total >= 100:
        points = points * 2
    return points
