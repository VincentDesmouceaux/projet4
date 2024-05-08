import json
from pathlib import Path
from models.player import Player


class UserManager:
    def __init__(self, file_path):
        self.file_path = Path(file_path)
        self.players = []

    def load_players(self, players_data):
        self.players = [Player(**data) for data in players_data]

    def save_players(self):
        with self.file_path.open('w', encoding='utf-8') as file:
            json.dump([player.as_dict() for player in self.players], file, indent=4, ensure_ascii=False)

    def add_player(self, player_data):
        new_player = Player(**player_data)
        self.players.append(new_player)
        self.save_players()
        return "Player added successfully!"

    def update_player(self, player_id, updated_data):
        for player in self.players:
            if player.chess_id == player_id:
                player.update(**updated_data)
                self.save_players()
                return f"Player {player_id} updated successfully!"
        return "Player ID not found."

    def get_all_players(self):
        return self.players
