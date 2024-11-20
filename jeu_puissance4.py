import os
from structures import *
from regles import affiche_regles_puissance4
from affiche_menu_jeu import *
from gestion_tableau import *

def afffiche_grille_puissance4(grille : list[int]):
    """
    afffiche_grille_puissance4 

    Cette procédure affiche la grille avec les jetons placés

    Args:
        grille (list[int]): tableau d'entier (0 : vide, 1 : pion J1, 2 : pion J2) de 42 cases
    """

    for cpt in range(0, 6):
        for cpt2 in range(0, 7):
            if grille[cpt2+cpt*7]==1:
                print("| "+ TextStyle.YELLOW + "\u25CF " + TextStyle.RESET , end="")
            elif grille[cpt2+cpt*7]==2:
                print("| "+ TextStyle.RED + "\u25CF " + TextStyle.RESET , end="")
            else :
                print("|   ", end="")

        print("|")
        print("+" + "---+" * 7)
    for cpt in range(1,8):
        print(" ",cpt, end=" ")
    print("")

def verif_colonne_pleine(grille : list[int], colonne : int)->bool:
    """
    verif_colonne_pleine 

    Cette fonction retourne vraie si la colonne est pleine

    Args:
        grille (list[int]): grille du jeu
        colonne (int): colonne choisi par le joueur (un entier entre 1 et 7)

    Returns:
        bool: retourne vrai si la colonne est pleine
    """
    ligne : int

    ligne=5
    while grille[(colonne-1)+7*ligne]!=0 and ligne>=0:
            ligne-=1
    
    if ligne==-1:
        return False
    else: 
        return True

def verif_horizontal(grille:list[int], num_joueur : int) -> bool:
    """
    verif_horizontal 

    Cette fonction vérifie la conditon de victoire : 4 jetons sur une même ligne qui se suivent

    Args:
        grille (list[int]): grille du jeu
        num_joueur (int): un entier soit égal à 1 pour vérifier si le joueur 1 a gagné, soit égal à 2 pour vérifier si c'est le joueur 2 qui a gagné

    Returns:
        _type_: retourne un booleen qui retourne vraie si le joueur à gagner
    """
    ligne : int
    colonne : int
    for ligne in range(0,6):
        for colonne in range(0,4):  # Pour vérifier les lignes 
            if grille[ligne * 7 + colonne] == num_joueur and grille[ligne * 7 + colonne + 1] == num_joueur and grille[ligne * 7 + colonne + 2] == num_joueur and grille[ligne * 7 + colonne + 3] == num_joueur:
                return True
    return False

def verif_vertical(grille:list[int], num_joueur : int) -> bool:
    """
    verif_horizontal 

    Cette fonction vérifie la conditon de victoire : 4 jetons sur une même colonne qui se suivent

    Args:
        grille (list[int]): grille du jeu
        num_joueur (int): un entier soit égal à 1 pour vérifier si le joueur 1 a gagné, soit égal à 2 pour vérifier si c'est le joueur 2 qui a gagné

    Returns:
        _type_: retourne un booleen qui retourne vraie si le joueur à gagner
    """
    ligne : int
    colonne : int
    for colonne in range(0,7):
        for ligne in range(0,3):  # Pour vérifier les colonnes 
            if grille[ligne * 7 + colonne] == num_joueur and grille[(ligne + 1) * 7 + colonne] == num_joueur and grille[(ligne + 2) * 7 + colonne] == num_joueur and grille[(ligne + 3) * 7 + colonne] == num_joueur:
                return True
    return False

def verif_diagonale(grille:list[int], num_joueur : int):
    """
    verif_horizontal 

    Cette fonction vérifie la conditon de victoire : 4 jetons sur une même diagonale qui se suivent

    Args:
        grille (list[int]): grille du jeu
        num_joueur (int): un entier soit égal à 1 pour vérifier si le joueur 1 a gagné, soit égal à 2 pour vérifier si c'est le joueur 2 qui a gagné

    Returns:
        _type_: retourne un booleen qui retourne vraie si le joueur à gagner
    """
    ligne : int
    colonne : int
    # Vérification des diagonales ascendantes
    for ligne in range(0,3):
        for colonne in range(0,4):
            if grille[ligne * 7 + colonne] == num_joueur and grille[(ligne + 1) * 7 + colonne + 1] == num_joueur and grille[(ligne + 2) * 7 + colonne + 2] == num_joueur and grille[(ligne + 3) * 7 + colonne + 3] == num_joueur:
                return True
    # Vérification des diagonales descendantes
    for ligne in range(0,3):
        for colonne in range(0,4):
            if grille[(ligne + 3) * 7 + colonne] == num_joueur and grille[(ligne + 2) * 7 + colonne + 1] == num_joueur and grille[(ligne + 1) * 7 + colonne + 2] == num_joueur and grille[ligne * 7 + colonne + 3] == num_joueur:
                return True
    return False

def jeu_puissance4JcJ(score : Jeu):
    """Cette procédure contient l'exécution du Puissance 4

    Args:
        score (Jeu): la variable contenant les scores
    """
    joueur1 : Joueur
    joueur2 : Joueur
    joueur1 = Joueur()
    joueur2 = Joueur()
    tour : int
    grille : list[int]
    nb_cases_libres : int
    ligne : int
    choix_colonne_joueur : int

    grille = [0]*42 #initialisation des 42 cases de la grille 
    nb_cases_libres = 42

    #Choix des pseudos de chaque joueur avec contrôle de vérification sur la taille et si les pseudos sont identiques
    print(TextStyle.BOLD + "Bienvenue dans le Puissance 4\n" + TextStyle.RESET)
    print(TextStyle.YELLOW)
    joueur1.nom = input("La personne qui prend les jaunes : ")
    while len(joueur1.nom)>12:
        joueur1.nom=input("Erreur, veuillez saisir un pseudo de 12 caractères maximum : ")
    print(TextStyle.RED)
    joueur2.nom = input("La personne qui prend les rouges : ")
    while len(joueur2.nom)>12 or joueur2.nom==joueur1.nom:
        if len(joueur2.nom)>12:
            joueur2.nom=input("Erreur, veuillez saisir un pseudo de 12 caractères maximum : ")
        else:
            joueur2.nom=input("Erreur, veuillez saisir un pseudo différent du joueur 1 : ")
    print(TextStyle.RESET)

    #Saisie de l'utilisateur qui commencera en premier
    print("Veuillez choisir le joueur qui va commencer (",joueur1.nom," ou ",joueur2.nom,") : ", end="")
    choix_commence_partie=input("")
    while choix_commence_partie!=joueur1.nom and choix_commence_partie!=joueur2.nom:
        print("")
        print("Choix incorrect veuillez choisir ",joueur1.nom," ou ",joueur2.nom," : ", end="")
        choix_commence_partie=input("")


    #Gestion des tours
    if choix_commence_partie==joueur1.nom:
        tour=1
    else:
        tour=2

    partie_termine=False
    while nb_cases_libres>0 and not(partie_termine):
        os.system("CLS")
        #tour du joueur 1
        if tour%2==1:
            print(TextStyle.YELLOW, "A ton tour",TextStyle.BOLD + joueur1.nom + TextStyle.RESET," ->")
            tour=1
        #tour du joueur 2
        else:
            print(TextStyle.RED, "A ton tour",TextStyle.BOLD + joueur2.nom + TextStyle.RESET," ->")
            tour=2
        print("")
        afffiche_grille_puissance4(grille)

        choix_colonne_joueur=int(input("Choisis la colonne où tu veux placer ton jeton : "))
        print("")
        #vérification que le joueur respecte l'intervalle
        while choix_colonne_joueur<1 or choix_colonne_joueur>7:
            print("Le choix de la colonne doit être compris entre 1 et 7")
            choix_colonne_joueur=int(input("Veuillez saisir de nouveau votre choix : "))
        print("")
        #probleme de verification, on doit s'assurer de deux choses : l'intervalle et si c'est plein
        #seulement pour vérifier si c'est plein on doit s'assurer que l'input de l'utilisateur est dans l'intervalle 
        while choix_colonne_joueur<1 or choix_colonne_joueur>7 or not(verif_colonne_pleine(grille, choix_colonne_joueur)):
            if (choix_colonne_joueur<1 or choix_colonne_joueur>7):
                print("Le choix de la colonne doit être compris entre 1 et 7")
                choix_colonne_joueur=int(input("Veuillez saisir de nouveau votre choix : "))
            else :
                choix_colonne_joueur=int(input("La colonne est pleine, veuillez choisir une autre colonne : "))
        print("")

        #ajout du jeton dans le tableau
        ligne=5
        while grille[(choix_colonne_joueur-1)+7*ligne]!=0:
            ligne-=1
        grille[(choix_colonne_joueur-1)+7*ligne]=tour

        tour+=1
        nb_cases_libres-=1

        #Condition de victoire du joueur 1
        if verif_horizontal(grille, 1) or verif_vertical(grille, 1) or verif_diagonale(grille, 1):
            os.system("CLS")
            print(TextStyle.YELLOW + joueur1.nom, "a gagné !", TextStyle.RESET)
            print("")
            afffiche_grille_puissance4(grille)
            joueur1.score=1
            ajout_score(score.puissance4, joueur1)
            partie_termine=True
        #Condition de victoire du joueur 2
        elif verif_horizontal(grille, 2) or verif_vertical(grille, 2) or verif_diagonale(grille, 2):
            os.system("CLS")
            print(TextStyle.RED + joueur2.nom, "a gagné !", TextStyle.RESET)
            print("")
            afffiche_grille_puissance4(grille)
            joueur2.score=1
            ajout_score(score.puissance4, joueur2)
            partie_termine=True
    
    #Match nul
    if nb_cases_libres==0:
        os.system("CLS")
        print("La grille est pleine c'est un match nul")
        print("")
        afffiche_grille_puissance4(grille)

    print("")
    input("Appuyer sur entrer pour revenir au menu ")

def jeu_puissance4JcIA(score : Jeu):# A FAIRE
    """Cette procédure contient l'exécution du Puissance 4

    Args:
        score (Jeu): la variable contenant les scores
    """
    joueur1 : Joueur
    joueur2 : Joueur
    joueur1 = Joueur()
    joueur2 = Joueur()
    tour : int
    grille : list[int]
    nb_cases_libres : int
    ligne : int
    choix_colonne_joueur : int

    grille = [0]*42 #initialisation des 42 cases de la grille 
    nb_cases_libres = 42

    #Choix des pseudos de chaque joueur avec contrôle de vérification sur la taille et si les pseudos sont identiques
    print(TextStyle.BOLD + "Bienvenue dans le Puissance 4\n" + TextStyle.RESET)
    print(TextStyle.YELLOW)
    joueur1.nom = input("La personne qui prend les jaunes : ")
    while len(joueur1.nom)>12:
        joueur1.nom=input("Erreur, veuillez saisir un pseudo de 12 caractères maximum : ")
    print(TextStyle.RED)
    joueur2.nom = input("La personne qui prend les rouges : ")
    while len(joueur2.nom)>12 or joueur2.nom==joueur1.nom:
        if len(joueur2.nom)>12:
            joueur2.nom=input("Erreur, veuillez saisir un pseudo de 12 caractères maximum : ")
        else:
            joueur2.nom=input("Erreur, veuillez saisir un pseudo différent du joueur 1 : ")
    print(TextStyle.RESET)

    #Saisie de l'utilisateur qui commencera en premier
    print("Veuillez choisir le joueur qui va commencer (",joueur1.nom," ou ",joueur2.nom,") : ", end="")
    choix_commence_partie=input("")
    while choix_commence_partie!=joueur1.nom and choix_commence_partie!=joueur2.nom:
        print("")
        print("Choix incorrect veuillez choisir ",joueur1.nom," ou ",joueur2.nom," : ", end="")
        choix_commence_partie=input("")


    #Gestion des tours
    if choix_commence_partie==joueur1.nom:
        tour=1
    else:
        tour=2

    partie_termine=False
    while nb_cases_libres>0 and not(partie_termine):
        os.system("CLS")
        #tour du joueur 1
        if tour%2==1:
            print(TextStyle.YELLOW, "A ton tour",TextStyle.BOLD + joueur1.nom + TextStyle.RESET," ->")
            tour=1
        #tour du joueur 2
        else:
            print(TextStyle.RED, "A ton tour",TextStyle.BOLD + joueur2.nom + TextStyle.RESET," ->")
            tour=2
        print("")
        afffiche_grille_puissance4(grille)

        choix_colonne_joueur=int(input("Choisis la colonne où tu veux placer ton jeton : "))
        print("")
        #vérification que le joueur respecte l'intervalle
        while choix_colonne_joueur<1 or choix_colonne_joueur>7:
            print("Le choix de la colonne doit être compris entre 1 et 7")
            choix_colonne_joueur=int(input("Veuillez saisir de nouveau votre choix : "))
        print("")
        #probleme de verification, on doit s'assurer de deux choses : l'intervalle et si c'est plein
        #seulement pour vérifier si c'est plein on doit s'assurer que l'input de l'utilisateur est dans l'intervalle 
        while choix_colonne_joueur<1 or choix_colonne_joueur>7 or not(verif_colonne_pleine(grille, choix_colonne_joueur)):
            if (choix_colonne_joueur<1 or choix_colonne_joueur>7):
                print("Le choix de la colonne doit être compris entre 1 et 7")
                choix_colonne_joueur=int(input("Veuillez saisir de nouveau votre choix : "))
            else :
                choix_colonne_joueur=int(input("La colonne est pleine, veuillez choisir une autre colonne : "))
        print("")

        #ajout du jeton dans le tableau
        ligne=5
        while grille[(choix_colonne_joueur-1)+7*ligne]!=0:
            ligne-=1
        grille[(choix_colonne_joueur-1)+7*ligne]=tour

        tour+=1
        nb_cases_libres-=1

        #Condition de victoire du joueur 1
        if verif_horizontal(grille, 1) or verif_vertical(grille, 1) or verif_diagonale(grille, 1):
            os.system("CLS")
            print(TextStyle.YELLOW + joueur1.nom, "a gagné !", TextStyle.RESET)
            print("")
            afffiche_grille_puissance4(grille)
            joueur1.score=1
            ajout_score(score.puissance4, joueur1)
            partie_termine=True
        #Condition de victoire du joueur 2
        elif verif_horizontal(grille, 2) or verif_vertical(grille, 2) or verif_diagonale(grille, 2):
            os.system("CLS")
            print(TextStyle.RED + joueur2.nom, "a gagné !", TextStyle.RESET)
            print("")
            afffiche_grille_puissance4(grille)
            joueur2.score=1
            ajout_score(score.puissance4, joueur2)
            partie_termine=True
    
    #Match nul
    if nb_cases_libres==0:
        os.system("CLS")
        print("La grille est pleine c'est un match nul")
        print("")
        afffiche_grille_puissance4(grille)

    print("")
    input("Appuyer sur entrer pour revenir au menu ")

def jeu_puissance4IAcIA(score : Jeu):# A FAIRE
    """Cette procédure contient l'exécution du Puissance 4

    Args:
        score (Jeu): la variable contenant les scores
    """
    joueur1 : Joueur
    joueur2 : Joueur
    joueur1 = Joueur()
    joueur2 = Joueur()
    tour : int
    grille : list[int]
    nb_cases_libres : int
    ligne : int
    choix_colonne_joueur : int

    grille = [0]*42 #initialisation des 42 cases de la grille 
    nb_cases_libres = 42

    #Choix des pseudos de chaque joueur avec contrôle de vérification sur la taille et si les pseudos sont identiques
    print(TextStyle.BOLD + "Bienvenue dans le Puissance 4\n" + TextStyle.RESET)
    print(TextStyle.YELLOW)
    joueur1.nom = input("La personne qui prend les jaunes : ")
    while len(joueur1.nom)>12:
        joueur1.nom=input("Erreur, veuillez saisir un pseudo de 12 caractères maximum : ")
    print(TextStyle.RED)
    joueur2.nom = input("La personne qui prend les rouges : ")
    while len(joueur2.nom)>12 or joueur2.nom==joueur1.nom:
        if len(joueur2.nom)>12:
            joueur2.nom=input("Erreur, veuillez saisir un pseudo de 12 caractères maximum : ")
        else:
            joueur2.nom=input("Erreur, veuillez saisir un pseudo différent du joueur 1 : ")
    print(TextStyle.RESET)

    #Saisie de l'utilisateur qui commencera en premier
    print("Veuillez choisir le joueur qui va commencer (",joueur1.nom," ou ",joueur2.nom,") : ", end="")
    choix_commence_partie=input("")
    while choix_commence_partie!=joueur1.nom and choix_commence_partie!=joueur2.nom:
        print("")
        print("Choix incorrect veuillez choisir ",joueur1.nom," ou ",joueur2.nom," : ", end="")
        choix_commence_partie=input("")


    #Gestion des tours
    if choix_commence_partie==joueur1.nom:
        tour=1
    else:
        tour=2

    partie_termine=False
    while nb_cases_libres>0 and not(partie_termine):
        os.system("CLS")
        #tour du joueur 1
        if tour%2==1:
            print(TextStyle.YELLOW, "A ton tour",TextStyle.BOLD + joueur1.nom + TextStyle.RESET," ->")
            tour=1
        #tour du joueur 2
        else:
            print(TextStyle.RED, "A ton tour",TextStyle.BOLD + joueur2.nom + TextStyle.RESET," ->")
            tour=2
        print("")
        afffiche_grille_puissance4(grille)

        choix_colonne_joueur=int(input("Choisis la colonne où tu veux placer ton jeton : "))
        print("")
        #vérification que le joueur respecte l'intervalle
        while choix_colonne_joueur<1 or choix_colonne_joueur>7:
            print("Le choix de la colonne doit être compris entre 1 et 7")
            choix_colonne_joueur=int(input("Veuillez saisir de nouveau votre choix : "))
        print("")
        #probleme de verification, on doit s'assurer de deux choses : l'intervalle et si c'est plein
        #seulement pour vérifier si c'est plein on doit s'assurer que l'input de l'utilisateur est dans l'intervalle 
        while choix_colonne_joueur<1 or choix_colonne_joueur>7 or not(verif_colonne_pleine(grille, choix_colonne_joueur)):
            if (choix_colonne_joueur<1 or choix_colonne_joueur>7):
                print("Le choix de la colonne doit être compris entre 1 et 7")
                choix_colonne_joueur=int(input("Veuillez saisir de nouveau votre choix : "))
            else :
                choix_colonne_joueur=int(input("La colonne est pleine, veuillez choisir une autre colonne : "))
        print("")

        #ajout du jeton dans le tableau
        ligne=5
        while grille[(choix_colonne_joueur-1)+7*ligne]!=0:
            ligne-=1
        grille[(choix_colonne_joueur-1)+7*ligne]=tour

        tour+=1
        nb_cases_libres-=1

        #Condition de victoire du joueur 1
        if verif_horizontal(grille, 1) or verif_vertical(grille, 1) or verif_diagonale(grille, 1):
            os.system("CLS")
            print(TextStyle.YELLOW + joueur1.nom, "a gagné !", TextStyle.RESET)
            print("")
            afffiche_grille_puissance4(grille)
            joueur1.score=1
            ajout_score(score.puissance4, joueur1)
            partie_termine=True
        #Condition de victoire du joueur 2
        elif verif_horizontal(grille, 2) or verif_vertical(grille, 2) or verif_diagonale(grille, 2):
            os.system("CLS")
            print(TextStyle.RED + joueur2.nom, "a gagné !", TextStyle.RESET)
            print("")
            afffiche_grille_puissance4(grille)
            joueur2.score=1
            ajout_score(score.puissance4, joueur2)
            partie_termine=True
    
    #Match nul
    if nb_cases_libres==0:
        os.system("CLS")
        print("La grille est pleine c'est un match nul")
        print("")
        afffiche_grille_puissance4(grille)

    print("")
    input("Appuyer sur entrer pour revenir au menu ")

def menu_puissance4(score : Jeu):
    """Cette procédure permet la gestion du menu puissance4

    Args:
        score (Jeu): la variable contenant les scores
    """

    choix : int #Variable permettant de gérer le menu
    choix=0
    
    while(choix!=5):

        affiche_menu_jeu("Puissance 4  ")
        choix=int(input("Saisir votre choix : "))
        if choix==1 : #exécution du jeu
            os.system("CLS")
            jeu_puissance4JcJ(score)
        elif choix==2: 
            os.system("CLS")
            jeu_puissance4JcIA(score)
        elif choix==3: 
            os.system("CLS")
            jeu_puissance4IAcIA(score)
        elif choix==4: 
            affiche_regles_puissance4()
        elif choix==5: #retour au menu principal
            print("")  #On ne fait rien comme on retourne au menu précédent
        else :
            print("")
            print("Erreur dans le choix, veuillez entrer un nombre entre 1 et 3\n")
            print("")
            input("Appuyer sur entrer pour modifier votre choix")