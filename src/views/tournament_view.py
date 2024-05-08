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
    print(f"\n\n-- {round.name} --")
    print(f"Commencé à: {round.start_time.strftime('%Y-%m-%d %H:%M:%S')}")
    print(f"Terminé à: {round.end_time.strftime('%Y-%m-%d %H:%M:%S')}\n")
    for match in round.matches:
        print(f"{match.players[0].first_name} {match.players[0].last_name} vs {
              match.players[1].first_name} {match.players[1].last_name} - Score: {match.score}")
    print("-- Fin du tour --\n")


def display_final_scores(tournament):
    print("\n\n=== Résultats Finaux ===")
    final_scores = sorted(tournament.players, key=lambda p: p.score, reverse=True)
    for player in final_scores:
        print(f"{player.first_name} {player.last_name}: {player.score} points")
    print("========================\n\n")


def get_tournament_data():
    print("Entrez les détails du tournoi:")
    name = input("Nom du tournoi: ")
    location = input("Lieu: ")
    start_date = input("Date de début (YYYY-MM-DD): ")
    end_date = input("Date de fin (YYYY-MM-DD): ")
    number_of_rounds = int(input("Nombre de tours: "))
    description = input("Description: ")
    return {
        "name": name,
        "location": location,
        "start_date": start_date,
        "end_date": end_date,
        "number_of_rounds": number_of_rounds,
        "current_round": 0,
        "description": description
    }
