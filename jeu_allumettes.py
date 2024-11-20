import os
import random
from structures import *
from regles import affiche_regles_allumettes
from affiche_menu_jeu import *
from gestion_tableau import *


def jeu_allumettesJcJ(score : Jeu):
    """Cette procédure contient l'exécution du jeu des allumettes Joueur contre Joueur

    Args:
        score (Jeu): la variable contenant les scores
    """

    choix_commence_partie:str
    nb_allumettes:int
    retirer_allumettes:int
    cpt:int
    tour:int
    joueur1:str
    joueur2:str
    gagnant : Joueur
    gagnant = Joueur()

    nb_allumettes=20

    print(TextStyle.BOLD + "Bienvenue dans l'Allum'ouettes\n" + TextStyle.RESET)
    print("")

    #Choix des pseudos de chaque joueur avec contrôle de vérification sur la taille et si les pseudos sont identiques
    joueur1=input("Joueur 1 veuillez saisir votre pseudo (12 caractères maximum) : ")
    while len(joueur1)>12:
        joueur1=input("Erreur, veuillez saisir un pseudo de 12 caractères maximum : ")
    print("")
    joueur2=input("Joueur 2 veuillez saisir votre pseudo (12 caractères maximum) : ")
    while len(joueur2)>12 or joueur2==joueur1:
        if len(joueur2)>12:
            joueur2=input("Erreur, veuillez saisir un pseudo de 12 caractères maximum : ")
        else:
            joueur2=input("Erreur, veuillez saisir un pseudo différent du joueur 1 : ")
    print("")

    #Saisie de l'utilisateur qui commencera en premier
    print("Veuillez choisir le joueur qui va commencer (",joueur1," ou ",joueur2,") : ", end="")
    choix_commence_partie=input("")
    while choix_commence_partie!=joueur1 and choix_commence_partie!=joueur2:
        print("")
        print("Choix incorrect veuillez choisir ",joueur1," ou ",joueur2," : ", end="")
        choix_commence_partie=input("")

    #Gestion des tours
    if choix_commence_partie==joueur1:
        tour=1
    else:
        tour=2

    #Jeu
    while (nb_allumettes>0):
        os.system("CLS")
        if tour%2==1:
            print("A ton tour",TextStyle.BOLD + joueur1 + TextStyle.RESET,"(il reste ",TextStyle.BOLD,nb_allumettes,TextStyle.RESET,"allumettes) ->")
        else:
            print("A ton tour",TextStyle.BOLD + joueur2 + TextStyle.RESET,"(il reste ",TextStyle.BOLD,nb_allumettes,TextStyle.RESET,"allumettes) ->")

        #affichage des allumettes
        print("")
        for cpt in range(0, nb_allumettes):
            if (cpt%2==0):
                print(end=TextStyle.BG_CYAN + TextStyle.BOLD + " | " + TextStyle.RESET)
            else:
                print(end=TextStyle.BG_GREEN + TextStyle.BOLD + " | " + TextStyle.RESET)
        print("\n")

        #Le morceau pour retirer les allumettes
        retirer_allumettes=int(input("Choisissez le nombre d'allumettes que vous souhaitez retirer 1, 2 ou 3 :  "))
        while retirer_allumettes!=1 and retirer_allumettes!=2 and retirer_allumettes!=3:
            print("")
            retirer_allumettes=int(input("Erreur, choissisez 1, 2 ou 3 :  "))

        nb_allumettes-=retirer_allumettes
        tour+=1
    print("")


    #Scores

    gagnant.score=1
    if tour%2==1:
        gagnant.nom=joueur1
        print("Comme",joueur2,"a pris la dernière allumette,",joueur1,"a gagné (+1 victoire)")
    else :
        gagnant.nom=joueur2
        print("Comme",joueur1,"a pris la dernière allumette,",joueur2,"a gagné (+1 victoire)")

    ajout_score(score.allumettes, gagnant)

    print("")
    input("Appuyer sur entrer pour revenir au menu")

def jeu_allumettesJcIA(score : Jeu):
    """Cette procédure contient l'exécution du jeu des allumettes Joueur contre Ordinateur

    Args:
        score (Jeu): la variable contenant les scores
    """

    choix_commence_partie:str
    nb_allumettes:int
    retirer_allumettes:int
    cpt:int
    tour:int
    joueur1:str
    joueur2:str
    difficulte:int #1 pour facile et 2 pour difficile
    gagnant : Joueur
    gagnant = Joueur()

    nb_allumettes=20

    print(TextStyle.BOLD + "Bienvenue dans l'Allum'ouettes\n" + TextStyle.RESET)
    print("")

    #Choix des pseudos de chaque joueur avec contrôle de vérification sur la taille et si les pseudos sont identiques
    joueur2="Allumbot"
    joueur1=input("Joueur 1 veuillez saisir votre pseudo : ")
    while len(joueur1)>12 or joueur1==joueur2:
        if len(joueur1)>12:
            joueur1=input("Erreur, veuillez saisir un pseudo de 12 caractères maximum : ")
        else:
            joueur1=input("Erreur, veuillez saisir un pseudo différent du joueur 1 : ")
    print("")
    difficulte=int(input("Veuillez choisir la difficulté de l'ordinateur (1 pour facile, 2 pour difficile) : "))
    while difficulte!=1 and difficulte!=2:
        difficulte=int(input("Erreur, veuillez choisir 1 ou 2 : "))
    print("")

    #Saisie de l'utilisateur qui commencera en premier
    print("Veuillez choisir le joueur qui va commencer (",joueur1," ou ",joueur2,") : ", end="")
    choix_commence_partie=input("")
    while choix_commence_partie!=joueur1 and choix_commence_partie!=joueur2:
        print("")
        print("Choix incorrect veuillez choisir ",joueur1," ou ",joueur2," : ", end="")
        choix_commence_partie=input("")

    #Gestion des tours
    if choix_commence_partie==joueur1:
        tour=1
    else:
        tour=2

    #Jeu
    while (nb_allumettes>0):
        os.system("CLS")
        if tour%2==1:
            print("A ton tour",TextStyle.BOLD + joueur1 + TextStyle.RESET,"(il reste ",TextStyle.BOLD,nb_allumettes,TextStyle.RESET,"allumettes) ->")
        else:
            print("Au tour de ",TextStyle.BOLD + joueur2 + TextStyle.RESET,"(il reste ",TextStyle.BOLD,nb_allumettes,TextStyle.RESET,"allumettes) ->")

        #affichage des allumettes
        print("")
        for cpt in range(0, nb_allumettes):
            if (cpt%2==0):
                print(end=TextStyle.BG_CYAN + TextStyle.BOLD + " | " + TextStyle.RESET)
            else:
                print(end=TextStyle.BG_GREEN + TextStyle.BOLD + " | " + TextStyle.RESET)
        print("\n")

        #Le morceau pour retirer les allumettes
        if tour%2==1:
            retirer_allumettes=int(input("Choisissez le nombre d'allumettes que vous souhaitez retirer 1, 2 ou 3 :  "))
            while retirer_allumettes!=1 and retirer_allumettes!=2 and retirer_allumettes!=3:
                print("")
                retirer_allumettes=int(input("Erreur, choissisez 1, 2 ou 3 :  "))
        else:
            if difficulte==1:
                retirer_allumettes=random.randint(1,3)
            else:
                if nb_allumettes%4==3:
                    retirer_allumettes=2
                elif nb_allumettes%4==0:
                    retirer_allumettes=3
                else:
                    retirer_allumettes=1
            print("L'ordinateur retire ",retirer_allumettes,"allumette(s).")
            print("")
            input("Appuyez sur entrer pour passer au tour du joueur")

        nb_allumettes-=retirer_allumettes
        tour+=1
    print("")


    #Scores

    gagnant.score=1
    if tour%2==1:
        gagnant.nom=joueur1
        print("Comme",joueur2,"a pris la dernière allumette,",joueur1,"a gagné (+1 victoire)")
        ajout_score(score.allumettes, gagnant)
    else :
        print("Comme",joueur1,"a pris la dernière allumette,",joueur2,"a gagné")

    print("")
    input("Appuyez sur entrer pour revenir au menu")

def jeu_allumettesIAcIA():
    """Cette procédure contient l'exécution du jeu des allumettes Ordinateur contre Ordinateur
    """

    choix_commence_partie:str
    nb_allumettes:int
    retirer_allumettes:int
    cpt:int
    tour:int
    joueur1:str
    joueur2:str
    difficulte1:int
    difficulte2:int

    joueur1="Allumbot"
    joueur2="I'Allume"

    nb_allumettes=20

    print(TextStyle.BOLD + "Bienvenue dans l'Allum'ouettes\n" + TextStyle.RESET)
    print("")

    #Choix des difficulutés des bots
    print("Veuillez choisir la difficulté de",joueur1," (1 pour facile, 2 pour difficile) : ",end="")
    difficulte1=int(input())
    while difficulte1!=1 and difficulte1!=2:
        difficulte1=int(input("Erreur, veuillez choisir 1 ou 2 : "))
    print("")
    print("Veuillez choisir la difficulté de",joueur2," (1 pour facile, 2 pour difficile) : ",end="")
    difficulte2=int(input())
    while difficulte2!=1 and difficulte2!=2:
        difficulte2=int(input("Erreur, veuillez choisir 1 ou 2 : "))
    print("")

    #Saisie de l'utilisateur qui commencera en premier
    print("Veuillez choisir le joueur qui va commencer (",joueur1," ou ",joueur2,") : ", end="")
    choix_commence_partie=input("")
    while choix_commence_partie!=joueur1 and choix_commence_partie!=joueur2:
        print("")
        print("Choix incorrect veuillez choisir ",joueur1," ou ",joueur2," : ", end="")
        choix_commence_partie=input("")

    #Gestion des tours
    if choix_commence_partie==joueur1:
        tour=1
    else:
        tour=2

    #Jeu
    while (nb_allumettes>0):
        os.system("CLS")
        if tour%2==1:
            print("Au tour",TextStyle.BOLD + joueur1 + TextStyle.RESET,"(il reste ",TextStyle.BOLD,nb_allumettes,TextStyle.RESET,"allumettes) ->")
        else:
            print("Au tour",TextStyle.BOLD + joueur2 + TextStyle.RESET,"(il reste ",TextStyle.BOLD,nb_allumettes,TextStyle.RESET,"allumettes) ->")

        #affichage des allumettes
        print("")
        for cpt in range(0, nb_allumettes):
            if (cpt%2==0):
                print(end=TextStyle.BG_CYAN + TextStyle.BOLD + " | " + TextStyle.RESET)
            else:
                print(end=TextStyle.BG_GREEN + TextStyle.BOLD + " | " + TextStyle.RESET)
        print("\n")

        #Le morceau pour retirer les allumettes
        if tour%2==1:
            if difficulte1==1:
                retirer_allumettes=random.randint(1,3)
            else:
                if nb_allumettes%4==3:
                    retirer_allumettes=2
                elif nb_allumettes%4==0:
                    retirer_allumettes=3
                else:
                    retirer_allumettes=1
        else:
            if difficulte2==1:
                retirer_allumettes=random.randint(1,3)
            else:
                if nb_allumettes%4==3:
                    retirer_allumettes=2
                elif nb_allumettes%4==0:
                    retirer_allumettes=3
                else:
                    retirer_allumettes=1

        print("Il retire",retirer_allumettes,"allumette(s).")
        print("")
        input("Appuyez sur entrer pour passer au tour suivant")

        nb_allumettes-=retirer_allumettes
        tour+=1
    print("")


    #Scores

    if tour%2==1:
        print("Comme",joueur2,"a pris la dernière allumette,",joueur1,"a gagné")
    else :
        print("Comme",joueur1,"a pris la dernière allumette,",joueur2,"a gagné")

    print("")
    input("Appuyer sur entrer pour revenir au menu")

def menu_allumettes(score : Jeu):
    """Cette procédure permet la gestion du menu allumettes

    Args:
        score (Jeu): la variable contenant les scores
    """
    choix : int #Variable permettant de gérer le menu
    choix=0

    while(choix!=5):

        affiche_menu_jeu("Allum'ouettes")
        choix=int(input("Saisir votre choix : "))
        if choix==1 : #exécution du jeu
            os.system("CLS")
            jeu_allumettesJcJ(score)
        elif choix==2: 
            os.system("CLS")
            jeu_allumettesJcIA(score)
        elif choix==3: 
            os.system("CLS")
            jeu_allumettesIAcIA()
        elif choix==4: 
            affiche_regles_allumettes()
        elif choix==5: #retour au menu principal
            print("")  #On ne fait rien comme on retourne au menu précédent
        else :
            print("")
            print("Erreur dans le choix, veuillez entrer un nombre entre 1 et 5\n")
            print("")
            input("Appuyer sur entrer pour modifier votre choix")  

