import json
from pathlib import Path
from datetime import datetime
from models.tournament import Tournament
from models.player import Player
from models.round import Round
from models.match import Match
from views.tournament_view import display_tournament_details, display_round_details, display_final_scores


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
        self.tournaments = [Tournament.from_dict(t_data) for t_data in tournaments_data]

    def save_tournaments(self):
        with self.filepath.open("w", encoding="utf-8") as file:
            json.dump({"tournaments": [t.as_dict() for t in self.tournaments]}, file, indent=4, ensure_ascii=False)

    def get_tournament_details(self, tournament_name):
        tournament = next((t for t in self.tournaments if t.name.lower() == tournament_name.lower()), None)
        if not tournament:
            raise ValueError("No tournament found with the name specified.")
        return tournament

    def get_tournament_names(self):
        return [tournament.name for tournament in self.tournaments]

    def run_tournament(self, tournament_name, is_resumed=False):
        tournament = self.get_tournament_details(tournament_name)
        display_tournament_details(tournament)

        if tournament.current_round >= tournament.number_of_rounds:
            if display_final_scores(tournament):
                self.reset_tournament(tournament_name)
            return

        while tournament.current_round < tournament.number_of_rounds:
            self.run_round(tournament, is_resumed)
            is_resumed = False

            if tournament.current_round >= tournament.number_of_rounds:
                break

        display_final_scores(tournament)
        self.save_tournaments()

    def run_round(self, tournament, is_resumed):
        current_round_index = tournament.current_round
        round_name = f"Round {current_round_index + 1}"
        round = next((r for r in tournament.rounds if r.name == round_name), None)

        if not round:
            round = Round(name=round_name)
            self.generate_matches(tournament, round)
            round.start_round(resume=is_resumed)
            tournament.add_round(round)

        current_match = round.get_current_match()
        while current_match:
            display_round_details(round, self, current_match=current_match)
            current_match = round.get_current_match()
            self.save_tournaments()

        if not round.is_completed():
            print(f"Round {round_name} is not completed, current_round remains {tournament.current_round}")
            return

        if not round.end_time:
            round.end_round()
            tournament.current_round += 1
        self.save_tournaments()

    def generate_matches(self, tournament, round):
        from random import shuffle
        shuffle(tournament.players)
        match_id = 1
        for i in range(0, len(tournament.players), 2):
            match = Match(id=match_id, players=(tournament.players[i], tournament.players[i + 1]))
            round.add_match(match)
            match_id += 1

    def get_paused_tournaments(self):
        return [t.name for t in self.tournaments if t.current_round > 0 and t.current_round < t.number_of_rounds]

    def reset_all_tournaments(self):
        for tournament in self.tournaments:
            tournament.current_round = 0
            tournament.rounds = []
            for player in tournament.players:
                player.score = 0.0
        self.save_tournaments()
        print("Tous les tournois ont été réinitialisés avec succès.")
