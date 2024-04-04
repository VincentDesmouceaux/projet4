from dataclasses import dataclass, field
from typing import List
import datetime
from .round import Round
from .player import Player

@dataclass
class Tournament:
    """
    Représente un tournoi d'échecs, contenant des informations sur le tournoi lui-même et les tours/matchs/joueurs impliqués.

    Attributs :
        name (str): Nom du tournoi.
        location (str): Lieu du tournoi.
        start_date (datetime.date): Date de début du tournoi.
        end_date (datetime.date): Date de fin du tournoi.
        rounds (List[Round]): Liste des tours dans le tournoi.
        players (List[Player]): Liste des joueurs participants au tournoi.
        description (str): Description générale ou commentaires sur le tournoi.
        current_round (int): Numéro du tour actuel; par défaut à 0.

    Méthodes :
        add_round(round_: Round): Ajoute un tour à la liste des tours du tournoi.
        add_player(player: Player): Ajoute un joueur à la liste des joueurs du tournoi.

    """
    name: str
    location: str
    start_date: datetime.date
    end_date: datetime.date
    description: str = ''  # Valeur par défaut ajoutée ici
    rounds: List[Round] = field(default_factory=list)
    players: List[Player] = field(default_factory=list)
    current_round: int = 0


    def add_round(self, round_: Round):
        self.rounds.append(round_)
        self.current_round += 1

    def add_player(self, player: Player):
        self.players.append(player)

    def __str__(self):
        players_str = ", ".join(str(player) for player in self.players)
        rounds_str = "\n    ".join(str(round) for round in self.rounds)
        return f'''Tournament: {self.name}, Location: {self.location}, Dates: {self.start_date} to {self.end_date}
Description: {self.description}
Players: {players_str}
Rounds:
    {rounds_str}'''