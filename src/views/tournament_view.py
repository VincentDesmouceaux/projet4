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
        print(f"{green_start}{player1.first_name} {player1.last_name} a remporté la partie et gagne un point.{green_end}")
    elif choice == '3':
        match.score = (0, 1)
        print(f"{green_start}{player2.first_name} {player2.last_name} a remporté la partie et gagne un point.{green_end}")
    elif choice == '4':
        tournament_manager.save_tournaments()
        print(f"{red_start}Tournoi mis en pause et sauvegardé. À bientôt!{red_end}")
        exit(0)
    else:
        print(f"{red_start}Choix invalide, veuillez réessayer.{red_end}")
        return display_match_result(match, tournament_manager)

    match.update_player_scores()


def display_round_details(round, tournament_manager, styled=True):
    """
    Affiche les détails d'un tour spécifique.

    Args:
        round (Round): Un objet Round.
        tournament_manager (TournamentManager): Le gestionnaire de tournois pour permettre la pause et la sauvegarde.
        styled (bool): Indique si le texte doit être stylisé pour le terminal.
    """
    bold_start, bold_end = ("\033[1m", "\033[0m") if styled else ("", "")

    print("\n" + "=" * 40)
    print(f"{bold_start}-- {round.name} --{bold_end}")
    print(f"Commencé à: {round.start_time.strftime('%Y-%m-%d %H:%M:%S')}")
    if round.end_time:
        print(f"Terminé à: {round.end_time.strftime('%Y-%m-%d %H:%M:%S')}")
    else:
        print("En cours")
    print("-" * 40)
    for match in round.matches:
        display_match_result(match, tournament_manager)
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
