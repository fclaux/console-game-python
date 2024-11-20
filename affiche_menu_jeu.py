import os

def affiche_menu_jeu(nom_jeu : str):
    """Cette procédure affiche un menu en fonction du nom du jeu

    Args:
        nom_jeu (str): nom du jeu (idéalement de 13 caractères pour ne pas décaler le "|")
    """
    os.system("CLS")
    print(" _____________________________________________________________________________")
    print("|                                                                             |")
    print("|                               ",nom_jeu,"                               |")
    print("|                                                                             |")
    print("|                           - 1) Joueur contre Joueur                         |")
    print("|                           - 2) Joueur contre Ordinateur                     |")
    print("|                           - 3) Ordinateur contre Ordinateur                 |")
    print("|                           - 4) Règles                                       |")
    print("|                           - 5) Menu principal                               |")
    print("|_____________________________________________________________________________|")
    print("")
