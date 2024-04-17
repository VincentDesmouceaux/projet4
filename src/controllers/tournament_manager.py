import json
from pathlib import Path

class TournamentManager:
    """
    Gère les interactions avec les données de tournois stockées dans un fichier JSON.
    Permet de manipuler des informations sur les tournois et les joueurs inscrits à ces tournois.

    Attributes:
        filepath (Path): Le chemin du fichier JSON où les tournois sont stockés.
        tournaments (list of dict): La liste des tournois chargés depuis le fichier JSON.
    """

    def __init__(self, filepath):
        """
        Initialise le TournamentManager avec le chemin du fichier JSON.
        Args:
            filepath (str): Le chemin vers le fichier JSON contenant les données des tournois.
        """
        self.filepath = Path(filepath)
        self.tournaments = self.load_tournaments()

    def load_tournaments(self):
        """
        Charge les données des tournois à partir du fichier JSON spécifié lors de l'initialisation.
        Returns:
            list of dict: Une liste des tournois avec leurs détails et joueurs.
        """
        if not self.filepath.exists():
            return []  # Retourne une liste vide si le fichier n'existe pas
        with open(self.filepath, 'r', encoding='utf-8') as file:
            data = json.load(file)
            return data.get('tournaments', [])

    def save_tournaments(self):
        """
        Sauvegarde l'état actuel des tournois dans le fichier JSON.
        Cette méthode écrit les modifications apportées aux tournois dans le fichier,
        assurant la persistance des données entre les sessions.
        """
        with open(self.filepath, 'w', encoding='utf-8') as file:
            json.dump({'tournaments': self.tournaments}, file, ensure_ascii=False, indent=4)

    def get_tournament_names(self):
        """
        Récupère les noms de tous les tournois chargés.
        Returns:
            list of str: Liste des noms de tous les tournois.
        """
        return [tournament['name'] for tournament in self.tournaments]

    def get_tournament_details(self, tournament_name):
        """
        Récupère les détails d'un tournoi spécifique par son nom, insensible à la casse.

        Args:
            tournament_name (str): Le nom du tournoi dont on souhaite obtenir les détails.
        """
        normalized_name = tournament_name.strip().lower()
        for tournament in self.tournaments:
            if tournament['name'].lower() == normalized_name:
                return tournament
        raise ValueError(f"No tournament found with the name {tournament_name}")

    def run_tournament(self, tournament_name):
        """
        Exécute les activités liées au tournoi sélectionné.
        
        Args:
            tournament_name (str): Le nom du tournoi à lancer.

        Raises:
            ValueError: Si aucun tournoi correspondant au nom fourni n'est trouvé.
        """
        tournament = self.get_tournament_details(tournament_name)
        if not tournament:
            raise ValueError(f"No tournament found with the name {tournament_name}")

        # Ici, tu pourrais ajouter la logique pour démarrer le tournoi, par exemple:
        print(f"Le tournoi '{tournament_name}' commence !")
        # Affiche des informations sur le tournoi, les matchs programmés, etc.
        # Par exemple:
        print(f"Tournoi: {tournament['name']} à {tournament['location']} du {tournament['start_date']} au {tournament['end_date']}")
        print("Participants:")
        for player in tournament.get('players', []):
            print(f"- {player['first_name']} {player['last_name']}")
