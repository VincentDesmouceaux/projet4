# tournament_view.py

from models.tournament import Tournament
from models.player import Player
from models.round import Round

# tournament_view.py


def display_tournament_details(tournament):
    print("\n========================================")
    print(f"Nom du Tournoi: {tournament.name}")
    print(f"Lieu: {tournament.location}")
    print(f"Dates: Du {tournament.start_date} au {tournament.end_date}")
    print(f"Nombre de tours prévus: {tournament.number_of_rounds}")
    print("Description:", tournament.description)
    print("Liste des joueurs:")
    for player in tournament.players:
        print(f"- {player.first_name} {player.last_name}")
    print("========================================\n")


def display_round_details(round):
    print(f"\n-- {round.name} --")
    print(f"Commencé à: {round.start_time.strftime('%Y-%m-%d %H:%M:%S')}")
    print(f"Terminé à: {round.end_time.strftime('%Y-%m-%d %H:%M:%S')}")
    for match in round.matches:
        print(f"{match.players[0]} vs {match.players[1]} - Score: {match.score}")
    print("-- Fin du tour --\n")


def display_final_scores(tournament):
    print("\n=== Résultats Finaux ===")
    final_scores = sorted(tournament.players, key=lambda p: p.score, reverse=True)
    for player in final_scores:
        print(f"{player.first_name} {player.last_name}: {player.score} points")
    print("========================\n")
