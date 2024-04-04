from dataclasses import dataclass
import datetime

@dataclass
class Player:
    """
    Représente un joueur dans le tournoi d'échecs.

    Attributs :
        first_name (str): Prénom du joueur.
        last_name (str): Nom de famille du joueur.
        birth_date (datetime.date): Date de naissance du joueur.
        chess_id (str): Identifiant national d'échecs unique du joueur.

    """
    first_name: str
    last_name: str
    birth_date: datetime.date
    chess_id: str
    
    def __str__(self):
        return f'Player: {self.first_name} {self.last_name}, Birth Date: {self.birth_date}, ID: {self.chess_id}'