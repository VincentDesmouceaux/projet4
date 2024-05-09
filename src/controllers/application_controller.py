import json
from pathlib import Path
from datetime import datetime
from controllers.report_manager import ReportManager
from controllers.user_manager import UserManager
from controllers.tournament_manager import TournamentManager
from views.menu_view import display_welcome, display_main_menu, display_tournament_selection, display_report_menu
from views.tournament_view import get_tournament_data
from views.player_view import get_player_data


class ApplicationController:
    def __init__(self, filepath):
        self.file_path = Path(filepath)
        data = self.load_data()
        self.user_manager = UserManager(filepath)
        self.tournament_manager = TournamentManager(filepath)
        self.report_manager = ReportManager(self.tournament_manager, self.user_manager)

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
        if tournament_name is not None:
            self.tournament_manager.run_tournament(tournament_name)
        else:
            self.main_menu_loop()

    def main_menu_loop(self):
        while True:
            choice = display_main_menu()
            if choice == '1':
                self.create_new_tournament()
            elif choice == '2':
                self.report_menu_loop()
            elif choice == '3':
                break  # Quitter l'application
            else:
                print("Option invalide, veuillez réessayer.")

    def create_new_tournament(self):
        tournament_data = get_tournament_data()
        tournament_data['start_date'] = datetime.strptime(tournament_data['start_date'], "%Y-%m-%d").date()
        tournament_data['end_date'] = datetime.strptime(tournament_data['end_date'], "%Y-%m-%d").date()

        players = []
        for _ in range(4):
            player_data = get_player_data()
            player_data['birth_date'] = datetime.strptime(player_data['birth_date'], "%Y-%m-%d").date()
            player_data['chess_id'] = self.user_manager.generate_unique_chess_id()
            players.append(player_data)
        tournament_data['players'] = players

        self.tournament_manager.add_tournament(tournament_data)
        print("Tournoi créé avec succès !")

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
