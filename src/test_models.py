import json
from datetime import datetime
from pathlib import Path
from models.player import Player
from models.match import Match
from models.round import Round
from models.tournament import Tournament

def load_json_data(file_path):
    """
    Charge les données depuis un fichier JSON.
    
    Args:
        file_path (Path): Le chemin du fichier JSON à charger.
        
    Returns:
        dict: Les données chargées depuis le fichier JSON.
    """
    with open(file_path, 'r', encoding='utf-8') as file:
        return json.load(file)

# Chargement des données des joueurs et des tournois à partir de fichiers JSON.

tournaments_data = load_json_data(Path('src/data/tournaments.json'))['tournaments']

# Traitement de chaque tournoi
for tournament_data in tournaments_data:
    # Création des instances de joueurs à partir des données JSON du tournoi
    players = [Player(**player) for player in tournament_data['players']]

    # Création de l'instance du tournoi
    tournament = Tournament(
        name=tournament_data['name'],
        location=tournament_data['location'],
        start_date=datetime.strptime(tournament_data['start_date'], '%Y-%m-%d').date(),
        end_date=datetime.strptime(tournament_data['end_date'], '%Y-%m-%d').date(),
        description=tournament_data['description']
    )

    # Association des joueurs avec le tournoi
    for player in players:
        tournament.add_player(player)

    # Pour simplifier, crée un seul match et l'ajoute au tournoi
    match = Match(players=(players[0], players[1]), score=(0.0, 1.0))
    round = Round(name="Round 1", start_time=datetime.now(), end_time=datetime.now(), matches=[match])
    tournament.add_round(round)

    # Affiche les informations du tournoi pour vérification
    print(tournament)
