"""
Module pour la gestion des utilisateurs (joueurs).

Ce module contient la classe UserManager qui permet de gérer les joueurs,
y compris leur chargement, sauvegarde, ajout et mise à jour.
"""

import json
import random
import string
from pathlib import Path
from models.player import Player


class UserManager:
    """
    Classe responsable de la gestion des joueurs.

    Cette classe gère le chargement, la sauvegarde, l'ajout et la mise à jour
    des joueurs.
    """

    def __init__(self, file_path):
        """
        Initialise le UserManager.

        Args:
            file_path (str): Chemin vers le fichier de sauvegarde des joueurs.
        """
        self.file_path = Path(file_path)
        self.players = []

    def load_players(self, players_data):
        """
        Charge les joueurs à partir des données fournies.

        Args:
            players_data (list): Liste des données des joueurs.
        """
        self.players = [data if isinstance(data, Player) else Player.from_dict(data) for data in players_data]
        print(f"Loaded {len(self.players)} players.")

    def save_players(self):
        """
        Sauvegarde les joueurs dans un fichier JSON.
        """
        with self.file_path.open('w', encoding='utf-8') as file:
            json.dump([player.as_dict() for player in self.players], file, indent=4, ensure_ascii=False)

    def add_player(self, player_data):
        """
        Ajoute un nouveau joueur et le sauvegarde.

        Args:
            player_data (dict): Les données du nouveau joueur.

        Returns:
            str: Message de confirmation de l'ajout du joueur.
        """
        new_player = Player(**player_data)
        self.players.append(new_player)
        self.save_players()
        return "Player added successfully!"

    def update_player(self, player_id, updated_data):
        """
        Met à jour les informations d'un joueur existant.

        Args:
            player_id (str): ID du joueur à mettre à jour.
            updated_data (dict): Nouvelles données du joueur.

        Returns:
            str: Message de confirmation de la mise à jour ou message d'erreur si le joueur n'est pas trouvé.
        """
        for player in self.players:
            if player.chess_id == player_id:
                player.update(**updated_data)
                self.save_players()
                return f"Player {player_id} updated successfully!"
        return "Player ID not found."

    def get_all_players(self):
        """
        Retourne tous les joueurs.

        Returns:
            list: Liste de tous les joueurs.
        """
        return self.players

    def generate_unique_chess_id(self):
        """
        Génère un ID unique pour un joueur d'échecs.

        Returns:
            str: ID unique généré.
        """
        existing_ids = {player.chess_id for player in self.players}
        while True:
            new_id = ''.join(random.choices(string.ascii_uppercase, k=2)) + ''.join(random.choices(string.digits, k=5))
            if new_id not in existing_ids:
                return new_id
