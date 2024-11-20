import os

def affiche_regles_devinettes(): 
    """Cette procédure affiche les règles du jeu des devinettes
    """
    os.system("CLS")
    print(" _____________________________________________________________________________")
    print("|                                                                             |")
    print("|                            Règles du Devin'ombre                            |")
    print("|                                                                             |")
    print("| - Le joueur 1 choisi un nombre entre 1 et une limite que vous déciderez     |")
    print("| - Le joueur 2 doit deviner ce nombre en entrant un choix                    |")
    print("| - A chacun de ses propostions, le joueur 1 répond \"trop petit\", \"trop grand\"|")
    print("|   ou \"c'est gagné\" (Attention à bien respecter la casse !)                  |")
    print("|                                                                             |")
    print("|_____________________________________________________________________________|\n")
    print("")
    input("Appuyer sur entrer pour revenir au menu")

def affiche_regles_allumettes(): 
    """Cette procédure affiche les règles du jeu des allumettes
    """
    os.system("CLS")
    print(" _____________________________________________________________________________")
    print("|                                                                             |")
    print("|                       Règles du jeu des allumettes                          |")
    print("|                                                                             |")
    print("| - Vous disposez d'un tas de 20 allumettes                                   |")
    print("| - Chaque joueur, à tour de rôle, peut en prélever 1, 2 ou 3                 |")
    print("| - Le perdant est celui qui prend la dernière allumette                      |")
    print("|                                                                             |")
    print("|_____________________________________________________________________________|\n")
    print("")
    input("Appuyer sur entrer pour revenir au menu")

def affiche_regles_morpion(): 
    """Cette procédure affiche les règles du morpion
    """
    os.system("CLS")
    print(" _____________________________________________________________________________")
    print("|                                                                             |")
    print("|                          Règles du Morpion                                  |")
    print("|                                                                             |")
    print("| - Chaque joueur pose sa marque (un O ou une X) à tour de rôle               |")
    print("| - Pour cela vous disposez d'une grille de 3x3                               |")
    print("| - Le premier qui aligne 3 marques a gagné                                   |")
    print("|                                                                             |")
    print("|_____________________________________________________________________________|\n")
    print("")
    input("Appuyer sur entrer pour revenir au menu")

def affiche_regles_puissance4():
    """Cette procédure affiche les règles du puissance 4
    """
    os.system("CLS")
    print(" _____________________________________________________________________________")
    print("|                                                                             |")
    print("|                          Règles du puissance 4                              |")
    print("|                                                                             |")
    print("| - Chaque joueur possède des jetons de sa couleur                            |")
    print("| - A tour de rôle, un joueur inssère un jeton dans la colonne de son choix   |")
    print("| - Pour cela, vous disposez d'une grille de 6 rangées et 7 colonnes          |")
    print("| - Le jeton tombe en bas de la colonne                                       |")
    print("| - Le premier qui aligne 4 pions de même couleur gagne                       |")
    print("|                                                                             |")
    print("|_____________________________________________________________________________|\n")
    print("")
    input("Appuyer sur entrer pour revenir au menu")