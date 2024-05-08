import json
from pathlib import Path
from views.report_view import (
    display_all_tournaments,
    display_tournament_details,
    display_all_players_alphabetically,
    display_tournament_players_alphabetically,
)
from models.player import Player


class ReportManager:
    def __init__(self, tournament_manager, user_manager, file_path):
        self.tournament_manager = tournament_manager
        self.user_manager = user_manager
        self.file_path = Path(file_path)
        self.load_data()

    def load_data(self):
        if self.file_path.exists():
            with self.file_path.open('r', encoding='utf-8') as file:
                data = json.load(file)
                self.tournament_manager.load_tournaments(data.get('tournaments', []))
                players_data = [p_data for tournament in data.get(
                    'tournaments', []) for p_data in tournament.get('players', [])]
                self.user_manager.players = [Player(**p_data) if isinstance(p_data, dict)
                                             else p_data for p_data in players_data]
        else:
            print("Starting with an empty dataset.")

    def save_data(self):
        data = {
            "tournaments": self.tournament_manager.get_tournaments_data(),
            "players": [player.as_dict() for player in self.user_manager.players]
        }
        with self.file_path.open('w', encoding='utf-8') as file:
            json.dump(data, file, indent=4, ensure_ascii=False)

    def list_all_tournaments(self):
        tournaments = self.tournament_manager.get_all_tournaments()
        display_all_tournaments(tournaments)

    def list_all_players(self):
        players = self.user_manager.get_all_players()
        display_all_players_alphabetically(players)

    def get_tournament_names(self):
        return self.tournament_manager.get_tournament_names()
