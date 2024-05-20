import json
from pathlib import Path
from models.tournament import Tournament
from models.round import Round
from models.match import Match
from views.tournament_view import display_tournament_details, display_round_details, display_final_scores


class TournamentManager:
    """
    Gère les opérations liées aux tournois,le chargement, la sauvegarde, la création, et la réinitialisation.

    Attributes:
        filepath (Path): Le chemin vers le fichier JSON contenant les tournois.
        tournaments (list): La liste des tournois.
    """

    def __init__(self, filepath):
        """
        Initialise la classe TournamentManager.

        Args:
            filepath (str): Le chemin vers le fichier JSON contenant les tournois.
        """
        self.filepath = Path(filepath)
        self.tournaments = []
        self.load_tournaments_from_file()

    def load_tournaments_from_file(self):
        """
        Charge les tournois à partir du fichier JSON spécifié.
        """
        if self.filepath.exists():
            with self.filepath.open("r", encoding="utf-8") as file:
                data = json.load(file)
                self.load_tournaments(data.get('tournaments', []))
        else:
            print("No file found, starting with an empty list of tournaments.")

    def load_tournaments(self, tournaments_data):
        """
        Charge les tournois à partir d'une liste de dictionnaires.

        Args:
            tournaments_data (list): La liste des dictionnaires représentant les tournois.
        """
        self.tournaments = [Tournament.from_dict(t_data) for t_data in tournaments_data]

    def save_tournaments(self):
        """
        Sauvegarde les tournois dans le fichier JSON spécifié.
        """
        with self.filepath.open("w", encoding="utf-8") as file:
            json.dump({"tournaments": [t.as_dict() for t in self.tournaments]}, file, indent=4, ensure_ascii=False)

    def get_tournament_details(self, tournament_name):
        """
        Récupère les détails d'un tournoi spécifique.

        Args:
            tournament_name (str): Le nom du tournoi.

        Returns:
            Tournament: Le tournoi correspondant au nom spécifié.

        Raises:
            ValueError: Si aucun tournoi avec le nom spécifié n'est trouvé.
        """
        tournament = next((t for t in self.tournaments if t.name.lower() == tournament_name.lower()), None)
        if not tournament:
            raise ValueError("No tournament found with the name specified.")
        return tournament

    def get_tournament_names(self):
        """
        Récupère les noms de tous les tournois.

        Returns:
            list: La liste des noms de tous les tournois.
        """
        return [tournament.name for tournament in self.tournaments]

    def run_tournament(self, tournament_name, is_resumed=False):
        """
        Exécute un tournoi spécifié, en affichant les détails du tournoi et en gérant chaque tour.

        Args:
            tournament_name (str): Le nom du tournoi à exécuter.
            is_resumed (bool): Indique si le tournoi est repris.
        """
        tournament = self.get_tournament_details(tournament_name)
        display_tournament_details(tournament)

        while tournament.current_round < tournament.number_of_rounds:
            self.run_round(tournament, is_resumed)
            is_resumed = False

        display_final_scores(tournament)
        self.save_tournaments()

        self.prompt_restart_tournament(tournament_name)

    def prompt_restart_tournament(self, tournament_name):
        """
        Demande à l'utilisateur s'il souhaite redémarrer le tournoi.

        Args:
            tournament_name (str): Le nom du tournoi à redémarrer.
        """
        restart_choice = input("Souhaitez-vous redémarrer le tournoi ? (Oui/Non) : ").strip().lower()
        if restart_choice == "oui":
            self.reset_tournament(tournament_name)
            self.run_tournament(tournament_name, is_resumed=False)
        else:
            print("Merci d'avoir utilisé le logiciel de tournoi d'échecs !")

    def run_round(self, tournament, is_resumed):
        """
        Exécute un tour spécifique d'un tournoi.

        Args:
            tournament (Tournament): Le tournoi en cours.
            is_resumed (bool): Indique si le tour est repris.
        """
        current_round_index = tournament.current_round
        round_name = f"Round {current_round_index + 1}"
        round = next((r for r in tournament.rounds if r.name == round_name), None)

        if not round:
            round = Round(name=round_name)
            self.generate_matches(tournament, round)
            round.start_round(resume=is_resumed)
            tournament.add_round(round)

        current_match = round.get_current_match()
        while current_match:
            display_round_details(round, self, current_match=current_match)
            current_match = round.get_current_match()
            self.save_tournaments()

        if not round.is_completed():
            print(f"Round {round_name} is not completed, current_round remains {tournament.current_round}")
            return

        if not round.end_time:
            round.end_round()
            tournament.current_round += 1
        self.save_tournaments()

    def generate_matches(self, tournament, round):
        """
        Génère les matchs pour un tour spécifique d'un tournoi.

        Args:
            tournament (Tournament): Le tournoi en cours.
            round (Round): Le tour en cours.
        """
        from random import shuffle
        shuffle(tournament.players)
        match_id = 1
        for i in range(0, len(tournament.players), 2):
            match = Match(id=match_id, players=(tournament.players[i], tournament.players[i + 1]))
            round.add_match(match)
            match_id += 1

    def get_paused_tournaments(self):
        """
        Récupère la liste des tournois en pause.

        Returns:
            list: La liste des noms des tournois en pause.
        """
        return [t.name for t in self.tournaments if t.current_round > 0 and t.current_round < t.number_of_rounds]

    def reset_all_tournaments(self):
        """
        Réinitialise tous les tournois, en réinitialisant les scores et en supprimant les tours.
        """
        for tournament in self.tournaments:
            tournament.current_round = 0
            tournament.rounds = []
            for player in tournament.players:
                player.score = 0.0
        self.save_tournaments()
        print("Tous les tournois ont été réinitialisés avec succès.")

    def reset_tournament(self, tournament_name):
        """
        Réinitialise un tournoi spécifique, en réinitialisant les scores et en supprimant les tours.

        Args:
            tournament_name (str): Le nom du tournoi à réinitialiser.
        """
        tournament = self.get_tournament_details(tournament_name)
        tournament.current_round = 0
        tournament.rounds = []
        for player in tournament.players:
            player.score = 0.0
        self.save_tournaments()

    def get_all_tournaments(self):
        """
        Récupère tous les tournois.

        Returns:
            list: La liste de tous les tournois.
        """
        return self.tournaments

    def add_tournament(self, tournament_data):
        """
        Ajoute un nouveau tournoi à la liste des tournois et sauvegarde les tournois.

        Args:
            tournament_data (dict): Les données du tournoi à ajouter.
        """
        tournament = Tournament.from_dict(tournament_data)
        self.tournaments.append(tournament)
        self.save_tournaments()
        print(f"Tournament '{tournament.name}' has been added successfully.")
