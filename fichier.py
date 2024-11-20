from structures import *
import pickle
from typing import BinaryIO

def teste_existence_fichier(nom_fichier : str)->bool:
    """Cette fonction teste l'existence d'un fichier

    Args:
        nom_fichier (str): une chaine valide constituant le nom du fichier que l'on cherche

    Returns:
        bool: retourne false si le fichier n'existe pas et true si le fichier existe
    """
    try:
        with open(nom_fichier, 'r'):
            return True
    except FileNotFoundError:
        return False

def sauvegarder_classe(classe : Jeu, nom_fichier : str):
    """Cette procédure permet d'enregistrer la classe jeu dans le fichier spécifié

    Args:
        classe (Jeu): une classe jeu contenant des données
        nom_fichier (str): un nom de fichier valide
    """
    print("Sauvegarde des scores en cours, ne pas fermer la console avant la fin de la sauvegarde...")
    print("")
    output = open(nom_fichier, "wb")
    pickle.dump(classe, output)
    output.close()
    print("Sauvegarde des scores bien effectuée.")

def lire_classe(nom_fichier : str)->Jeu:
    """Cette fonction permet de charger la classe Jeu stocker dans un fichier

    Args:
        nom_fichier (str): nom du fichier qui stocke la classe

    Returns:
        Jeu: retourne la classe Jeu téléchargé
    """
    ma_classe : Jeu
    ma_classe = Jeu()
    ma_classe.allumettes = []
    ma_classe.devinette = []
    ma_classe.morpion = []
    ma_classe.puissance4 = []
    input : BinaryIO

    fichier_existe:bool

    print("Chargement des scores...")
    print("")

    fichier_existe=teste_existence_fichier(nom_fichier)

    #Si le fichier existe, charge les données du fichier dans ma_classe
    if fichier_existe:
        input = open(nom_fichier, "rb")
        ma_classe = pickle.load(input)
        input.close()
        print("Chargement terminé, vous pouvez accéder au menu.")
    #Sinon, si aucun fichier n'est déjà chargé, affiche un message d'absence de fichier de sauvegarde
    else :
        print("Aucun fichier de sauvegarde détecté, vous pouvez accéder au menu")
    print("")

    return ma_classe


