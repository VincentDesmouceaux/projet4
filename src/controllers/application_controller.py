"""
Module de contrôle principal pour l'application de gestion de tournois d'échecs.

Ce module contient la classe ApplicationController qui orchestre le flux global de l'application,
gérant les interactions avec l'utilisateur et coordonnant les actions entre les différents gestionnaires.
"""

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
    """
    Classe principale pour le contrôle de l'application.

    Cette classe gère le cycle de vie de l'application, y compris le chargement des données,
    la gestion des utilisateurs, des tournois et la génération de rapports.
    """

    def __init__(self, filepath):
        """
        Initialise le contrôleur de l'application.

        Args:
            filepath (str): Le chemin du fichier de données JSON.
        """
        self.file_path = Path(filepath)
        self.user_manager = UserManager(filepath)
        self.tournament_manager = TournamentManager(filepath)
        self.report_manager = ReportManager(self.tournament_manager, self.user_manager)

    def load_data(self):
        """
        Charge les données à partir du fichier JSON.

        Returns:
            dict: Les données chargées depuis le fichier JSON, ou un dictionnaire vide si le fichier n'existe pas.
        """
        if self.file_path.exists():
            with self.file_path.open('r', encoding='utf-8') as file:
                return json.load(file)
        return {}

    def start(self):
        """
        Démarre l'application en affichant le menu de bienvenue et en dirigeant l'utilisateur
        vers le démarrage d'un tournoi existant ou vers le menu principal.
        """
        start_action = display_welcome()
        if start_action.lower() == "oui":
            self.run_existing_tournament()
        else:
            self.main_menu_loop()

    def run_existing_tournament(self):
        """
        Lance un tournoi existant sélectionné par l'utilisateur.
        """
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
                self.reset_tournament()
            elif choice == '4':
                break  # Quitter l'application
            else:
                print("Option invalide, veuillez réessayer.")

    def create_new_tournament(self):
        """
        Crée un nouveau tournoi en collectant les informations du tournoi et des joueurs,
        puis en ajoutant le tournoi via le TournamentManager.
        """
        tournament_data = get_tournament_data()
        tournament_data['start_date'] = datetime.strptime(tournament_data['start_date'], "%Y-%m-%d").date()
        tournament_data['end_date'] = datetime.strptime(tournament_data['end_date'], "%Y-%m-%d").date()

        players = []
        for i in range(1, 5):  # Ajoutez des joueurs au tournoi
            player_data = get_player_data(i)
            player_data['birth_date'] = datetime.strptime(player_data['birth_date'], "%Y-%m-%d").date()
            player_data['chess_id'] = self.user_manager.generate_unique_chess_id()
            players.append(player_data)
        tournament_data['players'] = players

        self.tournament_manager.add_tournament(tournament_data)
        print("\n\033[1m\033[32mTournoi créé avec succès !\033[0m\n")

    def report_menu_loop(self):
        """
        Affiche et gère le menu des rapports.
        """
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

    def reset_tournament(self):
        tournament_name = display_tournament_selection(self.report_manager.get_tournament_names())
        if tournament_name:
            self.tournament_manager.reset_tournament(tournament_name)
        else:
            print("Aucun tournoi sélectionné pour réinitialisation.")
