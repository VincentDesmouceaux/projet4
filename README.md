# 🎉 Gestionnaire de Tournoi d'Échecs 🏆

Bienvenue dans le Gestionnaire de Tournoi d'Échecs, une application complète conçue pour gérer les tournois d'échecs de manière fluide. Ce projet vous permet de créer, lancer et générer des rapports sur les tournois d'échecs avec facilité.

---

## 📜 Table des Matières

- [Introduction](#introduction)
- [Fonctionnalités](#fonctionnalités)
- [Installation](#installation)
- [Utilisation](#utilisation)
  - [Créer un Nouveau Tournoi](#créer-un-nouveau-tournoi)
  - [Lancer un Tournoi Existant](#lancer-un-tournoi-existant)
  - [Générer des Rapports](#générer-des-rapports)
- [Structure des Fichiers](#structure-des-fichiers)
- [Contribution](#contribution)
- [Licence](#licence)

---

## 🌟 Introduction

Le Gestionnaire de Tournoi d'Échecs est conçu pour aider les organisateurs à gérer efficacement les tournois d'échecs. L'application fournit des fonctionnalités pour créer des tournois, ajouter des joueurs, exécuter des matchs et générer des rapports détaillés.

---

## 🚀 Fonctionnalités

- **Créer des Tournois:** Configurez facilement de nouveaux tournois avec des détails comme le nom, le lieu, les dates et les joueurs.
- **Lancer des Tournois:** Exécutez des tours et des matchs automatiquement avec des résultats de match aléatoires.
- **Générer des Rapports:** Produisez des rapports détaillés en formats texte et HTML, incluant les classements des joueurs et les résultats des matchs.
- **Interface Conviviale:** Interface simple et intuitive pour une interaction facile.

---

## 🛠️ Installation

### Prérequis

- Python 3.x
- Git

### Étapes

1. **Cloner le Répertoire**
   
   git clone https://github.com/VincentDesmouceaux/projet4.git
   cd projet4
2. **Créer un Environnement Virtuel**
   
   python3 -m venv venv
   source venv/bin/activate   # Sur Windows: venv\Scripts\activate

3. **Installer les Dépendances**
   
   pip install -r requirements.txt

## 📖 Utilisation

### Créer un Nouveau Tournoi

1. Exécutez l'application :
   ```sh
   python src/main.py

2. Suivez les instructions à l'écran :

    Sélectionnez "Créer un Nouveau Tournoi".
    Entrez les détails du tournoi : nom, lieu, dates de début et de fin, nombre de tours, et description.
    Entrez les détails des joueurs pour chaque joueur (au moins 4 joueurs).

### Lancer un Tournoi Existant

1. Exécutez l'application :

    python src/main.py

2. Sélectionnez "Lancer un Tournoi Existant".

    Choisissez le tournoi que vous souhaitez lancer dans la liste.
    L'application simulera les tours et les matchs, affichant les résultats.

### Générer des Rapports

1. Exécutez l'application :

    python src/main.py

2. Sélectionnez "Consulter les Rapports".

    Choisissez le type de rapport que vous souhaitez générer.
    Optionnellement, exportez le rapport en format texte ou HTML.

## 📂 Structure des Fichiers


    ├── src
    │   ├── controllers
    │   │   ├── application_controller.py
    │   │   ├── report_manager.py
    │   │   ├── tournament_manager.py
    │   │   └── user_manager.py
    │   ├── models
    │   │   ├── match.py
    │   │   ├── player.py
    │   │   ├── round.py
    │   │   └── tournament.py
    │   ├── views
    │   │   ├── menu_view.py
    │   │   ├── player_view.py
    │   │   ├── report_view.py
    │   │   └── tournament_view.py
    │   ├── data
    │   │   └── tournaments.json
    │   ├── rapports
    │   │   └── (Rapports Générés)
    │   └── main.py
    ├── .gitignore
    ├── README.md
    ├── requirements.txt

## 🤝 Contribution

    Les contributions sont les bienvenues ! Voici comment vous pouvez aider :

    Signaler des Bugs: Si vous rencontrez des problèmes, veuillez les signaler sur le suivi des problèmes de GitHub.
    Soumettre des Pull Requests: Si vous avez une correction ou une amélioration, n'hésitez pas à soumettre une pull request.
    Suggérer des Fonctionnalités: Vous avez une idée de nouvelle fonctionnalité ? Faites-le nous savoir !


Merci d'utiliser le Gestionnaire de Tournoi d'Échecs ! Si vous avez des questions ou des retours, n'hésitez pas à nous contacter. Bonne organisation ! 🎉
