import json
from pathlib import Path
from models.tournament import Tournament
from models.player import Player
from models.round import Round
from models.match import Match
from views.tournament_view import display_tournament_details, display_final_scores, display_round_details


class TournamentManager:
    def __init__(self, filepath):
        self.filepath = Path(filepath)
        self.tournaments = []
        self.load_tournaments_from_file()

    def load_tournaments_from_file(self):
        if self.filepath.exists():
            with self.filepath.open("r", encoding="utf-8") as file:
                data = json.load(file)
                self.load_tournaments(data.get('tournaments', []))
        else:
            print("No file found, starting with an empty list of tournaments.")

    def load_tournaments(self, tournaments_data):
        self.tournaments = [self.deserialize_tournament(t_data) for t_data in tournaments_data]

    def deserialize_tournament(self, data):
        players = [Player(**player_data) for player_data in data.get("players", [])]
        data["players"] = players
        rounds = [Round(**round_data) for round_data in data.get("rounds", [])]
        data["rounds"] = rounds
        return Tournament(**data)

    def save_tournaments(self):
        with self.filepath.open("w", encoding="utf-8") as file:
            json.dump({"tournaments": [self.serialize_tournament(t)
                      for t in self.tournaments]}, file, indent=4, ensure_ascii=False)

    def serialize_tournament(self, tournament):
        tournament_data = tournament.as_dict()
        tournament_data["players"] = [player.as_dict() for player in tournament.players]
        return tournament_data

    def get_tournament_names(self):
        return [tournament.name for tournament in self.tournaments]

    def get_tournament_details(self, tournament_name):
        tournament = next((t for t in self.tournaments if t.name.lower() == tournament_name.lower()), None)
        if not tournament:
            raise ValueError("No tournament found with the name specified.")
        return tournament

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

    def get_all_tournaments(self):
        return self.tournaments
