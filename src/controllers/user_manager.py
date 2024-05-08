import json
import random
import string
from pathlib import Path
from models.player import Player
from datetime import datetime


class UserManager:
    def __init__(self, file_path):
        self.file_path = Path(file_path)
        self.players = []

    def load_players(self, players_data):
        self.players = [
            Player(
                first_name=data['first_name'],
                last_name=data['last_name'],
                birth_date=datetime.strptime(data['birth_date'], "%Y-%m-%d").date(),
                chess_id=data['chess_id'],
                score=data.get('score', 0.0)
            ) for data in players_data
        ]
        print(f"Loaded {len(self.players)} players.")

    def save_players(self):
        with self.file_path.open('w', encoding='utf-8') as file:
            json.dump([player.as_dict() for player in self.players], file, indent=4, ensure_ascii=False)
        print(f"Saved {len(self.players)} players.")

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

    def generate_unique_chess_id(self):
        existing_ids = {player.chess_id for player in self.players}
        while True:
            new_id = ''.join(random.choices(string.ascii_uppercase, k=2)) + ''.join(random.choices(string.digits, k=5))
            if new_id not in existing_ids:
                return new_id
