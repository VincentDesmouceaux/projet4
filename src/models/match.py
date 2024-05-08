from dataclasses import dataclass, field
import random
from .player import Player


@dataclass
class Match:
    """
    Classe représentant un match entre deux joueurs dans un tournoi d'échecs.

    Attributes:
        players (tuple): Tuple contenant deux instances de Player.
        score (tuple): Tuple contenant les scores des deux joueurs, initialisé à (0.0, 0.0).
    """

    players: tuple
    score: tuple = field(default_factory=lambda: (0.0, 0.0))

    def play_match(self):
        """
        Simule le match entre les deux joueurs et attribue les scores de manière aléatoire.
        """
        self.score = random.choice([(1, 0), (0, 1), (0.5, 0.5)])
        self.update_player_scores()

    def update_player_scores(self):
        """
        Met à jour le score de chaque joueur basé sur le résultat du match.
        """
        self.players[0].score += self.score[0]
        self.players[1].score += self.score[1]

    def __str__(self):
        return f"Match: {self.players[0]} vs {self.players[1]}, Score: {self.score}"

    def as_dict(self):
        return {
            "players": [player.as_dict() for player in self.players],
            "score": self.score
        }
