"""
Module de vue pour afficher les rapports des tournois et des joueurs.
"""


def display_all_players_alphabetically(players, styled=True):
    """
    Affiche la liste de tous les joueurs par ordre alphabétique.

    Args:
        players (list): Liste des objets Player.
        styled (bool): Indique si le texte doit être stylisé pour le terminal.
    """
    bold_start, bold_end = ("\033[1m", "\033[0m") if styled else ("", "")

    print("\n" + "=" * 40)
    print(f"{bold_start}Liste de tous les joueurs par ordre alphabétique{bold_end}")
    print("=" * 40)
    for player in sorted(players, key=lambda x: (x.first_name, x.last_name)):
        print(f"- {player.first_name} {player.last_name}")
    print("=" * 40 + "\n")


def display_all_tournaments(tournaments, styled=True):
    """
    Affiche la liste de tous les tournois.

    Args:
        tournaments (list): Liste des objets Tournament.
        styled (bool): Indique si le texte doit être stylisé pour le terminal.
    """
    bold_start, bold_end = ("\033[1m", "\033[0m") if styled else ("", "")

    print("\n" + "=" * 40)
    print(f"{bold_start}Liste de tous les tournois{bold_end}")
    print("=" * 40)
    for tournament in tournaments:
        print(f"{bold_start}- {tournament.name}{bold_end} - {tournament.location}")
        print(f"  Du {tournament.start_date} au {tournament.end_date}")
        print("-" * 40)
    print("=" * 40 + "\n")


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
    for player in sorted(tournament.players, key=lambda x: (x.first_name, x.last_name)):
        print(f"- {player.first_name} {player.last_name}")
    print("=" * 40 + "\n")


def display_tournament_players_alphabetically(tournament, styled=True):
    """
    Affiche la liste des joueurs d'un tournoi par ordre alphabétique.

    Args:
        tournament (Tournament): Un objet Tournament.
        styled (bool): Indique si le texte doit être stylisé pour le terminal.
    """
    bold_start, bold_end = ("\033[1m", "\033[0m") if styled else ("", "")

    print("\n" + "=" * 40)
    print(f"{bold_start}Liste des joueurs du tournoi {tournament.name} par ordre alphabétique{bold_end}")
    print("=" * 40)
    sorted_players = sorted(tournament.players, key=lambda x: (x.first_name, x.last_name))
    for player in sorted_players:
        print(f"- {player.first_name} {player.last_name}")
    print("=" * 40 + "\n")


def display_tournament_rounds_and_matches(tournament, styled=True):
    """
    Affiche tous les tours et matchs d'un tournoi.

    Args:
        tournament (Tournament): Un objet Tournament.
        styled (bool): Indique si le texte doit être stylisé pour le terminal.
    """
    bold_start, bold_end = ("\033[1m", "\033[0m") if styled else ("", "")

    print("\n" + "=" * 40)
    print(f"{bold_start}Rapport des tours et matchs pour le tournoi: {tournament.name}{bold_end}")
    print("=" * 40)
    for round in tournament.rounds:
        print("\n" + "-" * 40)
        print(f"{bold_start}Tour: {round.name}{bold_end}")
        print("-" * 40)
        for match in round.matches:
            print(f"- {match.players[0].first_name} {match.players[0].last_name} vs {
                  match.players[1].first_name} {match.players[1].last_name} - Score: {match.score}")
    print("=" * 40 + "\n")
