"""
Module de vue pour afficher les informations des tournois, des tours et des scores.
"""


def display_tournament_details(tournament, styled=True):
    """
    Affiche les détails d'un tournoi spécifique.

    Args:
        tournament (Tournament): Un objet Tournament.
        styled (bool): Indique si le texte doit être stylisé pour le terminal.
    """
    bold_start, bold_end = ("\033[1m", "\033[0m") if styled else ("", "")

    print("\n" + "=" * 40)
    print(f"{bold_start}Nom du Tournoi:{bold_end} {tournament.name}")
    print(f"{bold_start}Lieu:{bold_end} {tournament.location}")
    print(f"{bold_start}Dates:{bold_end} Du {tournament.start_date} au {tournament.end_date}")
    print(f"{bold_start}Nombre de tours prévus:{bold_end} {tournament.number_of_rounds}")
    print(f"{bold_start}Description:{bold_end} {tournament.description}")
    print(f"{bold_start}Liste des joueurs:{bold_end}")
    # Trier les joueurs par prénom et nom de famille
    for player in sorted(tournament.players, key=lambda x: (x.first_name, x.last_name)):
        print(f"- {player.first_name} {player.last_name}")
    print("=" * 40 + "\n")


def display_round_details(round, styled=True):
    """
    Affiche les détails d'un tour spécifique.

    Args:
        round (Round): Un objet Round.
        styled (bool): Indique si le texte doit être stylisé pour le terminal.
    """
    bold_start, bold_end = ("\033[1m", "\033[0m") if styled else ("", "")

    print("\n" + "=" * 40)
    print(f"{bold_start}-- {round.name} --{bold_end}")
    print(f"Commencé à: {round.start_time.strftime('%Y-%m-%d %H:%M:%S')}")
    print(f"Terminé à: {round.end_time.strftime('%Y-%m-%d %H:%M:%S')}")
    print("-" * 40)
    for match in round.matches:
        player1 = match.players[0]
        player2 = match.players[1]
        print(f"{player1.first_name} {player1.last_name} vs {
              player2.first_name} {player2.last_name} - Score: {match.score}")
    print("-" * 40 + "\n")


def display_final_scores(tournament, styled=True):
    """
    Affiche les scores finaux d'un tournoi.

    Args:
        tournament (Tournament): Un objet Tournament.
        styled (bool): Indique si le texte doit être stylisé pour le terminal.
    """
    bold_start, bold_end = ("\033[1m", "\033[0m") if styled else ("", "")

    print("\n" + "=" * 40)
    print(f"{bold_start}=== Résultats Finaux ==={bold_end}")
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
