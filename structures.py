# Codes ANSI pour les couleurs du texte
class TextStyle:
    # Styles de texte
    RESET = "\033[0m"
    BOLD = "\033[1m"
    UNDERLINE = "\033[4m"
    BLINK = "\033[5m"
    INVERT = "\033[7m"

    # Couleurs du texte
    RED = "\033[91m"
    GREEN = "\033[92m"
    YELLOW = "\033[93m"
    BLUE = "\033[94m"
    MAGENTA = "\033[95m"
    CYAN = "\033[96m"
    WHITE = "\033[97m"

    # Arrière-plans colorés
    BG_RED = "\033[101m"
    BG_GREEN = "\033[102m"
    BG_YELLOW = "\033[103m"
    BG_BLUE = "\033[104m"
    BG_MAGENTA = "\033[105m"
    BG_CYAN = "\033[106m"
    BG_WHITE = "\033[107m"

class Joueur:
    nom:str
    score:int

class Jeu:
    devinette:list[Joueur]
    allumettes:list[Joueur]
    morpion:list[Joueur]
    puissance4:list[Joueur]