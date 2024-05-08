import json
from pathlib import Path
from controllers.report_manager import ReportManager
from controllers.user_manager import UserManager
from controllers.tournament_manager import TournamentManager
from views.menu_view import display_welcome, display_main_menu, display_tournament_selection, display_report_menu


class ApplicationController:
    def __init__(self, filepath):
        self.file_path = Path(filepath)
        data = self.load_data()
        self.user_manager = UserManager(filepath)
        self.tournament_manager = TournamentManager(filepath)
        self.report_manager = ReportManager(self.tournament_manager, self.user_manager, filepath)

    def load_data(self):
        if self.file_path.exists():
            with self.file_path.open('r', encoding='utf-8') as file:
                return json.load(file)
        return {}

    def start(self):
        start_action = display_welcome()

        if start_action.lower() == "oui":
            self.run_existing_tournament()
        else:
            self.main_menu_loop()

    def run_existing_tournament(self):
        tournament_name = display_tournament_selection(self.report_manager.get_tournament_names())
        self.tournament_manager.run_tournament(tournament_name)

    def main_menu_loop(self):
        while True:
            choice = display_main_menu()
            if choice == '1':
                # Supposer que cette fonction crée un nouveau tournoi (à implémenter)
                pass
            elif choice == '2':
                self.report_menu_loop()
            elif choice == '3':
                break  # Quitter l'application
            else:
                print("Option invalide, veuillez réessayer.")

    def report_menu_loop(self):
        while True:
            choice = display_report_menu()
            if choice == '1':
                self.report_manager.list_all_players()
            elif choice == '2':
                self.report_manager.list_all_tournaments()
            elif choice == '3':
                tournament_name = display_tournament_selection(self.report_manager.get_tournament_names())
                self.report_manager.show_tournament_details(tournament_name)
            elif choice == '4':
                tournament_name = display_tournament_selection(self.report_manager.get_tournament_names())
                self.report_manager.show_tournament_players_alphabetically(tournament_name)
            elif choice == '5':
                tournament_name = display_tournament_selection(self.report_manager.get_tournament_names())
                self.report_manager.show_tournament_rounds_and_matches(tournament_name)
            elif choice == '6':
                break  # Retourner au menu principal
            else:
                print("Option invalide, veuillez réessayer.")
