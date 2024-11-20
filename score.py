import os
from structures import *
from gestion_tableau import *

def affiche_menu_score():
    """Cette procédure affiche le menu pour les scores
    """
    os.system("CLS")
    print(" _____________________________________________________________________________")
    print("|                                                                             |")
    print("|                 Quel classement souhaitez vous voir :                       |")
    print("|                                                                             |")
    print("|                           - 1) Devin'ombre                                  |")
    print("|                           - 2) Allum'ouettes                                |")
    print("|                           - 3) Morpion                                      |")
    print("|                           - 4) Puissance 4                                  |")
    print("|                           - 5) Menu principal                               |")
    print("|_____________________________________________________________________________|\n")
    print("")

def affiche_score(tab : list[Joueur], unite_score : str, nom_du_jeu : str):
    """
    affiche_score

    Cette procédure affiche les scores en fonctions de l'unité et du jeu

    Args:
        tab (list[Joueur]): le tableau de joueur correspondant au jeu que l'on veut afficher
        unite_score (str): l'unite du score (nombres de victoires, score)
        nom_du_jeu (str): le nom du jeu pour gérer l'affichage
    """
    cpt : int

    if len(tab)<1:
        print("Il n'y pas encore de score d'initialiser pour le",nom_du_jeu)
    else :
        tri_par_insertion(tab)
        print("Classement du",nom_du_jeu)
        print("")

    print("Place\t\t Nom\t\t Score")
    for cpt in range(0, len(tab)):
        print(f"{cpt+1:<6}/\t\t {tab[cpt].nom:<14}\t {tab[cpt].score:>10d}")

def scores(score : Jeu):
    """Cette procédure gère l'affichage du menu des scores et l'accès aux procédures pour chaque jeu

    Args:
        score (Jeu): la classe contenant les scores
    """
    choix : int

    choix = 0

    while(choix!=5):
        os.system("CLS")
        affiche_menu_score()       
        choix=int(input("Saisir votre choix : ")) 
        if choix==1 :
            os.system("CLS")
            affiche_score(score.devinette, "Score", "Devin'ombre")
            print("")
            input("Appuyer sur entrer pour revenir au menu")
        elif choix==2:
            os.system("CLS")
            affiche_score(score.allumettes, "Nombres de victoires", "Allum'ouettes")
            print("")
            input("Appuyer sur entrer pour revenir au menu")
        elif choix==3:
            os.system("CLS")
            affiche_score(score.morpion, "Nombres de victoires", "Morpion")
            print("")
            input("Appuyer sur entrer pour revenir au menu")
        elif choix==4:
            os.system("CLS")
            affiche_score(score.puissance4, "Nombres de victoires", "Puissance 4")
            print("")
            input("Appuyer sur entrer pour revenir au menu")
        elif choix==5:
            #retour au menu
            print()
        else :
            print("")
            print("Erreur dans le choix, veuillez entrer un nombre entre 1 et 5\n")
            print("")
            input("Appuyer sur entrer pour modifier votre choix")
