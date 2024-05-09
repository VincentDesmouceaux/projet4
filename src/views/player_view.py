def get_player_data(player_number):
    """
    Demande à l'utilisateur de saisir les détails d'un nouveau joueur.

    Returns:
        dict: Un dictionnaire contenant les informations du joueur.
    """
    print(f"\n\033[1m\033[4mVeuillez entrer les détails du joueur {player_number}:\033[0m\n")
    first_name = input("Prénom: ")
    last_name = input("Nom: ")
    birth_date = input("Date de naissance (YYYY-MM-DD): ")
    return {'first_name': first_name, 'last_name': last_name, 'birth_date': birth_date}
