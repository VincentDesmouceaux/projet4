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
players_data = load_json_data(Path('src/data/players.json'))['players']
tournaments_data = load_json_data(Path('src/data/tournaments.json'))['tournaments']

# Création des instances de joueurs à partir des données JSON.
players = [Player(**player) for player in players_data]

# Affichage des joueurs pour vérification.
for player in players:
    print(player)

# Supposons qu'un seul tournoi soit défini pour simplifier l'exemple.
tournament_data = tournaments_data[0]

# Création de l'instance du tournoi, initialement sans joueurs.
tournament = Tournament(
    name=tournament_data['name'],
    location=tournament_data['location'],
    start_date=datetime.strptime(tournament_data['start_date'], '%Y-%m-%d').date(),
    end_date=datetime.strptime(tournament_data['end_date'], '%Y-%m-%d').date(),
    description=tournament_data['description']
)

# Associe les joueurs au tournoi en utilisant leurs identifiants.
for player_id in tournament_data['players']:
    # Recherche le joueur par son identifiant et l'ajoute au tournoi si trouvé.
    player = next((player for player in players if player.chess_id == player_id), None)
    if player:
        tournament.add_player(player)

# Pour simplifier, crée un seul match et l'ajoute au tournoi.
match = Match(players=(players[0], players[1]), score=(0.0, 1.0))
round = Round(name="Round 1", start_time=datetime.now(), end_time=datetime.now(), matches=[match])
tournament.add_round(round)

# Affiche les informations du tournoi pour vérification.
print(tournament)
