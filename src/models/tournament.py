"""
Module pour la gestion des tournois d'échecs.

Ce module contient la classe Tournament qui représente un tournoi d'échecs. La classe permet de gérer
les joueurs, les rounds, et fournit des méthodes pour convertir un tournoi en dictionnaire ou créer
un tournoi à partir d'un dictionnaire.
"""

from dataclasses import dataclass, field
from typing import List
import datetime
from .round import Round
from .player import Player


@dataclass
class Tournament:
    """
    Classe représentant un tournoi d'échecs.

    Attributes:
        name (str): Le nom du tournoi.
        location (str): Le lieu du tournoi.
        start_date (datetime.date): La date de début du tournoi.
        end_date (datetime.date): La date de fin du tournoi.
        description (str): La description du tournoi.
        number_of_rounds (int): Le nombre de tours prévus pour le tournoi.
        rounds (List[Round]): La liste des rounds dans ce tournoi.
        players (List[Player]): La liste des joueurs participant au tournoi.
        current_round (int): Le tour actuel du tournoi.
    """
    name: str
    location: str
    start_date: datetime.date
    end_date: datetime.date
    description: str
    number_of_rounds: int
    rounds: List[Round] = field(default_factory=list)
    players: List[Player] = field(default_factory=list)
    current_round: int = 0

    def add_player(self, player: Player):
        """
        Ajoute un joueur au tournoi.

        Args:
            player (Player): Le joueur à ajouter.
        """
        self.players.append(player)

    def add_round(self, round: Round):
        """
        Ajoute un round au tournoi et incrémente le tour actuel.

        Args:
            round (Round): Le round à ajouter.

        Raises:
            ValueError: Si le nombre de rounds dépasse le nombre de tours spécifié.
        """
        if len(self.rounds) < self.number_of_rounds:
            self.rounds.append(round)
            self.current_round += 1
        else:
            raise ValueError("Cannot add more rounds than specified")

    def __str__(self):
        """
        Retourne une représentation en chaîne de caractères du tournoi.

        Returns:
            str: Représentation du tournoi sous forme de chaîne de caractères.
        """
        players_str = ", ".join(str(player) for player in self.players)
        rounds_str = "\n".join(str(round) for round in self.rounds)
        return (
            f"Tournament: {self.name}, Location: {self.location}, Dates: {self.start_date} to {self.end_date}\n"
            f"Description: {self.description}\n"
            f"Players: {players_str}\n"
            f"Rounds:\n    {rounds_str}"
        )

    def as_dict(self):
        """
        Convertit le tournoi en un dictionnaire.

        Returns:
            dict: Dictionnaire représentant le tournoi avec ses détails.
        """
        return {
            "name": self.name,
            "location": self.location,
            "start_date": self.start_date.isoformat(),
            "end_date": self.end_date.isoformat(),
            "description": self.description,
            "number_of_rounds": self.number_of_rounds,
            "current_round": self.current_round,
            "players": [player.as_dict() for player in self.players],
            "rounds": [round.as_dict() for round in self.rounds]
        }

    @classmethod
    def from_dict(cls, data):
        """
        Crée une instance de Tournament à partir d'un dictionnaire.

        Args:
            data (dict): Dictionnaire contenant les données du tournoi.

        Returns:
            Tournament: Instance de Tournament créée à partir des données fournies.
        """
        start_date = datetime.datetime.strptime(data["start_date"], "%Y-%m-%d").date()
        end_date = datetime.datetime.strptime(data["end_date"], "%Y-%m-%d").date()
        players = [Player.from_dict(p_data) for p_data in data["players"]]
        rounds = [Round.from_dict(r_data) for r_data in data.get("rounds", [])]  # Gérer l'absence de clé 'rounds'
        return cls(
            name=data["name"],
            location=data["location"],
            start_date=start_date,
            end_date=end_date,
            description=data["description"],
            number_of_rounds=data["number_of_rounds"],
            current_round=data.get("current_round", 0),
            players=players,
            rounds=rounds
        )
