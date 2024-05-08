import json
from pathlib import Path
from views.report_view import (
    display_all_tournaments,
    display_tournament_details,
    display_all_players_alphabetically,
    display_tournament_players_alphabetically,
    display_tournament_rounds_and_matches
)
from models.player import Player
from controllers.export_manager import ExportManager  # Importer le nouveau contrôleur


class ReportManager:
    def __init__(self, tournament_manager, user_manager, file_path):
        self.tournament_manager = tournament_manager
        self.user_manager = user_manager
        self.file_path = Path(file_path)
        self.export_manager = ExportManager()  # Créer une instance d'ExportManager
        self.load_data()

    def load_data(self):
        if self.file_path.exists():
            with self.file_path.open('r', encoding='utf-8') as file:
                data = json.load(file)
                self.tournament_manager.load_tournaments(data.get('tournaments', []))
                self.user_manager.players = [
                    Player(**p_data) if isinstance(p_data, dict) else p_data
                    for tournament in data.get('tournaments', [])
                    for p_data in tournament.get('players', [])
                ]
        else:
            print("Starting with an empty dataset.")

    def save_data(self):
        data = {
            "tournaments": self.tournament_manager.get_tournaments_data(),
            "players": [player.as_dict() for player in self.user_manager.get_all_players()]
        }
        with self.file_path.open('w', encoding='utf-8') as file:
            json.dump(data, file, indent=4, ensure_ascii=False)

    def list_all_tournaments(self):
        tournaments = self.tournament_manager.get_all_tournaments()
        display_all_tournaments(tournaments)
        self.ask_to_export_report("all_tournaments", display_all_tournaments, tournaments)

    def list_all_players(self):
        players = self.user_manager.get_all_players()
        display_all_players_alphabetically(players)
        self.ask_to_export_report("all_players", display_all_players_alphabetically, players)

    def show_tournament_details(self, tournament_name):
        tournament = self.tournament_manager.get_tournament_details(tournament_name)
        display_tournament_details(tournament)
        self.ask_to_export_report(f"tournament_details_{tournament_name}", display_tournament_details, tournament)

    def get_tournament_names(self):
        return self.tournament_manager.get_tournament_names()

    def show_tournament_players_alphabetically(self, tournament_name):
        tournament = self.tournament_manager.get_tournament_details(tournament_name)
        display_tournament_players_alphabetically(tournament)
        self.ask_to_export_report(f"tournament_players_{tournament_name}",
                                  display_tournament_players_alphabetically, tournament)

    def show_tournament_rounds_and_matches(self, tournament_name):
        tournament = self.tournament_manager.get_tournament_details(tournament_name)
        display_tournament_rounds_and_matches(tournament)
        self.ask_to_export_report(f"tournament_rounds_{tournament_name}",
                                  display_tournament_rounds_and_matches, tournament)

    def ask_to_export_report(self, filename, display_function, data):
        choice = input("Souhaitez-vous imprimer ce rapport ? (Oui/Non) : ")
        if choice.lower() == 'oui':
            format_choice = input("Choisissez le format : 1. Texte brut, 2. HTML, 3. Les deux : ")
            if format_choice == '1':
                self.export_manager.export_report(filename + ".txt", display_function, data)
            elif format_choice == '2':
                self.export_manager.export_report_html(filename + ".html", display_function, data)
            elif format_choice == '3':
                self.export_manager.export_report(filename + ".txt", display_function, data)
                self.export_manager.export_report_html(filename + ".html", display_function, data)
