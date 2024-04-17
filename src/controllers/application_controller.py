from controllers.menu_manager import MenuManager
from controllers.tournament_manager import TournamentManager
from controllers.user_manager import UserManager

class ApplicationController:
    """
    Contrôleur principal de l'application qui orchestre les interactions entre les menus,
    la gestion des tournois, et la gestion des utilisateurs.

    Attributes:
        menu_manager (MenuManager): Gère les interactions du menu principal.
        tournament_manager (TournamentManager): Gère les opérations liées aux tournois.
        user_manager (UserManager): Gère les informations relatives aux utilisateurs.
    """
    def __init__(self):
        """Initialise les managers utilisés dans l'application."""
        self.menu_manager = MenuManager()
        self.tournament_manager = TournamentManager()
        self.user_manager = UserManager()

    def run(self):
        """
        Lance le cycle principal de l'application où les commandes sont reçues et traitées.
        """
        while True:
            action = self.menu_manager.display_main_menu()
            if action == '1':
                self.tournament_manager.handle_tournament_creation()
            elif action == '2':
                self.tournament_manager.list_tournaments()
            elif action == 'exit':
                break
            else:
                print("Invalid option, please try again.")
