"""
Point d'entrée principal de l'application de gestion de tournoi d'échecs.

Ce fichier initialise et démarre le contrôleur de l'application qui gère l'ensemble du flux de travail.
"""

from controllers.application_controller import ApplicationController


def main():
    """
    Fonction principale de l'application.

    Cette fonction initialise le contrôleur de l'application avec le chemin du fichier de données des tournois
    et démarre l'application.
    """
    # Initialiser le contrôleur de l'application avec le chemin vers le fichier JSON des tournois
    app_controller = ApplicationController('src/data/tournaments.json')
    # Démarrer l'application
    app_controller.start()


if __name__ == '__main__':
    # Vérifier si ce script est exécuté directement (et non importé)
    main()
