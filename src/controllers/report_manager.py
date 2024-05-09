"""
Module pour la gestion des rapports.

Ce module contient la classe ReportManager qui permet de gérer et d'exporter
des rapports pour les tournois et les joueurs.
"""

import json
from views.report_view import (
    display_all_tournaments,
    display_tournament_details,
    display_all_players_alphabetically,
    display_tournament_players_alphabetically,
    display_tournament_rounds_and_matches
)
from controllers.export_manager import ExportManager


class ReportManager:
    """
    Classe responsable de la gestion des rapports.

    Cette classe gère la création, l'affichage et l'exportation des rapports
    pour les tournois et les joueurs.
    """

    def __init__(self, tournament_manager, user_manager):
        """
        Initialise le ReportManager.

        Args:
            tournament_manager (TournamentManager): Le gestionnaire de tournois.
            user_manager (UserManager): Le gestionnaire des utilisateurs.
        """
        self.tournament_manager = tournament_manager
        self.user_manager = user_manager
        self.export_manager = ExportManager()
        self.load_data()

    def load_data(self):
        """
        Charge les données des tournois et des joueurs depuis le fichier JSON.
        """
        if self.tournament_manager.filepath.exists():
            with self.tournament_manager.filepath.open('r', encoding='utf-8') as file:
                data = json.load(file)
                self.tournament_manager.load_tournaments(data.get('tournaments', []))
                players = []
                for tournament in self.tournament_manager.tournaments:
                    players.extend(tournament.players)
                self.user_manager.load_players(players)
        else:
            print("Starting with an empty dataset.")

    def save_data(self):
        """
        Sauvegarde les données des tournois et des joueurs dans le fichier JSON.
        """
        data = {
            "tournaments": self.tournament_manager.get_tournaments_data(),
            "players": [player.as_dict() for player in self.user_manager.get_all_players()]
        }
        with self.tournament_manager.filepath.open('w', encoding='utf-8') as file:
            json.dump(data, file, indent=4, ensure_ascii=False)

    def list_all_tournaments(self):
        """
        Affiche la liste de tous les tournois et propose d'exporter le rapport.
        """
        tournaments = self.tournament_manager.get_all_tournaments()
        display_all_tournaments(tournaments)
        self.ask_to_export_report("all_tournaments", display_all_tournaments, tournaments)

    def list_all_players(self):
        """
        Affiche la liste de tous les joueurs par ordre alphabétique et propose d'exporter le rapport.
        """
        players = self.user_manager.get_all_players()
        display_all_players_alphabetically(players)
        self.ask_to_export_report("all_players", display_all_players_alphabetically, players)

    def show_tournament_details(self, tournament_name):
        """
        Affiche les détails d'un tournoi et propose d'exporter le rapport.

        Args:
            tournament_name (str): Le nom du tournoi.
        """
        tournament = self.tournament_manager.get_tournament_details(tournament_name)
        display_tournament_details(tournament)
        self.ask_to_export_report(f"tournament_details_{tournament_name}", display_tournament_details, tournament)

    def get_tournament_names(self):
        """
        Retourne les noms de tous les tournois.

        Returns:
            list: Liste des noms de tournois.
        """
        return self.tournament_manager.get_tournament_names()

    def show_tournament_players_alphabetically(self, tournament_name):
        """
        Affiche la liste des joueurs d'un tournoi par ordre alphabétique et propose d'exporter le rapport.

        Args:
            tournament_name (str): Le nom du tournoi.
        """
        tournament = self.tournament_manager.get_tournament_details(tournament_name)
        display_tournament_players_alphabetically(tournament)
        self.ask_to_export_report(f"tournament_players_{tournament_name}",
                                  display_tournament_players_alphabetically, tournament)

    def show_tournament_rounds_and_matches(self, tournament_name):
        """
        Affiche tous les tours et matchs d'un tournoi et propose d'exporter le rapport.

        Args:
            tournament_name (str): Le nom du tournoi.
        """
        tournament = self.tournament_manager.get_tournament_details(tournament_name)
        display_tournament_rounds_and_matches(tournament)
        self.ask_to_export_report(f"tournament_rounds_{tournament_name}",
                                  display_tournament_rounds_and_matches, tournament)

    def ask_to_export_report(self, filename, display_function, data):
        """
        Demande à l'utilisateur s'il souhaite exporter le rapport et dans quel format.

        Args:
            filename (str): Le nom de base du fichier de rapport.
            display_function (function): La fonction utilisée pour générer le contenu du rapport.
            data (any): Les données à passer à la fonction de génération de rapport.
        """
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
