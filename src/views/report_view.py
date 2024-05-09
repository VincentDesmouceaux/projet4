"""
Module de vue pour afficher les informations des joueurs et des tournois.

"""


def display_all_players_alphabetically(players):
    """
    Affiche tous les joueurs par ordre alphabétique.

    Args:
        players (list): Une liste d'objets Player.
    """
    print("\n" + "=" * 40)
    print("\033[1mListe de tous les joueurs par ordre alphabétique\033[0m")
    print("=" * 40)
    # Trier les joueurs par prénom et nom de famille
    for player in sorted(players, key=lambda x: (x.first_name, x.last_name)):
        print(f"- {player.first_name} {player.last_name}")
    print("=" * 40 + "\n")


def display_all_tournaments(tournaments):
    """
    Affiche tous les tournois avec leur nom et lieu.

    Args:
        tournaments (list): Une liste d'objets Tournament.
    """
    print("\n" + "=" * 40)
    print("\033[1mListe de tous les tournois\033[0m")
    print("=" * 40)
    # Afficher chaque tournoi avec ses détails
    for tournament in tournaments:
        print(f"\033[1m- {tournament.name}\033[0m - {tournament.location}")
        print(f"  Du {tournament.start_date} au {tournament.end_date}")
        print("-" * 40)
    print("=" * 40 + "\n")


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
    print("=" * 40 + "\n")


def display_tournament_players_alphabetically(tournament):
    """
    Affiche les joueurs d'un tournoi par ordre alphabétique.

    Args:
        tournament (Tournament): Un objet Tournament.
    """
    print("\n" + "=" * 40)
    print(f"\033[1mListe des joueurs du tournoi {tournament.name} par ordre alphabétique\033[0m")
    print("=" * 40)
    # Trier les joueurs du tournoi par prénom et nom de famille
    sorted_players = sorted(tournament.players, key=lambda x: (x.first_name, x.last_name))
    for player in sorted_players:
        print(f"- {player.first_name} {player.last_name}")
    print("=" * 40 + "\n")


def display_tournament_rounds_and_matches(tournament):
    """
    Affiche les tours et matchs d'un tournoi.

    Args:
        tournament (Tournament): Un objet Tournament.
    """
    print("\n" + "=" * 40)
    print(f"\033[1mRapport des tours et matchs pour le tournoi: {tournament.name}\033[0m")
    print("=" * 40)
    # Afficher les détails de chaque tour et match du tournoi
    for round in tournament.rounds:
        print("\n" + "-" * 40)
        print(f"\033[1mTour: {round.name}\033[0m")
        print("-" * 40)
        for match in round.matches:
            print(f"- {match.players[0].first_name} {match.players[0].last_name} vs {
                  match.players[1].first_name} {match.players[1].last_name} - Score: {match.score}")
    print("=" * 40 + "\n")
