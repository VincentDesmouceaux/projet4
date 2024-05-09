"""
Module de vue pour la saisie des détails des joueurs.

Ce module contient une fonction pour demander à l'utilisateur de saisir les détails d'un nouveau joueur.
"""


def get_player_data(player_number):
    """
    Demande à l'utilisateur de saisir les détails d'un nouveau joueur.

    Args:
        player_number (int): Le numéro du joueur (pour indiquer quel joueur l'utilisateur est en train de saisir).

    Returns:
        dict: Un dictionnaire contenant les informations du joueur (prénom, nom, date de naissance).
    """
    print(f"\n\033[1m\033[4mVeuillez entrer les détails du joueur {player_number}:\033[0m\n")
    first_name = input("Prénom: ")
    last_name = input("Nom: ")
    birth_date = input("Date de naissance (YYYY-MM-DD): ")
    return {'first_name': first_name, 'last_name': last_name, 'birth_date': birth_date}
