from dataclasses import dataclass, field
from typing import List
import datetime
from .match import Match

@dataclass
class Round:
    """
    Représente un tour dans le tournoi, composé de plusieurs matchs.

    Attributs :
        name (str): Nom du tour.
        start_time (datetime.datetime): Date et heure de début du tour.
        end_time (datetime.datetime): Date et heure de fin du tour.
        matches (List[Match]): Liste des matchs joués pendant ce tour.

    Méthodes :
        add_match(match: Match): Ajoute un match à la liste des matchs du tour.

    """
    name: str
    start_time: datetime.datetime
    end_time: datetime.datetime
    matches: List[Match] = field(default_factory=list)

    def add_match(self, match: Match):
        self.matches.append(match)

    def __str__(self):
        matches_str = "\n    ".join(str(match) for match in self.matches)
        return f'Round: {self.name}, Start: {self.start_time}, End: {self.end_time}\n    Matches:\n    {matches_str}'    
