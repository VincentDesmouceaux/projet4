from dataclasses import dataclass, field
from typing import List
import datetime
from .round import Round  # Assurez-vous que ce chemin est correct
from .player import Player  # Assurez-vous que ce chemin est correct


@dataclass
class Tournament:
    name: str
    location: str
    start_date: datetime.date
    end_date: datetime.date
    description: str
    number_of_rounds: int  # Déplacé avant les champs avec des valeurs par défaut
    rounds: List[Round] = field(default_factory=list)
    players: List[Player] = field(default_factory=list)
    current_round: int = 0

    def add_player(self, player: Player):
        """Ajoute un joueur à la liste des participants du tournoi."""
        self.players.append(player)

    def add_round(self, round: Round):
        """Ajoute un tour à la liste des tours du tournoi et incrémente le compteur de rounds actuels."""
        print("Adding round to tournament...")
        print(f"Current number of rounds: {len(self.rounds)}")
        print(f"Number of rounds specified: {self.number_of_rounds}")
        if len(self.rounds) < self.number_of_rounds:
            self.rounds.append(round)
            self.current_round += 1
            print("Round added successfully.")
        else:
            raise ValueError(
                "Cannot add more rounds than the number of rounds specified for the tournament."
            )

    def __str__(self):
        players_str = ", ".join(str(player) for player in self.players)
        rounds_str = "\n".join(str(round) for round in self.rounds)
        return (
            f"Tournament: {self.name}, Location: {self.location}, Dates: {self.start_date} to {self.end_date}\n"
            f"Description: {self.description}\n"
            f"Players: {players_str}\n"
            f"Rounds:\n    {rounds_str}"
        )
