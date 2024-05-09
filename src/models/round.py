"""
Module pour la gestion des rounds dans un tournoi d'échecs.
"""

from dataclasses import dataclass, field
from typing import List
import datetime
from .match import Match


@dataclass
class Round:
    """
    Classe représentant un round dans un tournoi d'échecs.

    Attributes:
        name (str): Le nom du round.
        matches (List[Match]): La liste des matchs dans ce round.
        start_time (datetime.datetime): L'heure de début du round.
        end_time (datetime.datetime): L'heure de fin du round.
    """
    name: str
    matches: List[Match] = field(default_factory=list)
    start_time: datetime.datetime = None
    end_time: datetime.datetime = None

    def start_round(self):
        """
        Démarre le round en définissant l'heure de début à l'heure actuelle.
        """
        self.start_time = datetime.datetime.now()

    def end_round(self):
        """
        Termine le round en définissant l'heure de fin à l'heure actuelle.
        """
        self.end_time = datetime.datetime.now()

    def add_match(self, match: Match):
        """
        Ajoute un match au round et joue le match.

        Args:
            match (Match): Le match à ajouter au round.
        """
        self.matches.append(match)
        match.play_match()

    def __str__(self):
        """
        Retourne une représentation en chaîne de caractères du round.

        Returns:
            str: Représentation du round sous forme de chaîne de caractères.
        """
        round_details = f"{self.name} - Start: {self.start_time}, End: {self.end_time}\n"
        if self.matches:
            for match in self.matches:
                round_details += str(match) + "\n"
        else:
            round_details += "No matches played yet."
        return round_details

    def as_dict(self):
        """
        Convertit le round en un dictionnaire.

        Returns:
            dict: Dictionnaire représentant le round avec ses détails.
        """
        return {
            "name": self.name,
            "matches": [match.as_dict() for match in self.matches],
            "start_time": self.start_time.isoformat() if self.start_time else None,
            "end_time": self.end_time.isoformat() if self.end_time else None
        }

    @classmethod
    def from_dict(cls, data):
        """
        Crée une instance de Round à partir d'un dictionnaire.

        Args:
            data (dict): Dictionnaire contenant les données du round.

        Returns:
            Round: Instance de Round créée à partir des données fournies.
        """
        matches = [Match.from_dict(match_data) for match_data in data.get("matches", [])]
        start_time = datetime.datetime.fromisoformat(data["start_time"]) if data["start_time"] else None
        end_time = datetime.datetime.fromisoformat(data["end_time"]) if data["end_time"] else None
        return cls(name=data["name"], matches=matches, start_time=start_time, end_time=end_time)
