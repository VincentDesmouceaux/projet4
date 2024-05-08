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
