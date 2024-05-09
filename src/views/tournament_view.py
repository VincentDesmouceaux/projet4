# tournament_view.py

from models.tournament import Tournament
from models.player import Player
from models.round import Round

# tournament_view.py


def display_tournament_details(tournament):
    print("\n" + "=" * 40)
    print(f"\033[1mNom du Tournoi:\033[0m {tournament.name}")
    print(f"\033[1mLieu:\033[0m {tournament.location}")
    print(f"\033[1mDates:\033[0m Du {tournament.start_date} au {tournament.end_date}")
    print(f"\033[1mNombre de tours prévus:\033[0m {tournament.number_of_rounds}")
    print(f"\033[1mDescription:\033[0m {tournament.description}")
    print("\033[1mListe des joueurs:\033[0m")
    for player in sorted(tournament.players, key=lambda x: (x.first_name, x.last_name)):
        print(f"- {player.first_name} {player.last_name}")
    print("=" * 40 + "\n")


def display_round_details(round):
    print("\n" + "=" * 40)
    print(f"\033[1m-- {round.name} --\033[0m")
    print(f"Commencé à: {round.start_time.strftime('%Y-%m-%d %H:%M:%S')}")
    print(f"Terminé à: {round.end_time.strftime('%Y-%m-%d %H:%M:%S')}")
    print("-" * 40)
    for match in round.matches:
        print(f"{match.players[0].first_name} {match.players[0].last_name} vs {
              match.players[1].first_name} {match.players[1].last_name} - Score: {match.score}")
    print("-" * 40 + "\n")


def display_final_scores(tournament):
    print("\n" + "=" * 40)
    print("\033[1m=== Résultats Finaux ===\033[0m")
    final_scores = sorted(tournament.players, key=lambda p: p.score, reverse=True)
    for player in final_scores:
        print(f"{player.first_name} {player.last_name}: {player.score} points")
    print("=" * 40 + "\n")


def get_tournament_data():
    print("\n\033[1m\033[4mEntrez les détails du tournoi:\033[0m\n")
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
