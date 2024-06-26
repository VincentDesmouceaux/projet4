"""
Module de vues pour les menus de l'application de tournoi d'échecs.

Ce module contient des fonctions pour afficher les différents menus de l'application, y compris le menu
principal, la sélection de tournoi et le menu des rapports.
"""


def display_welcome():
    """
    Affiche un message de bienvenue et demande à l'utilisateur s'il souhaite lancer un tournoi existant.

    Returns:
        str: La réponse de l'utilisateur (Oui/Non).
    """
    print("\n\033[1m\033[4mBonjour ! Bienvenue dans le Logiciel de tournoi d’échecs !\033[0m\n")
    return input("Voulez-vous lancer un tournoi existant ? (Oui/Non) : ")


def display_main_menu():
    print("\n\033[1m\033[4mQue voulez-vous faire ?\033[0m\n")
    print("1. Créer un nouveau tournoi\n")
    print("2. Consulter les rapports\n")
    print("3. Réinitialiser un tournoi\n")
    print("4. Quitter\n")
    return input("Entrez votre choix : ")


def display_tournament_selection(tournaments, include_paused=True):
    print("\n\033[1m\033[4mSélectionnez un tournoi parmi les suivants:\033[0m\n")
    for index, tournament in enumerate(tournaments, start=1):
        print(f"{index}. {tournament}\n")

    selection = input("Entrez le numéro du tournoi à lancer : ")
    try:
        selected_index = int(selection) - 1
        if 0 <= selected_index < len(tournaments):
            return tournaments[selected_index]
        elif include_paused and selected_index == len(tournaments):
            return "resume"
        elif selected_index == len(tournaments) + (1 if include_paused else 0):
            return None
        else:
            print("\n\033[31mNuméro invalide, veuillez réessayer.\033[0m\n")
            return display_tournament_selection(tournaments, include_paused)
    except ValueError:
        print("\n\033[31mVeuillez entrer un nombre valide.\033[0m\n")
        return display_tournament_selection(tournaments, include_paused)


def display_report_menu():
    """
    Affiche le menu des rapports et demande à l'utilisateur de choisir une option.

    Returns:
        str: Le choix de l'utilisateur.
    """
    print("\n\033[1m\033[4mQue voulez-vous faire ?\033[0m\n")
    print("1. Liste de tous les joueurs par ordre alphabétique\n")
    print("2. Liste de tous les tournois\n")
    print("3. Nom et dates d’un tournoi donné\n")
    print("4. Liste des joueurs du tournoi par ordre alphabétique\n")
    print("5. Liste de tous les tours du tournoi et de tous les matchs du tour\n")
    print("6. Retourner au menu principal\n")
    return input("Entrez votre choix : ")
