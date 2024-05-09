"""
Module pour la gestion des tournois.

Ce module contient la classe TournamentManager qui permet de gérer les tournois,
y compris leur chargement, sauvegarde, exécution et génération des matchs.
"""

import json
from pathlib import Path
from models.tournament import Tournament
from models.player import Player
from models.round import Round
from models.match import Match
from views.tournament_view import display_tournament_details, display_final_scores, display_round_details
from datetime import datetime


class TournamentManager:
    """
    Classe responsable de la gestion des tournois.

    Cette classe gère le chargement, la sauvegarde, l'exécution et la génération
    des matchs pour les tournois.
    """

    def __init__(self, filepath):
        """
        Initialise le TournamentManager.

        Args:
            filepath (str): Chemin vers le fichier de sauvegarde des tournois.
        """
        self.filepath = Path(filepath)
        self.tournaments = []
        self.load_tournaments_from_file()

    def load_tournaments_from_file(self):
        """
        Charge les tournois depuis un fichier JSON.
        """
        if self.filepath.exists():
            with self.filepath.open("r", encoding="utf-8") as file:
                data = json.load(file)
                self.load_tournaments(data.get('tournaments', []))
        else:
            print("No file found, starting with an empty list of tournaments.")

    def load_tournaments(self, tournaments_data):
        """
        Charge les tournois à partir des données JSON.

        Args:
            tournaments_data (list): Liste des données des tournois.
        """
        self.tournaments = [Tournament.from_dict(t_data) for t_data in tournaments_data]

    def save_tournaments(self):
        """
        Sauvegarde les tournois dans un fichier JSON.
        """
        with self.filepath.open("w", encoding="utf-8") as file:
            json.dump({"tournaments": [self.serialize_tournament(t)
                                       for t in self.tournaments]}, file, indent=4, ensure_ascii=False)
        # print(f"Saved {len(self.tournaments)} tournaments.")

    def serialize_tournament(self, tournament):
        """
        Sérialise un tournoi en dictionnaire.

        Args:
            tournament (Tournament): Le tournoi à sérialiser.

        Returns:
            dict: Le tournoi sérialisé.
        """
        return tournament.as_dict()

    def get_tournament_names(self):
        """
        Retourne les noms de tous les tournois.

        Returns:
            list: Liste des noms des tournois.
        """
        return [tournament.name for tournament in self.tournaments]

    def get_tournament_details(self, tournament_name):
        """
        Retourne les détails d'un tournoi donné.

        Args:
            tournament_name (str): Le nom du tournoi.

        Returns:
            Tournament: Le tournoi trouvé.

        Raises:
            ValueError: Si aucun tournoi n'est trouvé avec le nom spécifié.
        """
        tournament = next((t for t in self.tournaments if t.name.lower() == tournament_name.lower()), None)
        if not tournament:
            raise ValueError("No tournament found with the name specified.")
        return tournament

    def run_tournament(self, tournament_name):
        """
        Exécute un tournoi jusqu'à ce que tous les tours soient complétés.

        Args:
            tournament_name (str): Le nom du tournoi à exécuter.
        """
        tournament = self.get_tournament_details(tournament_name)
        display_tournament_details(tournament)
        while tournament.current_round < tournament.number_of_rounds:
            self.run_round(tournament)
        display_final_scores(tournament)
        self.save_tournaments()

    def run_round(self, tournament):
        """
        Exécute un tour du tournoi.

        Args:
            tournament (Tournament): Le tournoi en cours d'exécution.
        """
        round = Round(name=f"Round {tournament.current_round + 1}")
        round.start_round()
        self.generate_and_play_matches(tournament, round)
        round.end_round()
        tournament.add_round(round)
        display_round_details(round)
        self.save_tournaments()

    def generate_and_play_matches(self, tournament, round):
        """
        Génère et joue les matchs pour un tour.

        Args:
            tournament (Tournament): Le tournoi en cours d'exécution.
            round (Round): Le tour actuel.
        """
        from random import shuffle
        shuffle(tournament.players)
        for i in range(0, len(tournament.players), 2):
            match = Match(players=(tournament.players[i], tournament.players[i + 1]))
            match.play_match()
            round.add_match(match)

    def get_all_tournaments(self):
        """
        Retourne tous les tournois.

        Returns:
            list: Liste de tous les tournois.
        """
        return self.tournaments

    def add_tournament(self, tournament_data):
        """
        Ajoute un nouveau tournoi et le sauvegarde.

        Args:
            tournament_data (dict): Les données du nouveau tournoi.
        """
        players = [Player(**player_data) for player_data in tournament_data['players']]
        tournament_data['players'] = players
        new_tournament = Tournament(**tournament_data)
        self.tournaments.append(new_tournament)
        self.save_tournaments()
        print(f"\n\033[1m\033[32mTournoi {new_tournament.name} ajouté avec succès.\033[0m\n")

    def reset_tournament(self, tournament_name):
        """
        Réinitialise les scores et les rounds d'un tournoi donné.

        Args:
            tournament_name (str): Le nom du tournoi à réinitialiser.
        """
        tournament = self.get_tournament_details(tournament_name)
        tournament.current_round = 0
        tournament.rounds = []
        for player in tournament.players:
            player.score = 0.0
        self.save_tournaments()
        print(f"Tournoi {tournament_name} réinitialisé avec succès.")
