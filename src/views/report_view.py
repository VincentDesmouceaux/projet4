def display_all_players_alphabetically(players):
    print("\n" + "=" * 40)
    print("Liste de tous les joueurs par ordre alphabétique")
    print("=" * 40)
    for player in sorted(players, key=lambda x: (x.last_name, x.first_name)):
        print(f"- {player.first_name} {player.last_name}")
    print("=" * 40 + "\n")


def display_all_tournaments(tournaments):
    print("\n" + "=" * 40)
    print("Liste de tous les tournois")
    print("=" * 40)
    for tournament in tournaments:
        print(f"- {tournament.name} - {tournament.location}")
        print(f"  Du {tournament.start_date} au {tournament.end_date}")
        print("-" * 40)
    print("=" * 40 + "\n")


def display_tournament_details(tournament):
    print("\n" + "=" * 40)
    print(f"Nom du Tournoi: {tournament.name}")
    print(f"Lieu: {tournament.location}")
    print(f"Dates: Du {tournament.start_date} au {tournament.end_date}")
    print(f"Nombre de tours prévus: {tournament.number_of_rounds}")
    print(f"Description: {tournament.description}")
    print("=" * 40 + "\n")


def display_tournament_players_alphabetically(tournament):
    print("\n" + "=" * 40)
    print(f"Liste des joueurs du tournoi {tournament.name} par ordre alphabétique")
    print("=" * 40)
    sorted_players = sorted(tournament.players, key=lambda x: (x.last_name, x.first_name))
    for player in sorted_players:
        print(f"- {player.first_name} {player.last_name}")
    print("=" * 40 + "\n")


def display_tournament_rounds_and_matches(tournament):
    print("\n" + "=" * 40)
    print(f"Rapport des tours et matchs pour le tournoi: {tournament.name}")
    print("=" * 40)
    for round in tournament.rounds:
        print(f"\nTour: {round.name}")
        for match in round.matches:
            print(f"- {match.players[0]} vs {match.players[1]} - Score: {match.score}")
    print("=" * 40 + "\n")
