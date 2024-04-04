from datetime import date, datetime
from models.player import Player
from models.match import Match
from models.round import Round
from models.tournament import Tournament

# Tester la création de joueur
player1 = Player("John", "Doe", date(1990, 1, 1), "AB12345")
player2 = Player("Jane", "Doe", date(1992, 2, 2), "CD67890")
print(player1)
print(player2)

# Tester la création de match
match = Match((player1, player2), (0.0, 1.0))
print(match)

# Tester la création de round
round = Round("Round 1", datetime.now(), datetime.now())
round.add_match(match)
print(round)

# Tester la création de tournoi
tournament = Tournament("Championnat Local", "Paris", date.today(), date.today(), "Un tournoi très intéressant.")
tournament.add_player(player1)
tournament.add_player(player2)
tournament.add_round(round)
print(tournament)
