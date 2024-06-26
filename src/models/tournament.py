from dataclasses import dataclass, field
from typing import List
import datetime
from .round import Round
from .player import Player


@dataclass
class Tournament:
    """
    Représente un tournoi d'échecs.

    Attributes:
        name (str): Le nom du tournoi.
        location (str): Le lieu du tournoi.
        start_date (datetime.date): La date de début du tournoi.
        end_date (datetime.date): La date de fin du tournoi.
        description (str): La description du tournoi.
        number_of_rounds (int): Le nombre de tours dans le tournoi.
        rounds (List[Round]): La liste des tours du tournoi.
        players (List[Player]): La liste des joueurs du tournoi.
        current_round (int): Le tour en cours.
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
        Ajoute un tour au tournoi.

        Args:
            round (Round): Le tour à ajouter.

        Raises:
            ValueError: Si le nombre de tours dépasse le nombre spécifié.
        """
        if len(self.rounds) < self.number_of_rounds:
            self.rounds.append(round)
        else:
            raise ValueError("Cannot add more rounds than specified")

    def get_current_round(self):
        """
        Retourne le tour en cours ou un nouveau tour si tous les tours sont terminés.

        Returns:
            Round: Le tour en cours ou None si tous les tours sont terminés.
        """
        if not self.rounds:
            return None

        current_round = self.rounds[-1]
        if current_round.is_completed():
            if len(self.rounds) < self.number_of_rounds:
                return None
            else:
                return current_round

        return current_round

    def get_current_match(self):
        """
        Retourne le match en cours ou None si tous les matchs sont terminés.

        Returns:
            Match: Le match en cours ou None si tous les matchs sont terminés.
        """
        current_round = self.get_current_round()
        if not current_round:
            return None

        return current_round.get_current_match()

    def __str__(self):
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
        Convertit l'objet Tournament en dictionnaire.

        Returns:
            dict: Le dictionnaire représentant le tournoi.
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
        Crée un objet Tournament à partir d'un dictionnaire.

        Args:
            data (dict): Le dictionnaire contenant les données du tournoi.

        Returns:
            Tournament: L'objet Tournament créé.
        """
        start_date = datetime.datetime.strptime(data["start_date"], "%Y-%m-%d").date()
        end_date = datetime.datetime.strptime(data["end_date"], "%Y-%m-%d").date()
        players = [Player.from_dict(p_data) for p_data in data["players"]]
        rounds = [Round.from_dict(r_data) for r_data in data.get("rounds", [])]
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
