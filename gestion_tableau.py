from structures import *

def tri_par_insertion(tab: list[Joueur]):
    """Cette procédure tri un tableau de joueur par le score avec la méthode du tri par insertion. Ce tri est décroissant

    Args:
        tab (list[Joueur]): un tableau de joueur possédant un nom et un score
    """
    cpt : int
    cpt2 : int
    joueur_temp: Joueur

    for cpt in range(1, len(tab)):
        joueur_temp = tab[cpt]
        cpt2 = cpt - 1
        while cpt2 >= 0 and tab[cpt2].score < joueur_temp.score:
            tab[cpt2 + 1] = tab[cpt2]
            cpt2 -= 1
        tab[cpt2 + 1] = joueur_temp

def recherche_nom_joueur(tab : list[Joueur], joueur_cherche:str)->int:
    """Cette fonction retourne la place d'un élément d'un tableau joueur si il y a une correspondance entre le nom
    recherché et un nom de joueur du tableau

    Args:
        tab (list[Joueur]): un tableau de joueur contenant un score et un nom
        joueur_cherche (str): le nom du joueur que l'on cherche

    Returns:
        int: la place du joueur dans le tableau ou -1 si il n'est pas présent
    """
    place : int
    cpt :int

    place = -1
    cpt = 0

    while (place==-1) and (cpt<len(tab)):
        if joueur_cherche==tab[cpt].nom:
            place=cpt
        cpt+=1
    return place

def ajout_score(tab : list[Joueur], joueur : Joueur):
    """
    ajout_score 

    Permet d'ajouter un score à un tableau de joueur. Si le joueur existe on vient additioner son score
    sinon on ajoute un nouveau joueur au tableau de joueur

    Args:
        tab (list[Joueur]): tableau de joueur 
        joueur (Joueur): un joueur (ici le gagnant d'un jeu)
    """

    place=recherche_nom_joueur(tab, joueur.nom)
    #Si le joueur existe on ajoute son score à son ancien score sinon on crée un nouveau joueur
    if place==-1 :
        tab.append(joueur)
    else :
        tab[place].score+=joueur.score
    
