# tournament_manager.py

import json
from pathlib import Path
from models.tournament import Tournament
from models.round import Round
from models.match import Match
from models.player import Player
from views.tournament_view import (
    display_tournament_details,
    display_final_scores,
    display_round_details,
)


class TournamentManager:
    def __init__(self, filepath):
        self.filepath = Path(filepath)
        self.tournaments = self.load_tournaments()

    def load_tournaments(self):
        if not self.filepath.exists():
            print("No file found, starting with an empty list of tournaments.")
            return []
        with self.filepath.open("r", encoding="utf-8") as file:
            data = json.load(file)
            loaded_tournaments = []
            for tournament_data in data.get("tournaments", []):
                # Transforme les dictionnaires des joueurs en objets Player
                players = [
                    Player(**player_data)
                    for player_data in tournament_data.get("players", [])
                ]
                tournament_data["players"] = players
                loaded_tournaments.append(Tournament(**tournament_data))
            return loaded_tournaments

    def save_tournaments(self):
        with self.filepath.open("w", encoding="utf-8") as file:
            json.dump(
                {
                    "tournaments": [
                        tournament.as_dict() for tournament in self.tournaments
                    ]
                },
                file,
                indent=4,
                ensure_ascii=False,
            )

    def get_tournament_names(self):
        return [tournament.name for tournament in self.tournaments]

    def get_tournament_details(self, tournament_name):
        for tournament in self.tournaments:
            if tournament.name.lower() == tournament_name.lower():
                return tournament
        raise ValueError("No tournament found with the name specified.")

    def run_tournament(self, tournament_name):
        tournament = self.get_tournament_details(tournament_name)
        display_tournament_details(tournament)
        while tournament.current_round < tournament.number_of_rounds:
            self.run_round(tournament)
        display_final_scores(tournament)

    def run_round(self, tournament):
        round = Round(name=f"Round {tournament.current_round + 1}")
        round.start_round()
        self.generate_and_play_matches(tournament, round)
        round.end_round()
        tournament.add_round(round)
        display_round_details(round)

    def generate_and_play_matches(self, tournament, round):
        from random import shuffle

        shuffle(tournament.players)
        for i in range(0, len(tournament.players), 2):
            match = Match(players=(tournament.players[i], tournament.players[i + 1]))
            match.play_match()
            round.add_match(match)
