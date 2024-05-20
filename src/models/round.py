from dataclasses import dataclass, field
from typing import List
import datetime
from .match import Match


@dataclass
class Round:
    """
    Représente un tour dans un tournoi d'échecs.

    Attributes:
        name (str): Le nom du tour.
        matches (List[Match]): La liste des matchs du tour.
        start_time (datetime.datetime): L'heure de début du tour.
        end_time (datetime.datetime): L'heure de fin du tour.
    """
    name: str
    matches: List[Match] = field(default_factory=list)
    start_time: datetime.datetime = None
    end_time: datetime.datetime = None

    def start_round(self, resume=False):
        """
        Démarre le tour.

        Args:
            resume (bool): Indique si le tour est repris.
        """
        if not resume:
            self.start_time = datetime.datetime.now()

    def end_round(self):
        """
        Termine le tour.
        """
        self.end_time = datetime.datetime.now()

    def add_match(self, match: Match):
        """
        Ajoute un match au tour.

        Args:
            match (Match): Le match à ajouter.
        """
        self.matches.append(match)

    def get_current_match(self):
        """
        Retourne le premier match non complété du tour.

        Returns:
            Match: Le premier match non complété ou None si tous les matchs sont terminés.
        """
        for match in self.matches:
            if match.score == (0.0, 0.0):
                return match
        return None

    def has_started(self):
        """
        Vérifie si le tour a commencé.

        Returns:
            bool: True si le tour a commencé, False sinon.
        """
        return self.start_time is not None

    def is_completed(self):
        """
        Vérifie si tous les matchs du tour ont été complétés.

        Returns:
            bool: True si tous les matchs sont complétés, False sinon.
        """
        return all(match.score != (0.0, 0.0) for match in self.matches)

    def __str__(self):
        round_details = f"{self.name} - Start: {self.start_time}, End: {self.end_time}\n"
        if self.matches:
            for match in self.matches:
                round_details += str(match) + "\n"
        else:
            round_details += "No matches played yet."
        return round_details

    def as_dict(self):
        """
        Convertit l'objet Round en dictionnaire.

        Returns:
            dict: Le dictionnaire représentant le tour.
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
        Crée un objet Round à partir d'un dictionnaire.

        Args:
            data (dict): Le dictionnaire contenant les données du tour.

        Returns:
            Round: L'objet Round créé.
        """
        matches = [Match.from_dict(match_data) for match_data in data.get("matches", [])]
        start_time = datetime.datetime.fromisoformat(data["start_time"]) if data["start_time"] else None
        end_time = datetime.datetime.fromisoformat(data["end_time"]) if data["end_time"] else None
        return cls(name=data["name"], matches=matches, start_time=start_time, end_time=end_time)
