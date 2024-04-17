from models.player import Player
from views.player_view import get_player_data, display_players, update_player_view
from utils.file_handler import load_players, save_players

class UserManager:
    """
    Gère les opérations liées aux joueurs dans le système.

    Methods:
        add_player(): Ajoute un nouveau joueur au système.
        update_player(): Met à jour les informations d'un joueur existant.
        list_players(): Affiche tous les joueurs enregistrés.
    """

    def __init__(self):
        """Charge les joueurs existants à partir du fichier de données."""
        self.players = load_players()

    def add_player(self):
        """Demande les données du joueur et l'ajoute à la liste des joueurs."""
        player_data = get_player_data()
        new_player = Player(**player_data)
        self.players.append(new_player)
        save_players(self.players)
        print("Player added successfully!")

    def update_player(self):
        """Affiche les joueurs et permet à l'utilisateur de choisir un pour mise à jour."""
        display_players(self.players)
        player_id, updated_data = update_player_view()
        for player in self.players:
            if player.chess_id == player_id:
                player.update(**updated_data)
                save_players(self.players)
                print(f"Player {player_id} updated successfully!")
                break

    def list_players(self):
        """Affiche tous les joueurs enregistrés."""
        display_players(self.players)
