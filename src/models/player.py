"""
Module pour la gestion des joueurs d'échecs.

Ce module contient la classe Player qui représente un joueur d'échecs avec ses
informations personnelles et son score. La classe permet de convertir un joueur
en dictionnaire et de créer un joueur à partir d'un dictionnaire.
"""

from dataclasses import dataclass
import datetime


@dataclass
class Player:
    """
    Classe représentant un joueur d'échecs.

    Attributes:
        first_name (str): Le prénom du joueur.
        last_name (str): Le nom de famille du joueur.
        birth_date (datetime.date): La date de naissance du joueur.
        chess_id (str): L'identifiant unique du joueur.
        score (float): Le score du joueur. Par défaut, il est de 0.0.
    """
    first_name: str
    last_name: str
    birth_date: datetime.date
    chess_id: str
    score: float = 0.0

    def __str__(self):
        """
        Retourne une représentation en chaîne de caractères du joueur.

        Returns:
            str: Représentation du joueur sous forme de chaîne de caractères.
        """
        return f"{self.first_name} {self.last_name}, Score: {self.score}"

    def as_dict(self):
        """
        Convertit le joueur en un dictionnaire.

        Returns:
            dict: Dictionnaire représentant le joueur avec ses informations personnelles et son score.
        """
        return {
            "first_name": self.first_name,
            "last_name": self.last_name,
            "birth_date": self.birth_date.isoformat(),
            "chess_id": self.chess_id,
            "score": self.score
        }

    @classmethod
    def from_dict(cls, data):
        """
        Crée une instance de Player à partir d'un dictionnaire.

        Args:
            data (dict): Dictionnaire contenant les données du joueur.

        Returns:
            Player: Instance de Player créée à partir des données fournies.
        """
        birth_date = datetime.datetime.strptime(data["birth_date"], "%Y-%m-%d").date()
        return cls(
            first_name=data["first_name"],
            last_name=data["last_name"],
            birth_date=birth_date,
            chess_id=data["chess_id"],
            score=data.get("score", 0.0)
        )
