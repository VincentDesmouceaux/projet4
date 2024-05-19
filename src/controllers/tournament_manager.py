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
            json.dump({"tournaments": [self.serialize_tournament(t)
                      for t in self.tournaments]}, file, indent=4, ensure_ascii=False)

    def serialize_tournament(self, tournament):
        return tournament.as_dict()

    def get_tournament_names(self):
        return [tournament.name for tournament in self.tournaments]

    def get_tournament_details(self, tournament_name):
        tournament = next((t for t in self.tournaments if t.name.lower() == tournament_name.lower()), None)
        if not tournament:
            raise ValueError("No tournament found with the name specified.")
        return tournament

    def run_round(self, tournament, is_resumed):
        current_round_index = tournament.current_round
        round_name = f"Round {current_round_index + 1}"
        round = next((r for r in tournament.rounds if r.name == round_name), None)

        if not round:
            round = Round(name=round_name)
            self.generate_matches(tournament, round)
            round.start_round(resume=is_resumed)
            tournament.add_round(round)
            print(f"Started {round_name}, current_round now {tournament.current_round}")

        current_match = round.get_current_match()
        while current_match:
            display_round_details(round, self, current_match=current_match)
            current_match = round.get_current_match()
            self.save_tournaments()  # Save the tournament state after each match

        if not round.end_time:
            round.end_round()
            tournament.current_round += 1  # Increment current_round here
            print(f"Round {round_name} ended, current_round now {tournament.current_round}")
        self.save_tournaments()  # Save the tournament state after the round ends

    def run_tournament(self, tournament_name, is_resumed=False):
        tournament = self.get_tournament_details(tournament_name)
        display_tournament_details(tournament)

        # Si le tournoi est terminé, afficher les scores finaux et proposer une réinitialisation
        if tournament.current_round >= tournament.number_of_rounds:
            if display_final_scores(tournament):
                self.reset_tournament(tournament_name)
                print("\nLe tournoi a été réinitialisé. Vous pouvez recommencer.\n")
            else:
                return

        # Reprendre le tournoi à partir du round en cours
        while tournament.current_round < tournament.number_of_rounds:
            self.run_round(tournament, is_resumed)
            is_resumed = False

            # Vérifier si le tournoi est terminé après le round courant
            if tournament.current_round >= tournament.number_of_rounds:
                break

        display_final_scores(tournament)
        self.save_tournaments()

    def generate_matches(self, tournament, round):
        from random import shuffle
        shuffle(tournament.players)
        for i in range(0, len(tournament.players), 2):
            match = Match(players=(tournament.players[i], tournament.players[i + 1]))
            round.add_match(match)

    def get_all_tournaments(self):
        return self.tournaments

    def add_tournament(self, tournament_data):
        players = [Player(**player_data) for player_data in tournament_data['players']]
        for player in players:
            player.score = 0.0  # Initialisation des scores à 0
        tournament_data['players'] = players
        new_tournament = Tournament(**tournament_data)
        self.tournaments.append(new_tournament)
        self.save_tournaments()
        print(f"\n\033[1m\033[32mTournoi {new_tournament.name} ajouté avec succès.\033[0m\n")

    def reset_tournament(self, tournament_name):
        tournament = self.get_tournament_details(tournament_name)
        tournament.current_round = 0
        tournament.rounds = []
        for player in tournament.players:
            player.score = 0.0
        self.save_tournaments()
        print(f"Tournoi {tournament_name} réinitialisé avec succès.")

    def reset_all_tournaments(self):
        for tournament in self.tournaments:
            tournament.current_round = 0
            tournament.rounds = []
            for player in tournament.players:
                player.score = 0.0
        self.save_tournaments()
        print("Tous les tournois ont été réinitialisés avec succès.")

    def get_paused_tournaments(self):
        return [tournament.name for tournament in self.tournaments if tournament.current_round > 0 and tournament.current_round < tournament.number_of_rounds]
