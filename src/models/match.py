"""
Module pour la gestion des matchs d'échecs.

Ce module contient la classe Match qui représente un match entre deux joueurs,
avec leurs scores respectifs.
"""

from dataclasses import dataclass, field
from .player import Player


@dataclass
class Match:
    players: tuple
    score: tuple = field(default_factory=lambda: (0.0, 0.0))

    def enter_score(self, choice):
        """
        Met à jour le score du match en fonction du choix de l'utilisateur.

        Args:
            choice (int): Le choix de l'utilisateur indiquant le résultat du match.
        """
        if choice == 1:
            self.score = (0.5, 0.5)
        elif choice == 2:
            self.score = (1, 0)
        elif choice == 3:
            self.score = (0, 1)
        self.update_player_scores()

    def update_player_scores(self):
        self.players[0].score += self.score[0]
        self.players[1].score += self.score[1]

    def __str__(self):
        return f"Match: {self.players[0]} vs {self.players[1]}, Score: {self.score}"

    def as_dict(self):
        return {
            "players": [player.as_dict() for player in self.players],
            "score": self.score
        }

    @classmethod
    def from_dict(cls, data):
        players = tuple(Player.from_dict(p_data) for p_data in data["players"])
        score = tuple(data["score"])
        return cls(players=players, score=score)
