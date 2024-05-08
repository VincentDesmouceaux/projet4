def display_all_players_alphabetically(players):
    print("Liste de tous les joueurs par ordre alphabétique:")
    for player in sorted(players, key=lambda x: (x.last_name, x.first_name)):
        print(f"{player.first_name} {player.last_name}")


def display_all_tournaments(tournaments):
    print("Liste de tous les tournois:")
    for tournament in tournaments:
        print(f"{tournament.name} - {tournament.location} - Du {tournament.start_date} au {tournament.end_date}")


def display_tournament_details(tournament):
    print(f"\nNom du Tournoi: {tournament.name}")
    print(f"Lieu: {tournament.location}")
    print(f"Dates: Du {tournament.start_date} au {tournament.end_date}")
    print(f"Nombre de tours prévus: {tournament.number_of_rounds}")
    print(f"Description: {tournament.description}")


def display_tournament_players_alphabetically(tournament):
    print(f"\nListe des joueurs du tournoi {tournament.name} par ordre alphabétique:")
    sorted_players = sorted(tournament.players, key=lambda x: (x.last_name, x.first_name))
    for player in sorted_players:
        print(f"{player.first_name} {player.last_name}")


def display_tournament_rounds_and_matches(tournament):
    print(f"\nRapport des tours et matchs pour le tournoi: {tournament.name}")
    for round in tournament.rounds:
        print(f"\nTour: {round.name}")
        for match in round.matches:
            print(f"{match.players[0]} vs {match.players[1]} - Score: {match.score}")
