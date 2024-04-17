from pathlib import Path
from controllers.tournament_manager import TournamentManager
from views.menu_view import display_welcome, display_main_menu, display_tournament_selection

def main():
    """
    Fonction principale pour démarrer l'application.
    """
    print("Bonjour ! Bienvenue dans le Logiciel de tournoi d’échecs !")

    # Chemin vers le fichier JSON contenant les données des tournois
    json_file_path = Path('src/data/tournaments.json')

    # Initialisation du gestionnaire de tournois
    tournament_manager = TournamentManager(json_file_path)

    # Affichage du message de bienvenue et récupération de l'action initiale
    start_action = display_welcome()

    if start_action.lower() == "oui":
        tournament_name = display_tournament_selection(tournament_manager.get_tournament_names())
        tournament_manager.run_tournament(tournament_name)
    else:
        # Boucle principale de l'application
        while True:
            choice = display_main_menu()
            if choice == '1':
                # Gérer la création de tournois
                tournament_manager.handle_tournament_creation()
            elif choice == '2':
                # Gérer l'affichage des tournois
                tournament_manager.list_tournaments()
            elif choice == '3':
                # Sortir de l'application
                break
            else:
                print("Invalid option, please try again.")

if __name__ == "__main__":
    main()
