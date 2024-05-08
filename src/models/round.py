from dataclasses import dataclass, field
from typing import List
import datetime
from .match import Match


@dataclass
class Round:
    """
    Classe représentant un tour dans un tournoi d'échecs, contenant plusieurs matchs.

    Attributes:
        name (str): Nom du tour.
        start_time (datetime.datetime): Heure de début du tour.
        end_time (datetime.datetime): Heure de fin du tour.
        matches (List[Match]): Liste des matchs joués pendant ce tour.
    """

    name: str
    matches: List[Match] = field(default_factory=list)
    start_time: datetime.datetime = None
    end_time: datetime.datetime = None

    def start_round(self):
        """
        Marque le début du tour en enregistrant l'heure actuelle.
        """
        self.start_time = datetime.datetime.now()

    def end_round(self):
        """
        Marque la fin du tour en enregistrant l'heure actuelle.
        """
        self.end_time = datetime.datetime.now()

    def add_match(self, match: Match):
        """
        Ajoute un match à la liste des matchs de ce tour et le joue.
        """
        self.matches.append(match)
        match.play_match()

    def __str__(self):
        round_details = (
            f"{self.name} - Start: {self.start_time}, End: {self.end_time}\n"
        )
        if self.matches:
            for match in self.matches:
                round_details += str(match) + "\n"
        else:
            round_details += "No matches played yet."
        return round_details

    def as_dict(self):
        return {
            "name": self.name,
            "matches": [match.as_dict() for match in self.matches],
            "start_time": self.start_time.isoformat() if self.start_time else None,
            "end_time": self.end_time.isoformat() if self.end_time else None
        }
