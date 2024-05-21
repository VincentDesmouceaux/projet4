import re
from datetime import datetime

"""
Module de vue pour afficher les informations des tournois, des tours et des scores.
"""


def display_tournament_details(tournament, styled=True):
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


def display_match_result(match, tournament_manager):
    """
    Affiche le résultat d'un match et permet à l'utilisateur de saisir le score.

    Args:
        match (Match): Le match pour lequel saisir le score.
        tournament_manager (TournamentManager): Le gestionnaire de tournois pour permettre la pause et la sauvegarde.
    """
    player1 = match.players[0]
    player2 = match.players[1]
    bold_start, bold_end = ("\033[1m", "\033[0m")
    blue_start, blue_end = ("\033[94m", "\033[0m")
    green_start, green_end = ("\033[92m", "\033[0m")
    red_start, red_end = ("\033[91m", "\033[0m")
    yellow_start, yellow_end = ("\033[93m", "\033[0m")

    print("\n" + "-" * 40)
    print(f"{bold_start}Match: {blue_start}{player1.first_name} {player1.last_name}{
          blue_end} vs {blue_start}{player2.first_name} {player2.last_name}{blue_end}{bold_end}")
    print("Quel est le résultat ?")
    print(f"{yellow_start}1. Égalité{yellow_end}")
    print(f"{green_start}2. {player1.first_name} {player1.last_name} a gagné{green_end}")
    print(f"{green_start}3. {player2.first_name} {player2.last_name} a gagné{green_end}")
    print(f"{red_start}4. Mettre le tournoi en pause et quitter{red_end}")

    choice = input("Entrez votre choix (1, 2, 3, ou 4) : ")

    if choice == '1':
        match.score = (0.5, 0.5)
        print(f"{yellow_start}Égalité, chaque joueur remporte 0,5 point.{yellow_end}")
    elif choice == '2':
        match.score = (1, 0)
        print(f"{green_start}{player1.first_name} {player1.last_name} remporte la partie, gagne un point.{green_end}")
    elif choice == '3':
        match.score = (0, 1)
        print(f"{green_start}{player2.first_name} {player2.last_name} remporte la partie, gagne un point.{green_end}")
    elif choice == '4':
        tournament_manager.save_tournaments()
        print(f"{red_start}Tournoi mis en pause et sauvegardé. À bientôt!{red_end}")
        exit(0)
    else:
        print(f"{red_start}Choix invalide, veuillez réessayer.{red_end}")
        return display_match_result(match, tournament_manager)

    match.update_player_scores()


def display_round_details(round, tournament_manager, current_match=None, styled=True):
    bold_start, bold_end = ("\033[1m", "\033[0m") if styled else ("", "")
    print("\n" + "=" * 40)
    print(f"{bold_start}-- {round.name} --{bold_end}")
    if round.start_time:
        print(f"Commencé à: {round.start_time.strftime('%Y-%m-%d %H:%M:%S')}")
    else:
        print("Commencé à: N/A")
    if round.end_time:
        print(f"Terminé à: {round.end_time.strftime('%Y-%m-%d %H:%M:%S')}")
    else:
        print("En cours")
    print("-" * 40)

    for match in round.matches:
        player1 = match.players[0]
        player2 = match.players[1]
        if match == current_match:
            display_match_result(match, tournament_manager)
        elif match.score != (0.0, 0.0):
            print(f"Match: {player1.first_name} {player1.last_name} vs {player2.first_name} {player2.last_name}")
            print(f"Résultat: {match.score[0]} - {match.score[1]}")
        else:
            print(f"Match à venir: {player1.first_name} {player1.last_name} vs {
                  player2.first_name} {player2.last_name}")

    print("-" * 40 + "\n")


def display_final_scores(tournament, styled=True):
    bold_start, bold_end = ("\033[1m", "\033[0m") if styled else ("", "")
    print("\n" + "=" * 40)
    print(f"{bold_start}=== Résultats Finaux ==={bold_end}")
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

    def get_validated_input(prompt, validation_func, error_message):
        while True:
            user_input = input(prompt)
            if validation_func(user_input):
                return user_input
            else:
                print(f"\033[91m{error_message}\033[0m")

    def validate_date(date_str):
        try:
            datetime.strptime(date_str, '%Y-%m-%d')
            return True
        except ValueError:
            return False

    def validate_rounds(rounds_str):
        return rounds_str.isdigit() and 1 <= int(rounds_str) <= 4

    def validate_text(text_str):
        return re.match("^[A-Za-zÀ-ÖØ-öø-ÿ ]+$", text_str) is not None

    name = get_validated_input("Nom du tournoi: ", validate_text,
                               "Le nom du tournoi ne doit contenir que des lettres et des espaces.")
    location = get_validated_input("Lieu: ", validate_text, "Le lieu ne doit contenir que des lettres et des espaces.")
    start_date = get_validated_input("Date de début (YYYY-MM-DD): ", validate_date,
                                     "La date de début doit être au format YYYY-MM-DD.")
    end_date = get_validated_input("Date de fin (YYYY-MM-DD): ", validate_date,
                                   "La date de fin doit être au format YYYY-MM-DD.")
    number_of_rounds = get_validated_input("Nombre de tours (1-4): ", validate_rounds,
                                           "Le nombre de tours doit être un entier entre 1 et 4.")
    description = get_validated_input("Description: ", validate_text,
                                      "La description ne doit contenir que des lettres et des espaces.")

    return {
        "name": name,
        "location": location,
        "start_date": start_date,
        "end_date": end_date,
        "number_of_rounds": int(number_of_rounds),
        "current_round": 0,
        "description": description
    }
