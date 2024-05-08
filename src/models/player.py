from dataclasses import dataclass
import datetime


@dataclass
class Player:
    """
    Classe représentant un joueur dans un tournoi d'échecs.

    Attributes:
        first_name (str): Prénom du joueur.
        last_name (str): Nom de famille du joueur.
        birth_date (datetime.date): Date de naissance du joueur.
        chess_id (str): Identifiant unique du joueur dans le système.
        score (float): Score actuel du joueur dans le tournoi, initialisé à 0.
    """

    first_name: str
    last_name: str
    birth_date: datetime.date
    chess_id: str
    score: float = 0.0  # Initialisation du score à 0

    def __str__(self):
        return f"{self.first_name} {self.last_name}, Score: {self.score}"

    def as_dict(self):
        return {
            "first_name": self.first_name,
            "last_name": self.last_name,
            "birth_date": self.birth_date.isoformat(),
            "chess_id": self.chess_id,
            "score": self.score
        }
