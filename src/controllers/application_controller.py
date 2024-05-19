from pathlib import Path
import json
from datetime import datetime
from controllers.tournament_manager import TournamentManager
from controllers.user_manager import UserManager
from controllers.report_manager import ReportManager
from views.menu_view import display_welcome, display_main_menu, display_tournament_selection, display_report_menu
from views.tournament_view import display_tournament_details, display_round_details, display_final_scores, get_tournament_data
from views.player_view import get_player_data


class ApplicationController:
    def __init__(self, filepath):
        self.file_path = Path(filepath)
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
        if tournament_name == "resume":
            self.resume_tournament()
        elif tournament_name is not None:
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
                self.reset_tournament()
            elif choice == '4':
                print("Merci d'avoir utilisé le logiciel de tournoi d'échecs ! À bientôt !")
                break  # Quitter l'application
            else:
                print("Option invalide, veuillez réessayer.")

    def reset_tournament(self):
        print("\n1. Réinitialiser un tournoi spécifique\n2. Réinitialiser tous les tournois\n3. Retour")
        choice = input("Entrez votre choix : ")
        if choice == '1':
            tournament_name = display_tournament_selection(self.tournament_manager.get_tournament_names())
            if tournament_name:
                self.tournament_manager.reset_tournament(tournament_name)
                print(f"Tournoi {tournament_name} réinitialisé avec succès.")
        elif choice == '2':
            self.tournament_manager.reset_all_tournaments()
        elif choice == '3':
            return
        else:
            print("Option invalide, veuillez réessayer.")
            self.reset_tournament()

    def create_new_tournament(self):
        tournament_data = get_tournament_data()
        tournament_data['start_date'] = datetime.strptime(tournament_data['start_date'], "%Y-%m-%d").date()
        tournament_data['end_date'] = datetime.strptime(tournament_data['end_date'], "%Y-%m-%d").date()

        players = []
        for i in range(1, 9):  # Ajoutez des joueurs au tournoi
            player_data = get_player_data(i)
            player_data['birth_date'] = datetime.strptime(player_data['birth_date'], "%Y-%m-%d").date()
            player_data['chess_id'] = self.user_manager.generate_unique_chess_id()
            players.append(player_data)
        tournament_data['players'] = players

        self.tournament_manager.add_tournament(tournament_data)
        print("\n\033[1m\033[32mTournoi créé avec succès !\033[0m\n")

    def report_menu_loop(self):
        while True:
            choice = display_report_menu()
            if choice == '1':
                self.report_manager.list_all_players()
            elif choice == '2':
                self.report_manager.list_all_tournaments()
            elif choice == '3':
                tournament_name = display_tournament_selection(
                    self.report_manager.get_tournament_names(), include_paused=False)
                self.report_manager.show_tournament_details(tournament_name)
            elif choice == '4':
                tournament_name = display_tournament_selection(
                    self.report_manager.get_tournament_names(), include_paused=False)
                self.report_manager.show_tournament_players_alphabetically(tournament_name)
            elif choice == '5':
                tournament_name = display_tournament_selection(
                    self.report_manager.get_tournament_names(), include_paused=False)
                self.report_manager.show_tournament_rounds_and_matches(tournament_name)
            elif choice == '6':
                break  # Retourner au menu principal
            else:
                print("Option invalide, veuillez réessayer.")

    def resume_tournament(self):
        paused_tournaments = self.tournament_manager.get_paused_tournaments()
        if not paused_tournaments:
            print("Aucun tournoi en pause disponible.")
            return

        tournament_name = display_tournament_selection(paused_tournaments)
        if tournament_name:
            self.tournament_manager.run_tournament(tournament_name, is_resumed=True)
        else:
            self.main_menu_loop()
