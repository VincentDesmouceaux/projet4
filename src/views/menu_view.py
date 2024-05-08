def display_welcome():
    print("Bonjour ! Bienvenue dans le Logiciel de tournoi d’échecs !\n")
    return input("Voulez-vous lancer un tournoi existant ? (Oui/Non) : ")


def display_main_menu():
    print("\nQue voulez-vous faire ?")
    print("1. Créer un nouveau tournoi")
    print("2. Consulter les rapports")
    print("3. Quitter")
    return input("\nEntrez votre choix : ")


def display_tournament_selection(tournaments):
    print("Sélectionnez un tournoi parmi les suivants:\n")
    for index, tournament in enumerate(tournaments, start=1):
        print(f"{index}. {tournament}")

    selection = input("\nEntrez le numéro du tournoi à lancer : ")
    try:
        selected_index = int(selection) - 1
        if 0 <= selected_index < len(tournaments):
            return tournaments[selected_index]
        else:
            print("\nNuméro invalide, veuillez réessayer.\n")
            return display_tournament_selection(tournaments)
    except ValueError:
        print("\nVeuillez entrer un nombre valide.\n")
        return display_tournament_selection(tournaments)


def display_report_menu():
    print("\nQue voulez-vous faire ?")
    print("1. Liste de tous les joueurs par ordre alphabétique")
    print("2. Liste de tous les tournois")
    print("3. Nom et dates d’un tournoi donné")
    print("4. Liste des joueurs du tournoi par ordre alphabétique")
    print("5. Liste de tous les tours du tournoi et de tous les matchs du tour")
    print("6. Retourner au menu principal")
    return input("\nEntrez votre choix : ")
