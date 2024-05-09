def display_welcome():
    print("\n\033[1m\033[4mBonjour ! Bienvenue dans le Logiciel de tournoi d’échecs !\033[0m\n")
    return input("Voulez-vous lancer un tournoi existant ? (Oui/Non) : ")


def display_main_menu():
    print("\n\033[1m\033[4mQue voulez-vous faire ?\033[0m\n")
    print("1. Créer un nouveau tournoi\n")
    print("2. Consulter les rapports\n")
    print("3. Quitter\n")
    return input("Entrez votre choix : ")


def display_tournament_selection(tournaments):
    print("\n\033[1m\033[4mSélectionnez un tournoi parmi les suivants:\033[0m\n")
    for index, tournament in enumerate(tournaments, start=1):
        print(f"{index}. {tournament}\n")
    print(f"{len(tournaments) + 1}. Retour\n")
    selection = input("Entrez le numéro du tournoi à lancer : ")
    try:
        selected_index = int(selection) - 1
        if 0 <= selected_index < len(tournaments):
            return tournaments[selected_index]
        elif selected_index == len(tournaments):
            return None
        else:
            print("\n\033[31mNuméro invalide, veuillez réessayer.\033[0m\n")
            return display_tournament_selection(tournaments)
    except ValueError:
        print("\n\033[31mVeuillez entrer un nombre valide.\033[0m\n")
        return display_tournament_selection(tournaments)


def display_report_menu():
    print("\n\033[1m\033[4mQue voulez-vous faire ?\033[0m\n")
    print("1. Liste de tous les joueurs par ordre alphabétique\n")
    print("2. Liste de tous les tournois\n")
    print("3. Nom et dates d’un tournoi donné\n")
    print("4. Liste des joueurs du tournoi par ordre alphabétique\n")
    print("5. Liste de tous les tours du tournoi et de tous les matchs du tour\n")
    print("6. Retourner au menu principal\n")
    return input("Entrez votre choix : ")
