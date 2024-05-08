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
    number_of_rounds: int
    rounds: List[Round] = field(default_factory=list)
    players: List[Player] = field(default_factory=list)
    current_round: int = 0

    def add_player(self, player: Player):
        self.players.append(player)

    def add_round(self, round: Round):
        if len(self.rounds) < self.number_of_rounds:
            self.rounds.append(round)
            self.current_round += 1
        else:
            raise ValueError("Cannot add more rounds than specified")

    def __str__(self):
        players_str = ", ".join(str(player) for player in self.players)
        rounds_str = "\n".join(str(round) for round in self.rounds)
        return (
            f"Tournament: {self.name}, Location: {self.location}, Dates: {self.start_date} to {self.end_date}\n"
            f"Description: {self.description}\n"
            f"Players: {players_str}\n"
            f"Rounds:\n    {rounds_str}"
        )

    def as_dict(self):
        return {
            "name": self.name,
            "location": self.location,
            "start_date": self.start_date.isoformat(),
            "end_date": self.end_date.isoformat(),
            "description": self.description,
            "number_of_rounds": self.number_of_rounds,
            "current_round": self.current_round,
            "players": [player.as_dict() for player in self.players],
            "rounds": [round.as_dict() for round in self.rounds]
        }
