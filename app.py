from jeu_devinette import *
from jeu_allumettes import *
from jeu_morpion import *
from jeu_puissance4 import *
from score import *
from structures import *
from fichier import *

def affiche_menu_principal():
    """Cette procédure affiche le menu principal
    """
    print(" _____________________________________________________________________________")
    print("|                                                                             |")
    print("|                   Bienvenue dans les jeux de flo et max                     |")
    print("|                                                                             |")
    print("|                         - 1) Devin'ombre                                    |")
    print("|                         - 2) Allum'ouettes                                  |")
    print("|                         - 3) Morpion                                        |")
    print("|                         - 4) Puissance 4                                    |")
    print("|                         - 5) Scores                                         |")
    print("|                         - 6) Quitter                                        |")
    print("|_____________________________________________________________________________|")
    print("")

if __name__=="__main__":

    score : Jeu
    score = Jeu()
    score.allumettes = []
    score.devinette = []
    score.morpion = []
    score.puissance4 = []
    choix:int


    nom_fichier : str
    nom_fichier = "scores.dat"

    choix=0

    #Gestion du fichier
    score = lire_classe(nom_fichier)
    input("Appuyer sur entrer pour revenir au menu ")
    
    while(choix!=6):
        os.system("CLS")
        affiche_menu_principal()       
        choix=int(input("Saisir votre choix : ")) 
        if choix==1 :
            menu_devinette(score)
        elif choix==2:
            menu_allumettes(score)
        elif choix==3:
            menu_morpion(score)
        elif choix==4:
            menu_puissance4(score)
        elif choix==5:
            scores(score)
        elif choix==6:
            os.system("CLS")
            sauvegarder_classe(score, nom_fichier)
            print("")
            print("Au revoir")
        else :
            print("")
            print("Erreur dans le choix, veuillez entrer un nombre entre 1 et 6\n")
            print("")
            input("Appuyer sur entrer pour modifier votre choix")
            