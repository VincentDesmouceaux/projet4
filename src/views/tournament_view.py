"""
Module de vue pour afficher les informations des tournois, des tours et des scores.

Ce module contient des fonctions pour afficher les détails d'un tournoi, les détails d'un tour spécifique, 
les scores finaux d'un tournoi et pour obtenir les informations nécessaires à la création d'un nouveau tournoi.
"""


def display_tournament_details(tournament):
    """
    Affiche les détails d'un tournoi spécifique.

    Args:
        tournament (Tournament): Un objet Tournament.
    """
    print("\n" + "=" * 40)
    print(f"\033[1mNom du Tournoi:\033[0m {tournament.name}")
    print(f"\033[1mLieu:\033[0m {tournament.location}")
    print(f"\033[1mDates:\033[0m Du {tournament.start_date} au {tournament.end_date}")
    print(f"\033[1mNombre de tours prévus:\033[0m {tournament.number_of_rounds}")
    print(f"\033[1mDescription:\033[0m {tournament.description}")
    print("\033[1mListe des joueurs:\033[0m")
    # Trier les joueurs par prénom et nom de famille
    for player in sorted(tournament.players, key=lambda x: (x.first_name, x.last_name)):
        print(f"- {player.first_name} {player.last_name}")
    print("=" * 40 + "\n")


def display_round_details(round):
    """
    Affiche les détails d'un tour spécifique.

    Args:
        round (Round): Un objet Round.
    """
    print("\n" + "=" * 40)
    print(f"\033[1m-- {round.name} --\033[0m")
    print(f"Commencé à: {round.start_time.strftime('%Y-%m-%d %H:%M:%S')}")
    print(f"Terminé à: {round.end_time.strftime('%Y-%m-%d %H:%M:%S')}")
    print("-" * 40)
    # Afficher les détails de chaque match dans le tour
    for match in round.matches:
        print(f"{match.players[0].first_name} {match.players[0].last_name} vs {
              match.players[1].first_name} {match.players[1].last_name} - Score: {match.score}")
    print("-" * 40 + "\n")


def display_final_scores(tournament):
    """
    Affiche les scores finaux d'un tournoi.

    Args:
        tournament (Tournament): Un objet Tournament.
    """
    print("\n" + "=" * 40)
    print("\033[1m=== Résultats Finaux ===\033[0m")
    # Trier les joueurs par score décroissant
    final_scores = sorted(tournament.players, key=lambda p: p.score, reverse=True)
    for player in final_scores:
        print(f"{player.first_name} {player.last_name}: {player.score} points")
    print("=" * 40 + "\n")


def get_tournament_data():
    """
    Demande à l'utilisateur de saisir les détails d'un nouveau tournoi.

    Returns:
        dict: Un dictionnaire contenant les informations du tournoi.
    """
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
