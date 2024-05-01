import json
import random
import datetime
from pathlib import Path


class TournamentManager:
    """
    Gère les interactions avec les données de tournois stockées dans un fichier JSON.
    Permet de manipuler des informations sur les tournois et les joueurs inscrits à ces tournois.
    """

    def __init__(self, filepath):
        """
        Initialise le TournamentManager avec le chemin du fichier JSON.
        """
        self.filepath = Path(filepath)
        self.tournaments = self.load_tournaments()

    def load_tournaments(self):
        """
        Charge les données des tournois à partir du fichier JSON spécifié lors de l'initialisation.
        Assure que chaque tournoi a une liste de rounds initialisée.
        """
        if not self.filepath.exists():
            return []  # Retourne une liste vide si le fichier n'existe pas
        with open(self.filepath, "r", encoding="utf-8") as file:
            data = json.load(file)
            tournaments = data.get("tournaments", [])
            for tournament in tournaments:
                if "rounds" not in tournament:
                    tournament["rounds"] = []  # Initialise rounds si non présent
            return tournaments

    def save_tournaments(self):
        """
        Sauvegarde l'état actuel des tournois dans le fichier JSON.
        """
        with open(self.filepath, "w", encoding="utf-8") as file:
            json.dump(
                {"tournaments": self.tournaments}, file, ensure_ascii=False, indent=4
            )

    def get_tournament_names(self):
        """
        Récupère les noms de tous les tournois chargés.
        """
        return [tournament["name"] for tournament in self.tournaments]

    def get_tournament_details(self, tournament_name):
        """
        Récupère les détails d'un tournoi spécifique par son nom, insensible à la casse.
        """
        normalized_name = tournament_name.strip().lower()
        for tournament in self.tournaments:
            if tournament["name"].lower() == normalized_name:
                return tournament
        raise ValueError(f"No tournament found with the name {tournament_name}")

    def run_tournament(self, tournament_name):
        """
        Exécute les activités liées au tournoi sélectionné, y compris les tours et les matchs.
        """
        tournament = self.get_tournament_details(tournament_name)
        if not tournament:
            raise ValueError(f"No tournament found with the name {tournament_name}")

        print(f"Le tournoi '{tournament_name}' commence !")
        print(
            f"Tournoi: {tournament['name']} à {tournament['location']} du {tournament['start_date']} au {tournament['end_date']}"
        )
        print(
            "Description:", tournament.get("description", "Aucune description fournie.")
        )
        print("Participants:")
        for player in tournament["players"]:
            player["score"] = 0  # Initialisation des scores à zéro
            print(f"- {player['first_name']} {player['last_name']}")

        num_rounds = tournament.get("number_of_rounds", 4)
        for round_index in range(num_rounds):
            round_name = f"Round {round_index + 1}"
            print(f"\n{round_name} commence !")
            self.run_round(tournament, round_name)
            self.update_scores(tournament)
            print(f"Fin du {round_name}")

        print("\nFin du tournoi. Résultats finaux:")
        self.display_final_scores(tournament)

    def run_round(self, tournament, round_name):
        """
        Exécute un tour dans le tournoi, génère et exécute les matchs.
        """
        players = tournament["players"]
        random.shuffle(players)  # Mélange aléatoire pour l'appariement
        matches = []
        start_time = datetime.datetime.now()

        for i in range(0, len(players) - 1, 2):
            player1 = players[i]
            player2 = players[i + 1]
            winner = random.choice([0, 1, -1])  # -1 pour un match nul
            if winner == -1:
                score = (0.5, 0.5)
            elif winner == 0:
                score = (1, 0)
            else:
                score = (0, 1)

            match = {"players": [player1, player2], "score": score}
            matches.append(match)
            print(
                f"Match: {player1['first_name']} vs {player2['first_name']}, Score: {score}"
            )

        end_time = datetime.datetime.now()
        tournament["rounds"].append(
            {
                "name": round_name,
                "start_time": start_time,
                "end_time": end_time,
                "matches": matches,
            }
        )
        print(f"{round_name} - Start: {start_time}, End: {end_time}")

    def update_scores(self, tournament):
        """
        Met à jour les scores des joueurs en fonction des résultats des matchs de tous les tours.
        """
        for round in tournament["rounds"]:
            for match in round["matches"]:
                p1, p2 = match["players"]
                s1, s2 = match["score"]
                p1["score"] += s1
                p2["score"] += s2

        print("Mise à jour des scores des joueurs:")
        for player in tournament["players"]:
            print(
                f"{player['first_name']} {player['last_name']}: {player['score']} points"
            )

    def display_final_scores(self, tournament):
        """
        Affiche les scores finaux de tous les joueurs après le dernier tour.
        """
        print("Scores finaux des joueurs:")
        players = sorted(
            tournament["players"], key=lambda x: x.get("score", 0), reverse=True
        )
        for player in players:
            print(
                f"{player['first_name']} {player['last_name']}: {player.get('score', 0)} points"
            )
