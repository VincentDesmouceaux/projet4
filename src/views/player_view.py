def get_player_data():
    """
    Demande à l'utilisateur de saisir les détails d'un nouveau joueur.
    
    Returns:
        dict: Un dictionnaire contenant les informations du joueur.
    """
    print("Enter player details:")
    first_name = input("First Name: ")
    last_name = input("Last Name: ")
    birth_date = input("Birth Date (YYYY-MM-DD): ")
    return {'first_name': first_name, 'last_name': last_name, 'birth_date': birth_date}

def display_players(players):
    """
    Affiche une liste de joueurs.
    
    Args:
        players (list of dict): Une liste de dictionnaires, chaque dictionnaire contenant les détails d'un joueur.
    """
    print("List of Players:")
    for player in players:
        print(f"{player['chess_id']}: {player['first_name']} {player['last_name']}, DOB: {player['birth_date']}")

def update_player_view():
    """
    Demande à l'utilisateur les détails pour mettre à jour un joueur existant.
    
    Returns:
        tuple: Le Chess ID du joueur à mettre à jour et un dictionnaire des nouvelles valeurs.
    """
    chess_id = input("Enter Chess ID of the player to update: ")
    print("Enter new details (leave blank to keep current):")
    first_name = input("First Name: ")
    last_name = input("Last Name: ")
    birth_date = input("Birth Date (YYYY-MM-DD): ")
    return chess_id, {'first_name': first_name, 'last_name': last_name, 'birth_date': birth_date}
