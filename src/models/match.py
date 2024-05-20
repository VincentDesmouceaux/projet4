from dataclasses import dataclass, field
from .player import Player


@dataclass
class Match:
    """
    Représente un match dans un tour d'un tournoi d'échecs.

    Attributes:
        id (int): Identifiant unique pour chaque match.
        players (tuple): Les deux joueurs du match.
        score (tuple): Le score du match (par défaut (0.0, 0.0)).
    """
    id: int  # Identifiant unique pour chaque match
    players: tuple
    score: tuple = field(default_factory=lambda: (0.0, 0.0))

    def update_player_scores(self):
        """
        Met à jour les scores des joueurs en fonction du score du match.
        """
        self.players[0].score += self.score[0]
        self.players[1].score += self.score[1]

    def __str__(self):
        return f"Match {self.id}: {self.players[0]} vs {self.players[1]}, Score: {self.score}"

    def as_dict(self):
        """
        Convertit l'objet Match en dictionnaire.

        Returns:
            dict: Le dictionnaire représentant le match.
        """
        return {
            "id": self.id,
            "players": [player.as_dict() for player in self.players],
            "score": self.score
        }

    @classmethod
    def from_dict(cls, data):
        """
        Crée un objet Match à partir d'un dictionnaire.

        Args:
            data (dict): Le dictionnaire contenant les données du match.

        Returns:
            Match: L'objet Match créé.
        """
        players = tuple(Player.from_dict(p_data) for p_data in data["players"])
        score = tuple(data["score"])
        return cls(id=data["id"], players=players, score=score)
