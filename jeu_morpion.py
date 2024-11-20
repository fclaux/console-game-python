import os
from structures import *
from regles import affiche_regles_morpion
from affiche_menu_jeu import *
from gestion_tableau import *
import random
    
def Afficher_morpion(grille : list[str]) :
    """
    Afficher_morpion fonction permettant la création et l'affichage de la grille de morpion

    Args:
        grille (list): liste comprenant 9 zones de caractères pour la mise en place
    """
    cpt : int
    
    print("    1   2   3")
    print("  -------------")
    print("1", end='')
    for cpt in range (0,3):                         # Affichage de la première ligne ainsi que l'asignation des espaces du tableau
        print(" | " + str(grille[cpt]), end='')
    print(" |")
    print("  -------------")
    print("2", end='')
    for cpt in range (0,3):                         # Affichage de la deuxième ligne ainsi que l'asignation des espaces du tableau
        print(" | " + str(grille[cpt+3]), end='')
    print(" |")
    print("  -------------")
    print("3", end='')
    for cpt in range (0,3):                         # Affichage de la troisième ligne ainsi que l'asignation des espaces du tableau
        print(" | " + str(grille[cpt+6]), end='')
    print(" |")
    print("  -------------")

def peux_gagner(grille : list[str], symbole) -> int  :
    """
    peux_gagner est une fonction qui vérifie si l'IA peut gagner

    Args:
        grille (list[str]): grille de jeux

    Returns:
        int : Retourne la position de la case à jouer
    """
    cpt : int
    position : int
    
    position = -1
    
    if (grille[0] == grille[1] == grille[2] == grille[3] == grille[5] == grille[6] == grille[7] == grille[8]  == " ") and (grille[4] != " ") :          # Vérification si le joueur jouant en premier joue au milieu et ainsi le contrer 
        position = 0
    for cpt in range (0, 3) :                                                                   # Vérification de victoire par colonne
        if (grille[cpt] == grille[cpt+3] == symbole) and (grille[cpt+6] == " ") :
            position = cpt+6
        elif (grille[cpt] == grille[cpt+6] == symbole) and (grille[cpt+3] == " ") :
            position = cpt+3
        elif (grille[cpt+3] == grille[cpt+6] == symbole) and (grille[cpt] == " ") :
            position = cpt
    for cpt in range (0, 3) :                                                                   # Vérification de victoire par ligne
        if (grille[cpt*3] == grille[cpt*3+1] == symbole) and (grille[cpt*3+2] == " ") :
            position = cpt*3+2
        elif (grille[cpt*3] == grille[cpt*3+2] == symbole) and (grille[cpt*3+1] == " ") :
            position = cpt*3+1
        elif (grille[cpt*3+1] == grille[cpt*3+2] == symbole) and (grille[cpt*3] == " ") :
            position = cpt*3
    if (grille[0] == grille[4] == symbole) and (grille[8] == " ") :                           # Vérification de victoire de la diagonal gauche vers la droite
            position = 8
    elif (grille[0] == grille[8] == symbole) and (grille[4] == " ") :                         # Vérification de victoire de la diagonal gauche vers la droite
            position = 4
    elif (grille[4] == grille[8] == symbole) and (grille[0] == " ") :                         # Vérification de victoire de la diagonal gauche vers la droite
            position = 0
    elif (grille[2] == grille[4] == symbole) and (grille[6] == " ") :                         # Vérification de victoire de la diagonal droite vers la gauche
            position = 6
    elif (grille[2] == grille[6] == symbole) and (grille[4] == " ") :                         # Vérification de victoire de la diagonal droite vers la gauche
            position = 4
    elif (grille[4] == grille[6] == symbole) and (grille[2] == " ") :                         # Vérification de victoire de la diagonal droite vers la gauche
            position = 2
    return position

def tour_joueur(grille : list[str], joueur : Joueur, tour_joueur : int):
    """
    tour_joueur permet au joueur désigner de poser son symbole 

    Args:
        grille (list[str]): grille de jeu
        joueur (str): joueur qui joue
        tour_joueur (int): définit le tour du joueur
    """
    ligne : int
    colonne : int
    
    print(f"{joueur.nom}, c'est à vous de jouer !")           # Affichage du joueur jouant
    
    ligne = int(input("Quel ligne voulez-vous jouer : "))
    while ligne < 1 or ligne > 3 :
        print("La valeur rentrez est mauvaise, veuillez rentrer une ligne correcte")
        ligne = int(input("Quel ligne voulez-vous jouer : "))
        
    colonne = int(input("Quel colonne voulez-vous jouer : "))
    while colonne < 1 or colonne > 3 :
        print("La valeur rentrez est mauvaise, veuillez rentrer une colonne correcte")
        colonne = int(input("Quel colonne voulez-vous jouer : "))
        
    while grille[(ligne-1) * 3 + (colonne-1)] != " " :                  # Vérifie si la case est vide ou non si elle ne l'est pas alors le joueur doit rentrer une nouvelle ligne et colonne
        print("Cette case n'est pas libre, choisissez une autre case")
        
        ligne = int(input("Quel ligne voulez-vous jouer : "))
        while ligne < 1 or ligne > 3 :
            print("La valeur rentrez est mauvaise, veuillez rentrer une ligne correcte")
            ligne = int(input("Quel ligne voulez-vous jouer : "))
            
        colonne = int(input("Quel colonne voulez-vous jouer : "))
        while colonne < 1 or colonne > 3 :
            print("La valeur rentrez est mauvaise, veuillez rentrer une colonne correcte")
            ligne = int(input("Quel colonne voulez-vous jouer : "))
    
    if tour_joueur == 1 :
        grille[(ligne-1) * 3 + (colonne-1)] = "X"                       # Désignation du X pour le joueur 1
    else :
        grille[(ligne-1) * 3 + (colonne-1)] = "O"                       # Désignation du O pour le joueur 2
    
    Afficher_morpion(grille)
        
def tour_IA(grille : list[str], joueur : Joueur, tour_joueur : int, difficulte : int):
    """
    tour_IA permet à l'IA de poser son symbole

    Args:
        grille (list[str]): grille de jeu
        joueur (Joueur): joueur qui joue
        tour_joueur (int): définit le tour du joueur
        difficulte (int): définit la difficulté de l'IA
    """
    ligne : int
    colonne : int
    decision : int
    chercher_victoire : int
    empecher_victoire : int
    
    input(f"{joueur.nom}, c'est à vous de jouer !")           # Affichage de l'IA jouant (Morbot ou Bitoe)
    
    if difficulte == 1 :                                        # Difficulté facile
        ligne = random.randint(1, 3)                            # Génération aléatoire de la ligne
        colonne = random.randint(1, 3)                          # Génération aléatoire de la colonne
        
        while grille[(ligne-1) * 3 + (colonne-1)] != " " :                  # Vérifie si la case est vide ou non si elle ne l'est pas alors l'IA doit rentrer une nouvelle ligne et colonne
            ligne = random.randint(1, 3)                            # Génération aléatoire de la ligne
            colonne = random.randint(1, 3)                          # Génération aléatoire de la colonne
        if tour_joueur == 1 :
            grille[(ligne-1) * 3 + (colonne-1)] = "X"                       # Désignation du X pour l'IA
        else :
            grille[(ligne-1) * 3 + (colonne-1)] = "O"                       # Désignation du O pour l'IA
            
    elif difficulte == 2 :                                      # Difficulté intermédiaire
        decision = random.randint(1, 3)                         # Génération aléatoire de la décision
        if decision == 1 :                                      # Si la décision est égale à 1 alors l'IA joue aléatoirement
            ligne = random.randint(1, 3)                            # Génération aléatoire de la ligne
            colonne = random.randint(1, 3)                          # Génération aléatoire de la colonne
            
            while grille[(ligne-1) * 3 + (colonne-1)] != " " :                  # Vérifie si la case est vide ou non si elle ne l'est pas alors l'IA doit rentrer une nouvelle ligne et colonne
                ligne = random.randint(1, 3)                            # Génération aléatoire de la ligne
                colonne = random.randint(1, 3)                          # Génération aléatoire de la colonne
            if tour_joueur == 1 :
                grille[(ligne-1) * 3 + (colonne-1)] = "X"                       # Désignation du X pour l'IA
            else :
                grille[(ligne-1) * 3 + (colonne-1)] = "O"                       # Désignation du O pour l'IA
                
        else :                                                  # Si la décision est égale à 2 alors l'IA joue pour empêcher la victoire du joueur ou gagner
            chercher_victoire = peux_gagner(grille, "X")                   # Vérification si "X" peut gagner ou empêcher la victoire du joueur
            empecher_victoire = peux_gagner(grille, "O")                   # Vérification si "O" peut gagner ou empêcher la victoire du joueur
            if empecher_victoire != -1 or chercher_victoire != -1 :                          # Vérification si l'IA peut gagner ou empêcher la victoire du joueur
                if tour_joueur == 1 :
                    chercher_victoire = peux_gagner(grille, "X")                   # Vérification si l'IA peut gagner
                    empecher_victoire = peux_gagner(grille, "O")                   # Vérification si l'IA peut empêcher la victoire du joueur adverse
                    if chercher_victoire != -1 :                         # Si l'IA peut gagner ou empêcher la victoire du joueur alors elle cherche en priorité à gagner
                        grille[chercher_victoire] = "X"                       # Désignation du X pour l'IA
                    else :
                        grille[empecher_victoire] = "X"                      # Désignation du X pour l'IA
                else :
                    chercher_victoire = peux_gagner(grille, "O")                   # Vérification si l'IA peut gagner
                    empecher_victoire = peux_gagner(grille, "X")                   # Vérification si l'IA peut empêcher la victoire du joueur adverse
                    if chercher_victoire != -1 :                          # Si l'IA peut gagner ou empêcher la victoire du joueur alors elle cherche en priorité à gagner
                        grille[chercher_victoire] = "O"                       # Désignation du O pour l'IA
                    else :
                        grille[empecher_victoire] = "O"                       # Désignation du O pour l'IA
            else :
                ligne = random.randint(1, 3)                            # Génération aléatoire de la ligne
                colonne = random.randint(1, 3)                          # Génération aléatoire de la colonne
                
                while grille[(ligne-1) * 3 + (colonne-1)] != " " :                  # Vérifie si la case est vide ou non si elle ne l'est pas alors l'IA doit rentrer une nouvelle ligne et colonne
                    ligne = random.randint(1, 3)                            # Génération aléatoire de la ligne
                    colonne = random.randint(1, 3)                          # Génération aléatoire de la colonne
                if tour_joueur == 1 :
                    grille[(ligne-1) * 3 + (colonne-1)] = "X"                       # Désignation du X pour l'IA
                else :
                    grille[(ligne-1) * 3 + (colonne-1)] = "O"                       # Désignation du O pour l'IA
            
    elif difficulte == 3 :                                      # Difficulté difficile
        chercher_victoire = peux_gagner(grille, "X")                   # Vérification si "X" peut gagner ou empêcher la victoire du joueur
        empecher_victoire = peux_gagner(grille, "O")                   # Vérification si "O" peut gagner ou empêcher la victoire du joueur
        if empecher_victoire != -1 or chercher_victoire != -1 :                          # Vérification si l'IA peut gagner ou empêcher la victoire du joueur
            if tour_joueur == 1 :                       
                chercher_victoire = peux_gagner(grille, "X")                   # Vérification si l'IA peut gagner
                empecher_victoire = peux_gagner(grille, "O")                   # Vérification si l'IA peut empêcher la victoire du joueur adverse
                if chercher_victoire != -1 :                          # Si l'IA peut gagner ou empêcher la victoire du joueur alors elle cherche en priorité à gagner
                    grille[chercher_victoire] = "X"                       # Désignation du X pour l'IA
                else :  
                    grille[empecher_victoire] = "X"                      # Désignation du X pour l'IA
            else :
                chercher_victoire = peux_gagner(grille, "O")                   # Vérification si l'IA peut gagner
                empecher_victoire = peux_gagner(grille, "X")                   # Vérification si l'IA peut empêcher la victoire du joueur adverse
                if chercher_victoire != -1 :                          # Si l'IA peut gagner ou empêcher la victoire du joueur alors elle cherche en priorité à gagner
                    grille[chercher_victoire] = "O"                       # Désignation du O pour l'IA
                else :
                    grille[empecher_victoire] = "O"                       # Désignation du O pour l'IA
        else :
            ligne = random.randint(1, 3)                            # Génération aléatoire de la ligne
            colonne = random.randint(1, 3)                          # Génération aléatoire de la colonne
            
            while grille[(ligne-1) * 3 + (colonne-1)] != " " :                  # Vérifie si la case est vide ou non si elle ne l'est pas alors l'IA doit rentrer une nouvelle ligne et colonne
                ligne = random.randint(1, 3)                            # Génération aléatoire de la ligne
                colonne = random.randint(1, 3)                          # Génération aléatoire de la colonne
            if tour_joueur == 1 :
                grille[(ligne-1) * 3 + (colonne-1)] = "X"                       # Désignation du X pour l'IA
            else :
                grille[(ligne-1) * 3 + (colonne-1)] = "O"                       # Désignation du O pour l'IA
                
    Afficher_morpion(grille)
    
def est_gagnant(grille : list[str]) -> bool :
    """
    est_gagnant est une fonction qui vérifie si il y a un gagnant

    Args:
        grille (list[str]): grille de jeux

    Returns:
        bool : Retourne le résultat de la vérification sous forme d'un booléen
    """

    cpt : int
    
    resultat = False
    for cpt in range (0, 3) :                                                                   # Vérification de victoire par colonne
        if (grille[cpt] == grille[cpt+3] == grille[cpt+6]) and (grille[cpt] != " ") :
            resultat = True
    for cpt in range (0, 3) :                                                                   # Vérification de victoire par ligne
        if (grille[cpt*3] == grille[cpt*3+1] == grille[cpt*3+2]) and (grille[cpt*3] != " ") :
            resultat = True
    if (grille[0] == grille[4] == grille[8]) and (grille[0] != " ") :                           # Vérification de victoire de la diagonal gauche vers la droite
            resultat = True
    elif (grille[2] == grille[4] == grille[6]) and (grille[2] != " ") :                         # Vérification de victoire de la diagonal droite vers la gauche
            resultat = True
    
    return resultat
    
def jeu_morpionJcJ(score : Jeu):
    """Cette procédure contient l'exécution du morprion joueur contre joueur

    Args:
        score (Jeu): la variable contenant les scores
    """
    cpt : int
    grille : list[str]
    victoire : bool
    joueur1 : Joueur
    joueur1 = Joueur()
    joueur2 : Joueur
    joueur2 = Joueur()
    
    cpt = 0
    grille = [" "," "," "," "," "," "," "," "," "]

    print(TextStyle.BOLD + "Bienvenue dans le Morpion Joueur contre Joueur\n" + TextStyle.RESET)
    print("")

    #Choix des pseudos de chaque joueur avec contrôle de vérification sur la taille et si les pseudos sont identiques
    joueur1.nom = input("La personne qui prend les X (ce sera le premier à jouer) : ")
    while len(joueur1.nom)>12:
        joueur1.nom=input("Erreur, veuillez saisir un pseudo de 12 caractères maximum : ")
    print("")
    joueur2.nom = input("La personne qui prend les O : ")
    while len(joueur2.nom)>12 or joueur2.nom==joueur1.nom:
        if len(joueur2.nom)>12:
            joueur2.nom=input("Erreur, veuillez saisir un pseudo de 12 caractères maximum : ")
        else:
            joueur2.nom=input("Erreur, veuillez saisir un pseudo différent du joueur 1 : ")

    os.system("CLS")
    Afficher_morpion(grille)
    while (not(est_gagnant(grille))) and (cpt < 9) :                 # Le jeu tourne jusqu'à qu'un joueur gagne ou que les 9 cases soient remplis
        if cpt % 2 == 0 :
            tour_joueur(grille, joueur1, 1)                             # Si compteur pair alors c'est au joueur 1 de joueur
            cpt += 1
        else :
            tour_joueur(grille, joueur2, 2)                             # Si compteur impair alors c'est au joueur 2 de joueur
            cpt += 1

    victoire = est_gagnant(grille)

    if (cpt == 9) and (not(victoire)) :
        print("Fin du jeu, match nul !")
    else : 
        if victoire and (cpt % 2 == 1) :             # Vérification de condition avec compteur impair car quand le joueur 1 finit sont tour le compteur devient impair 
            print("Bravo !",joueur1.nom,"a gagné !")
            joueur1.score=1
            ajout_score(score.morpion, joueur1)
        else :                                         # Vérification de condition avec compteur pair car quand le joueur 2 finit sont tour le compteur devient pair
            print("Bravo !",joueur2.nom,"a gagné !")
            joueur2.score=1
            ajout_score(score.morpion, joueur2)

    print("")
    input("Appuyer sur entrer pour revenir au menu ")
    
def jeu_morpionJcIA(score : Jeu):
    """Cette procédure contient l'exécution du morprion en joueur contre IA

    Args:
        score (Jeu): la variable contenant les scores
    """
    cpt : int
    grille : list[str]
    victoire : bool
    joueur1 : Joueur
    joueur2 : Joueur
    choix_difficulte : int
    choix : int
    
    choix_difficulte = 0
    choix = 0
    joueur1 = Joueur()
    joueur2 = Joueur()
    cpt = 0
    grille = [" "," "," "," "," "," "," "," "," "]

    print(TextStyle.BOLD + "Bienvenue dans le Morpion Joueur contre IA\n" + TextStyle.RESET)
    print("")

    #Choix du pseudo du joueur avec contrôle de vérification sur la taille et du choix de difficulté de l'IA
    choix_difficulte= int(input("Choisissez la difficulté de l'IA (1 = facile, 2 = intermédiaire et 3 = difficile) : "))
    choix = int(input("Voulez-vous commencer ? (1 = oui, 2 = non) : "))
    while choix != 1 and choix != 2 :
        print("Erreur dans le choix, veuillez entrer un nombre entre 1 et 2\n")
        choix = int(input("Voulez-vous commencer ? (1 = oui, 2 = non) : "))
        
    if choix == 1 :
        joueur1.nom = input("Veuillez rentrez votre nom : ")
        while len(joueur1.nom)>12:
            joueur1.nom=input("Erreur, veuillez saisir un pseudo de 12 caractères maximum : ")
        print("Vous aurez les X et Morbot les O : ")
        print("")
        joueur2.nom = "Morbot"
        
        os.system("CLS")
        Afficher_morpion(grille)
        while (not(est_gagnant(grille))) and (cpt < 9) :                 # Le jeu tourne jusqu'à qu'un joueur gagne ou que les 9 cases soient remplis
            if cpt % 2 == 0 :
                tour_joueur(grille, joueur1, 1)                             # Si compteur pair alors c'est au joueur de jouer
                cpt += 1
            else :
                tour_IA(grille, joueur2, 2, choix_difficulte)                             # Si compteur impair alors c'est a Morbot de jouer
                cpt += 1

        victoire = est_gagnant(grille)

        if (cpt == 9) and (not(victoire)) :
            print("Fin du jeu, match nul !")
        else : 
            if victoire and (cpt % 2 == 1) :             # Vérification de condition avec compteur impair car quand le joueur 1 finit sont tour le compteur devient impair 
                print("Bravo !",joueur1.nom,"a gagné !")
                joueur1.score=1
                ajout_score(score.morpion, joueur1)
            else :                                         # Vérification de condition avec compteur pair car quand Morbot finit sont tour le compteur devient pair
                print("Dommage !",joueur2.nom,"a gagné !")

        print("")
        input("Appuyer sur entrer pour revenir au menu ")
        
    elif choix == 2 :    
        joueur2.nom = input("Veuillez rentrez votre nom : ")
        while len(joueur2.nom)>12 or joueur2.nom==joueur1.nom:
            while len(joueur2.nom)>12:
                joueur2.nom=input("Erreur, veuillez saisir un pseudo de 12 caractères maximum : ")
        print("Vous aurez les O et Morbot les X : ")
        print("")
        joueur1.nom = "Morbot"

        os.system("CLS")
        Afficher_morpion(grille)
        while (not(est_gagnant(grille))) and (cpt < 9) :                 # Le jeu tourne jusqu'à qu'un joueur gagne ou que les 9 cases soient remplis
            if cpt % 2 == 0 :
                tour_IA(grille, joueur1, 1, choix_difficulte)               # Si compteur pair alors c'est a Marbot de jouer
                cpt += 1
            else :
                tour_joueur(grille, joueur2, 2)                             # Si compteur impair alors c'est au joueur de jouer
                cpt += 1

        victoire = est_gagnant(grille)

        if (cpt == 9) and (not(victoire)) :
            print("Fin du jeu, match nul !")
        else : 
            if victoire and (cpt % 2 == 1) :             # Vérification de condition avec compteur impair car quand Morbot finit sont tour le compteur devient impair 
                print("Dommage !",joueur1.nom,"a gagné !")
            else :                                         # Vérification de condition avec compteur pair car quand le joueur finit sont tour le compteur devient pair
                print("Bravo !",joueur2.nom,"a gagné !")
                joueur2.score=1
                ajout_score(score.morpion, joueur2)

        print("")
        input("Appuyer sur entrer pour revenir au menu ")

def jeu_morpionIAcIA():
    """Cette procédure contient l'exécution du morprion en IA contre IA

    Args:
        score (Jeu): la variable contenant les scores
    """
    cpt : int
    grille : list[str]
    victoire : bool
    joueur1 : Joueur
    joueur2 : Joueur
    choix_difficulte_1 : int
    choix_difficulte_2 : int
    choix : int
    
    choix_difficulte_1 = 0
    choix_difficulte_2 = 0
    choix = 0
    joueur1 = Joueur()
    joueur2 = Joueur()
    cpt = 0
    grille = [" "," "," "," "," "," "," "," "," "]

    print(TextStyle.BOLD + "Bienvenue dans le Morpion IA contre IA\n" + TextStyle.RESET)
    print("")

    print("Les IA auront pour nom Morbot et BitToe")
    #Choix de difficulté de chaque IA 
    choix_difficulte_1= int(input("Choisissez la difficulté de Morbot (1 = facile, 2 = intermédiaire et 3 = difficile) : "))
    choix_difficulte_2= int(input("Choisissez la difficulté de BitToe (1 = facile, 2 = intermédiaire et 3 = difficile) : "))
    choix = int(input("Qui commence ? (1 = Morbot, 2 = BitToe) : "))
    while choix != 1 and choix != 2 :
        print("Erreur dans le choix, veuillez entrer un nombre entre 1 et 2\n")
        choix = int(input("Qui commence ? (1 = Morbot, 2 = BitToe) : "))
        
    if choix == 1 :
        joueur1.nom = "Morbot"
        joueur2.nom = "BitToe"
        print("Morbot aura les X et BitToe les O : ")
        print("")
        
        os.system("CLS")
        Afficher_morpion(grille)
        while (not(est_gagnant(grille))) and (cpt < 9) :                 # Le jeu tourne jusqu'à qu'une IA gagne ou que les 9 cases soient remplis
            if cpt % 2 == 0 :
                tour_IA(grille, joueur1, 1, choix_difficulte_1)                             # Si compteur pair alors c'est a Morbot de jouer
                cpt += 1
            else :
                tour_IA(grille, joueur2, 2, choix_difficulte_2)                             # Si compteur impair alors c'est a BitToe de jouer
                cpt += 1

        victoire = est_gagnant(grille)

        if (cpt == 9) and (not(victoire)) :
            print("Fin du jeu, match nul !")
        else : 
            if victoire and (cpt % 2 == 1) :             # Vérification de condition avec compteur impair car quand Morbot finit sont tour le compteur devient impair 
                print("Bravo !",joueur1.nom,"a gagné !")
            else :                                         # Vérification de condition avec compteur pair car quand BitToe finit sont tour le compteur devient pair
                print("Bravo !",joueur2.nom,"a gagné !")

        print("")
        input("Appuyer sur entrer pour revenir au menu ")
        
    elif choix == 2 :    
        joueur2.nom = "BitToe"
        joueur1.nom = "Morbot"

        os.system("CLS")
        Afficher_morpion(grille)
        while (not(est_gagnant(grille))) and (cpt < 9) :                 # Le jeu tourne jusqu'à qu'une IA gagne ou que les 9 cases soient remplis
            if cpt % 2 == 0 :
                tour_IA(grille, joueur2, 1, choix_difficulte_2)               # Si compteur pair alors c'est a BitToe de jouer
                cpt += 1
            else :
                tour_IA(grille, joueur1, 2, choix_difficulte_1)                             # Si compteur impair alors c'est a Morbot de jouer
                cpt += 1

        victoire = est_gagnant(grille)

        if (cpt == 9) and (not(victoire)) :
            print("Fin du jeu, match nul !")
        else : 
            if victoire and (cpt % 2 == 1) :             # Vérification de condition avec compteur impair car quand BitToe finit sont tour le compteur devient impair 
                print("Bravo !",joueur2.nom,"a gagné !")
            else :                                         # Vérification de condition avec compteur pair car quand Morbot finit sont tour le compteur devient pair
                print("Bravo !",joueur1.nom,"a gagné !")

        print("")
        input("Appuyer sur entrer pour revenir au menu ")

def menu_morpion(score : Jeu):
    """Cette procédure permet la gestion du menu morpion

    Args:
        score (Jeu): la variable contenant les scores
    """

    choix : int #Variable permettant de gérer le premier menu
    choix=0
    
    while(choix!=5):

        affiche_menu_jeu("Devin'ombre  ")
        choix=int(input("Saisir votre choix : "))
        if choix==1 : #exécution du jeu
            os.system("CLS")
            jeu_morpionJcJ(score)
        elif choix==2: 
            os.system("CLS")
            jeu_morpionJcIA(score)
        elif choix==3: 
            os.system("CLS")
            jeu_morpionIAcIA()
        elif choix==4: 
            affiche_regles_morpion()
        elif choix==5: #retour au menu principal
            print("")  #On ne fait rien comme on retourne au menu précédent
        else :
            print("")
            print("Erreur dans le choix, veuillez entrer un nombre entre 1 et 5\n")
            print("")
            input("Appuyer sur entrer pour modifier votre choix")  