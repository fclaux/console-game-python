import math
import os
import random
from structures import *
from regles import affiche_regles_devinettes
from affiche_menu_jeu import *
from gestion_tableau import *


def jeu_devinetteJcJ(score : Jeu): 
    """Cette procédure contient l'exécution du jeu des devinettes

    Args:
        score (Jeu): la variable contenant les scores
    """
    nb_a_deviner : int
    nb_choix_j2 : int
    nb_essais_necessaire: int
    borne_max : int
    reponse_joueur1:str
    compteur_essais:int
    joueur1 : Joueur
    joueur1 = Joueur()
    joueur2 : Joueur
    joueur2 = Joueur()

    nb_choix_j2=-1
    compteur_essais=0

    
    print(TextStyle.BOLD + "Bienvenue dans le Devin'ombre\n" + TextStyle.RESET)
    print("")

    #Choix des pseudos de chaque joueur avec contrôle de vérification sur la taille et si les pseudos sont identiques
    joueur1.nom = input("La personne qui veut faire deviner entrez votre pseudo : ")
    while len(joueur1.nom)>12:
        joueur1.nom=input("Erreur, veuillez saisir un pseudo de 12 caractères maximum : ")
    print("")
    joueur2.nom = input("La personne qui devine entrez votre pseudo : ")
    while len(joueur2.nom)>12 or joueur2.nom==joueur1.nom:
        if len(joueur2.nom)>12:
            joueur2.nom=input("Erreur, veuillez saisir un pseudo de 12 caractères maximum : ")
        else:
            joueur2.nom=input("Erreur, veuillez saisir un pseudo différent du joueur 1 : ")

    os.system("CLS")

    #Premier partie où le joueur 1 établit l'étendu de jeu (intervalle, nombre à deviner) : le nombre d'essais se calcule automatiquement avec la borne max
    print(TextStyle.RED + joueur1.nom,"c'est à vous ->\n")

    borne_max=int(input("Choisissez la borne max (minimum 2 et maximum 1000000): "))
    while (borne_max<2) or (borne_max>1000000):
        print("Le borne n'est pas dans l'intervalle\n")
        borne_max=int(input("Ressaisissez une borne max : "))

    nb_essais_necessaire=math.ceil(math.log2(borne_max)) #Calcul le nombre d'essais necssaire à la résolution par dichotomie

    nb_a_deviner=int(input("Nombre à deviner : "))

    while (nb_a_deviner<1) or (nb_a_deviner>borne_max):
        print("Le nombre à deviner n'est pas dans l'intervalle\n")
        nb_a_deviner=int(input("Saisissez un nouveau nombre : "))

    #Pour clear l'écran : "cls" pour windows et "clear" pour linux
    os.system("CLS") 

    #Déroulement du jeu 
    while (nb_choix_j2!=nb_a_deviner) : # On sort de la boucle si la proposition du joueur2 = le nombre à deviner

        #Tour du joueur 2
        print(TextStyle.GREEN + joueur2.nom,"c'est à vous ->\n")
        print("Votre proposition (entre 1 et ",borne_max,") : ",end="")
        nb_choix_j2=int(input())
        while (nb_choix_j2<=0)or(nb_choix_j2>borne_max):
            print("Votre proposition n'est pas dans la borne\n")
            print("Votre proposition (entre 1 et ",borne_max,") : ",end="")
            nb_choix_j2=int(input())

        print("")
        print(TextStyle.WHITE + "---------------------------------------------------\n")

        #Tour du joueur 1
        print(TextStyle.RED + joueur1.nom,"c'est à vous ->\n")
        reponse_joueur1=input("Votre réponse (trop petit, trop grand, c'est gagné) : ")
        while ((nb_choix_j2<nb_a_deviner)and(reponse_joueur1!="trop petit"))or((nb_choix_j2>nb_a_deviner)and(reponse_joueur1!="trop grand"))or((nb_choix_j2==nb_a_deviner)and(reponse_joueur1!="c'est gagné")):
            print("Votre proposition est incorrect\n")
            reponse_joueur1=input("Veuillez ressaisir votre réponse (trop petit, trop grand, c'est gagné) : ")
        print(TextStyle.RESET)

        print("")
        print(TextStyle.WHITE + "---------------------------------------------------\n")
        
        compteur_essais=compteur_essais+1
    

    #calcul du score final avec annonce du gagnant
    if compteur_essais>nb_essais_necessaire :
        joueur2.score=10
    else :
        joueur2.score=int((1500-(1405*pow(borne_max,-0.341)))/compteur_essais)
    print("C'est",joueur2.nom,"qui a gagné, vous remportez ",joueur2.score ,"pts pour avoir trouvé en ", compteur_essais)
    ajout_score(score.devinette, joueur2)

    print("")
    input("Appuyer sur entrer pour revenir au menu")

def jeu_devinetteJcIA(score : Jeu): 
    """Cette procédure contient l'exécution du jeu des devinettes

    Args:
        score (Jeu): la variable contenant les scores
    """
    nb_a_deviner : int
    nb_choix_j2 : int
    nb_essais_necessaire: int
    borne_max : int
    reponse_joueur1:int
    compteur_essais:int
    joueur1 : Joueur
    joueur1 = Joueur()
    roles:int
    a:int
    b:int
    m:int

    nb_choix_j2=-1
    compteur_essais=0

    
    print(TextStyle.BOLD + "Bienvenue dans le Devin'ombre\n" + TextStyle.RESET)
    print("")

    #Choix des pseudos de chaque joueur avec contrôle de vérification sur la taille et si les pseudos sont identiques
    joueur1.nom = input("Entrez votre pseudo (12 caractères maximum) : ")
    while len(joueur1.nom)>12:
        joueur1.nom=input("Erreur, veuillez saisir un pseudo de 12 caractères maximum : ")
    print("")

    roles = int(input("Quel rôle voulez vous avoir (1 pour deviner ou 2 pour faire deviner) : "))
    while roles<1 or roles>2:
        roles = int(input("ERREUR, veuillez entrer 1 ou 2 : "))

    os.system("CLS")

    #Premier partie où le joueur 1 OU l'ordinateur établit l'étendu de jeu (intervalle, nombre à deviner) : le nombre d'essais se calcule automatiquement avec la borne max
    if roles==1:
        borne_max=random.randint(2, 1000000) #Génération de la borne maximum

        nb_essais_necessaire=math.ceil(math.log2(borne_max)) #Calcul le nombre d'essais nécessaire à la résolution par dichotomie

        nb_a_deviner=random.randint(1, borne_max) #Génération du nombre à deviner

        nb_essais_necessaire=math.ceil(math.log2(borne_max)) #Calcul le nombre d'essais necssaire à la résolution par dichotomie pour le score
    else :
        print(TextStyle.RED + joueur1.nom,"c'est à vous ->\n")

        difficulte = int(input("Choississez la difficulté de l'ordinateur (1 pour facile, 2 pour normale ou 3 pour difficile) : "))
        while difficulte<1 or difficulte>3:
            difficulte=int(input("Erreur, veuillez choisir 1, 2 ou 3 : "))
        print("")

        borne_max=int(input("Choisissez la borne max (minimum 2 et maximum 1000000): "))
        while (borne_max<2) or (borne_max>1000000):
            print("Le borne n'est pas dans l'intervalle\n")
            borne_max=int(input("Ressaisissez une borne max : "))

        nb_a_deviner=int(input("Nombre à deviner : "))

        while (nb_a_deviner<1) or (nb_a_deviner>borne_max):
            print("Le nombre à deviner n'est pas dans l'intervalle\n")
            nb_a_deviner=int(input("Saisissez un nouveau nombre : "))

        #Gestion des bornes pour la dichotomie
        a=1
        b=borne_max
        m=(a+b)//2

    
    #Pour clear l'écran : "cls" pour windows et "clear" pour linux
    os.system("CLS") 

    #Déroulement du jeu 
    while (nb_choix_j2!=nb_a_deviner) : # On sort de la boucle si la proposition du joueur2 = le nombre à deviner

    #Propositon d'un nombre
        #Tour du joueur
        if roles==1:
            print(TextStyle.GREEN + joueur1.nom,"c'est à vous ->\n")
            print("Votre proposition (entre 1 et ",borne_max,") : ",end="")
            nb_choix_j2=int(input())
            while (nb_choix_j2<=0)or(nb_choix_j2>borne_max):
                print("Votre proposition n'est pas dans la borne\n")
                print("Votre proposition (entre 1 et ",borne_max,") : ",end="")
                nb_choix_j2=int(input())
        #Tour de l'ordianteur
        else :
            print(TextStyle.GREEN + "Proposition de l'ordinateur (entre 1 et ",borne_max,"): ", end="")
            if difficulte==1: #Recherche aléatoire
                nb_choix_j2=random.randint(1, borne_max)
            elif difficulte==2: #Recherche semi dichotomique, semi aléatoire
                #On commence avec la valeur millieu de l'intervalle puis pour les essais suivant on prend un nombre aléatoire dans l'intervalle réduit
                if compteur_essais==0:
                    nb_choix_j2=m
                else:
                    if reponse_joueur1==1:
                        nb_choix_j2=random.randint(a,nb_choix_j2)
                    else :
                        nb_choix_j2=random.randint(nb_choix_j2,b)    
            else : #Recherche dichotomique
                nb_choix_j2=m
            print(nb_choix_j2)
            
        print("")
        print(TextStyle.WHITE + "---------------------------------------------------\n")

    #Réponse en fonction du nombre
        #Tour du joueur 1
        print(TextStyle.RED)
        if roles==1:
            if nb_choix_j2<nb_a_deviner:
                print("Le nombre à trouver est plus grand")
            elif nb_choix_j2>nb_a_deviner:
                print("Le nombre à trouver est plus petit")
            else :
                print("C'est le bon nombre !!")
        else:
            print(joueur1.nom,"c'est à vous ->\n")
            reponse_joueur1=int(input("Votre réponse (1 pour trop petit, 2 pour trop grand, 3 pour c'est gagné) : "))
            while ((nb_choix_j2<nb_a_deviner)and(reponse_joueur1!=1))or((nb_choix_j2>nb_a_deviner)and(reponse_joueur1!=2))or((nb_choix_j2==nb_a_deviner)and(reponse_joueur1!=3)):
                print("Votre proposition est incorrect\n")
                reponse_joueur1=int(input("Veuillez ressaisir votre réponse (trop petit, trop grand, c'est gagné) : "))

            #pour la dichotomie
            if nb_choix_j2<nb_a_deviner:
                a=nb_choix_j2+1
            elif nb_choix_j2>nb_a_deviner:
                b=nb_choix_j2-1
            m=(a+b)//2
            

        print("")
        print(TextStyle.WHITE + "---------------------------------------------------\n")
        
        compteur_essais=compteur_essais+1
    
    if roles==1:
        #calcul du score final
        if compteur_essais>nb_essais_necessaire :
            joueur1.score=10
        else :
            joueur1.score=int((1500-(1405*pow(borne_max,-0.341)))/compteur_essais)
        print(joueur1.nom,"vous avez trouvé le nombre en",compteur_essais,"essais, vous remportez : ",joueur1.score ,"pts")
        ajout_score(score.devinette, joueur1)
    else:
        print("L'ordinateur a trouvé en", compteur_essais, "essais.")

    print("")
    input("Appuyer sur entrer pour revenir au menu")

def jeu_devinetteIAcIA(): 
    """Cette procédure contient l'exécution du jeu des devinettes

    Args:
        score (Jeu): la variable contenant les scores
    """
    nb_a_deviner : int
    nb_choix_j2 : int
    nb_essais_necessaire: int
    borne_max : int
    reponse_joueur1:int #0 pour gagné, 1 pour trop petit et 2 pour trop grand
    compteur_essais:int
    difficulte : int

    #borne pour la dichotomie
    a:int
    b:int
    m:int

    nb_choix_j2=-1
    compteur_essais=0

    
    print(TextStyle.BOLD + "Bienvenue dans le Devin'ombre\n" + TextStyle.RESET)
    print("")

    #Choix de la difficulté de l'ordinateur qui va cherche un nombre
    difficulte = int(input("Choississez la difficulté de l'ordinateur (1 pour facile, 2 pour normale ou 3 pour difficile) : "))
    while difficulte<1 or difficulte>3:
        difficulte=int(input("Erreur, veuillez choisir 1, 2 ou 3 : "))
    print("")
 

    os.system("CLS")

    #Premier partie où le joueur 1 établit l'étendu de jeu (intervalle, nombre à deviner) : le nombre d'essais se calcule automatiquement avec la borne max

    borne_max=random.randint(2, 1000000) #Génération de la borne maximum

    nb_essais_necessaire=math.ceil(math.log2(borne_max)) #Calcul le nombre d'essais nécessaire à la résolution par dichotomie

    nb_a_deviner=random.randint(1, borne_max) #Génération du nombre à deviner

    #Gestion des bornes pour la dichotomie
    a=1
    b=borne_max
    m=(a+b)//2

    #Pour clear l'écran : "cls" pour windows et "clear" pour linux
    os.system("CLS") 

    #Déroulement du jeu 
    while (nb_choix_j2!=nb_a_deviner) : # On sort de la boucle si la proposition du joueur2 = le nombre à deviner

        #Tour du joueur 2
        print(TextStyle.GREEN + "Proposition de l'ordinateur (entre 1 et ",borne_max,"): ", end="")
        if difficulte==1: #Recherche aléatoire
            nb_choix_j2=random.randint(1, borne_max)
        elif difficulte==2: #Recherche aléatoire avec réduction d'intervalle
            #On commence avec la valeur millieu de l'intervalle puis pour les essais suivant on prend un nombre aléatoire dans l'intervalle réduit
            if compteur_essais==0:
                nb_choix_j2=m
            else:
                if reponse_joueur1==1:
                    nb_choix_j2=random.randint(a,nb_choix_j2)
                else :
                    nb_choix_j2=random.randint(nb_choix_j2,b)    
        else : #Recherche dichotomique
            nb_choix_j2=m


        print(nb_choix_j2)

        print("")
        print(TextStyle.WHITE + "---------------------------------------------------\n")

        #Tour du joueur 1
        print(TextStyle.RED)
        if nb_choix_j2<nb_a_deviner:
            reponse_joueur1=2
            print("Le nombre à trouver est plus grand")
            a=nb_choix_j2+1
        elif nb_choix_j2>nb_a_deviner:
            reponse_joueur1=1
            print("Le nombre à trouver est plus petit")
            b=nb_choix_j2-1
        else :
            reponse_joueur1=0
            print("C'est le bon nombre !!")

        m=(a+b)//2

        print("")
        print(TextStyle.WHITE + "---------------------------------------------------\n")
        compteur_essais=compteur_essais+1
    
    print("L'ordinateur a trouvé en", compteur_essais, "essais.")
    print("")
    input("Appuyer sur entrer pour revenir au menu")
    

def menu_devinette(score : Jeu):
    """Cette procédure permet la gestion du menu devinette

    Args:
        score (Jeu): la variable contenant les scores
    """

    choix : int #Variable permettant de gérer le menu
    choix=0
    
    while(choix!=5):

        affiche_menu_jeu("Devin'ombre  ")
        choix=int(input("Saisir votre choix : "))
        if choix==1 : #exécution du jeu
            os.system("CLS")
            jeu_devinetteJcJ(score)
        elif choix==2: 
            os.system("CLS")
            jeu_devinetteJcIA(score)
        elif choix==3: 
            os.system("CLS")
            jeu_devinetteIAcIA()
        elif choix==4: 
            affiche_regles_devinettes()
        elif choix==5: #retour au menu principal
            print("")  #On ne fait rien comme on retourne au menu précédent
        else :
            print("")
            print("Erreur dans le choix, veuillez entrer un nombre entre 1 et 5\n")
            print("")
            input("Appuyer sur entrer pour modifier votre choix")
