"""
Module de vue pour la saisie des détails des joueurs.

Ce module contient une fonction pour demander à l'utilisateur de saisir les détails d'un nouveau joueur.
"""

import re
from datetime import datetime


def validate_name(name):
    """
    Valide le prénom ou le nom en vérifiant qu'il ne contient que des lettres, des espaces et des tirets.

    Args:
        name (str): Le prénom ou le nom à valider.

    Returns:
        bool: True si le nom est valide, False sinon.
    """
    return bool(re.match(r'^[a-zA-Z\s-]+$', name))


def get_player_data(player_number):
    """
    Demande à l'utilisateur de saisir les détails d'un nouveau joueur et valide les entrées.

    Args:
        player_number (int): Le numéro du joueur (pour indiquer quel joueur l'utilisateur est en train de saisir).

    Returns:
        dict: Un dictionnaire contenant les informations du joueur (prénom, nom, date de naissance).
    """
    print(f"\n\033[1m\033[4mVeuillez entrer les détails du joueur {player_number}:\033[0m\n")

    while True:
        first_name = input("Prénom: ").strip()
        if not validate_name(first_name):
            print("Le prénom ne doit contenir que des lettres, des espaces et des tirets. Veuillez réessayer.")
            continue

        last_name = input("Nom: ").strip()
        if not validate_name(last_name):
            print("Le nom ne doit contenir que des lettres, des espaces et des tirets. Veuillez réessayer.")
            continue

        birth_date = input("Date de naissance (YYYY-MM-DD): ").strip()
        try:
            # Valider le format de la date
            datetime.strptime(birth_date, "%Y-%m-%d")
        except ValueError:
            print("Format de date invalide. Veuillez entrer une date au format YYYY-MM-DD.")
            continue

        return {
            'first_name': first_name,
            'last_name': last_name,
            'birth_date': birth_date
        }
