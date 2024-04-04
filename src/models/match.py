from dataclasses import dataclass, field
from typing import Tuple
from .player import Player

@dataclass
class Match:
    """
    Représente un match entre deux joueurs dans le tournoi.

    Attributs :
        players (Tuple[Player, Player]): Un tuple contenant les deux joueurs du match.
        score (Tuple[float, float]): Un tuple contenant les scores des joueurs; par défaut à (0.0, 0.0).

    """
    players: Tuple[Player, Player]
    score: Tuple[float, float] = field(default_factory=lambda: (0.0, 0.0))
