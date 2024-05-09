"""
Module pour la gestion des matchs d'échecs.

Ce module contient la classe Match qui représente un match entre deux joueurs,
avec leurs scores respectifs. La classe permet de jouer un match, mettre à jour
les scores des joueurs et fournir des représentations en chaîne et en dictionnaire
du match.
"""

from dataclasses import dataclass, field
import random
from .player import Player


@dataclass
class Match:
    """
    Classe représentant un match d'échecs entre deux joueurs.

    Attributes:
        players (tuple): Un tuple contenant deux objets Player représentant les joueurs du match.
        score (tuple): Un tuple contenant les scores des deux joueurs.
    """
    players: tuple
    score: tuple = field(default_factory=lambda: (0.0, 0.0))

    def play_match(self):
        """
        Joue le match en attribuant un score aléatoire aux joueurs.

        Le score est choisi parmi (1, 0), (0, 1), et (0.5, 0.5).
        Après avoir joué le match, les scores des joueurs sont mis à jour.
        """
        self.score = random.choice([(1, 0), (0, 1), (0.5, 0.5)])
        self.update_player_scores()

    def update_player_scores(self):
        """
        Met à jour les scores des joueurs en ajoutant les scores du match aux scores actuels des joueurs.
        """
        self.players[0].score += self.score[0]
        self.players[1].score += self.score[1]

    def __str__(self):
        """
        Retourne une représentation en chaîne de caractères du match.

        Returns:
            str: Représentation du match sous forme de chaîne de caractères.
        """
        return f"Match: {self.players[0]} vs {self.players[1]}, Score: {self.score}"

    def as_dict(self):
        """
        Convertit le match en un dictionnaire.

        Returns:
            dict: Dictionnaire représentant le match avec les joueurs et les scores.
        """
        return {
            "players": [player.as_dict() for player in self.players],
            "score": self.score
        }

    @classmethod
    def from_dict(cls, data):
        """
        Crée une instance de Match à partir d'un dictionnaire.

        Args:
            data (dict): Dictionnaire contenant les données du match.

        Returns:
            Match: Instance de Match créée à partir des données fournies.
        """
        players = tuple(Player.from_dict(p_data) for p_data in data["players"])
        score = tuple(data["score"])
        return cls(players=players, score=score)
