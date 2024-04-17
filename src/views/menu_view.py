def display_main_menu():
    """
    Affiche le menu principal de l'application et récupère le choix de l'utilisateur.

    Returns:
        str: Le choix de l'utilisateur sous forme de chaîne de caractères.
    """
    print("\nMain Menu:")
    print("1. Create Tournament")
    print("2. List Tournaments")
    print("3. Exit")
    return input("Choose an option: ")

def display_welcome():
    """
    Affiche un message de bienvenue et demande si l'utilisateur veut lancer un tournoi existant.

    Returns:
        str: La réponse de l'utilisateur ('oui' ou 'non').
    """
    return input("Que voulez-vous faire ?\n1. Lancer un tournois existant ? (Oui/Non): ")

def display_tournament_selection(tournament_names):
    """
    Affiche la liste des tournois disponibles et permet à l'utilisateur de sélectionner un.

    Args:
        tournament_names (list of str): Liste des noms des tournois disponibles.

    Returns:
        str: Le nom du tournoi sélectionné par l'utilisateur.
    """
    print("Sélectionnez un tournoi parmi les suivants:")
    for name in tournament_names:
        print(name)
    return input("Entrez le nom du tournoi à lancer: ")
