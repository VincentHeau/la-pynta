"""
Ce module contient l'ensemble des mini-jeux utilisés dans le jeu principal,
ainsi que les données qui servent à alimenter ces jeux.
"""
import random as rd
import time
import sys
from math import sin, cos, acos, pi
import carthaPirates


#### DATA ####

# 1. Création d'une liste de mots en français pour le jeu du pendu
fileObject = open("liste_francais.txt", "r")
data = fileObject.read()
mot = ''
liste_mot = []

for i in data:
    if i == '\n':
        liste_mot.append(mot)
        mot = ''
    else:
        mot = mot + i

# 2. Table des exceptions à prendre en compte dans la liste de mots français
exceptions = {'éèêẽ': 'e',
              'ç': 'c',
              'àâã': 'a',
              'ù': 'u',
              'œ': 'oe'
              }

# 2. Création d'une liste d'affichage pour les étapes du pendu
Affichage = [r"""      
   /|\
  / | \
 /  |  \
           """,
             r"""      
    |        
    |        
    |       
    |       
    |      
    |       
    |       
    |       
   /|\     
  / | \
 /  |  \
           """,
             r"""      
    _____________
    |        
    |        
    |       
    |       
    |      
    |       
    |        
    |       
   /|\ 
  / | \
 /  |  \
           """,
             r"""      
    _____________
    |        |
    |        |
    |       
    |      
    |      
    |        
    |        
    |       
   /|\ 
  / | \
 /  |  \
           """,
             r"""      
   _____________
   |        |
   |        |
   |       / \
   |       \ /
   |      
   |        
   |        
   |       
  /|\     
 / | \
/  |  \
           """,
             r"""      
   _____________
    |        |
    |        |
    |       / \
    |       \ /
    |      __|__
    |        |
    |        |
    |       
   /|\
  / | \
 /  |  \
           """,
             r"""      
    _____________
    |        |
    |        |
    |       / \
    |       \ /
    |      __|__       ಠ‿ಠ 
    |        |
    |        |
    |       / \
   /|\     /   \
  / | \   
 /  |  \
 
           """]

# 3. Création du dictionnaire des embarcations en code ASCII:

embarcations = {'Chaloupe': r"""
               
       
   _______________________________________/
      \         La Pynta (yawl)        _/
       \_____________________________/

""",
                'Navire': r"""
                                  |
                                -----
                                )___(
                                  |
                               -------
                              /       \
                             /_________\
                                  |
                            -------------
                           /             \
                          /_______________\
            _____________________|_________________/
               \  *        La Pynta (Vessel)     _/
                \_______________________________/

                """,
'Caravelle': r"""
                |
              -----                    |
              )___(                  -----
                |                    )___(
            ---------                  |
           /         \              -------
          /___________\            /       \
                |                 /_________\
         ---------------               |
        /               \        -------------
       /                 \      /             \
      /___________________\    /_______________\
    ____________|______________________|__________
     \_  µ           HMS La Pynta              _/
       \______________________________________/

"""
                }


#### FONCTIONS ####

def dms2dd(d, m, s):
    """Convertit un angle "degrés minutes secondes" en "degrés décimaux"
    """
    return d + m / 60 + s / 3600



def dd2dms(dd):
    """Convertit un angle "degrés décimaux" en "degrés minutes secondes"
    """
    d = int(dd)
    x = (dd - d) * 60
    m = int(x)
    s = (x - m) * 60
    return d, m, s

def deg2rad(dd):
    """Convertit un angle "degrés décimaux" en "radians"
    """
    return dd / 180 * pi


def rad2deg(rd):
    """Convertit un angle "radians" en "degrés décimaux"
    """
    return rd / pi * 180


def distanceGPS(latA, longA, latB, longB):
    """Retourne la distance en mètres entre les 2 points A et B connus grâce à
       leurs coordonnées GPS (en radians).
    """
    # Rayon de la terre en mètres (sphère IAG-GRS80)
    RT = 6378 #en km
    # angle en radians entre les 2 points
    S = acos(sin(latA) * sin(latB) + cos(latA) * cos(latB) * cos(abs(longB - longA)))
    # distance entre les 2 points, comptée sur un arc de grand cercle
    return round(S * RT)
def colorer(message, couleur):
    """
    Fonction issue du fichier exemple.py enrichi avec la couleur jaune
    :param message:
    :param couleur:
    :return:
    """
    couleurs = {"vert": "\033[92m","jaune":'\033[93m', "rouge": "\033[91m", "normal": "\033[0m"}
    return couleurs[couleur] + message + couleurs["normal"]

def remplace(mot):
    mot_remplace = ''
    for lettre in mot:
        for ex in exceptions:
            if lettre in ex:
                lettre = exceptions[ex]
                break
        mot_remplace += lettre
    return mot_remplace


# Test unitaire pour vérifier que la fonction de remplacement marche bien
# print(remplace("illétrédzàçœ"))


def barre_chargement(tps=0.1, icone=colorer("■","rouge"), mot=""):
    toolbar_width = 20
    for i in range(toolbar_width):
        time.sleep(tps)
        # avancement de la barre
        if i == 10:
            sys.stdout.write(mot)
        sys.stdout.write(icone)

        sys.stdout.flush()

    sys.stdout.write("\n")


def devine_les_coords(LatAtrouver,LongAtrouver, tour = 8):
    """
    :param nombreATrouver:
    :return:
    """

    n=0
    while n <= tour:
        n+=1
        Lat = input("Tape la latitude : ")
        Long = input("Tape la longitude : ")


        try:
            Lat, Long = int(Lat), int(Long)
            dist = distanceGPS(LatAtrouver, LongAtrouver, Lat, Long)
            if dist<=100:
                print("Bravo, tu es à moins de 100km !")
                print("Coordonnées réelles : (",LatAtrouver,",",LongAtrouver,")")
                return True
            else:
                if dist>=1000:
                    print("Oulala, ça part mal, tu te trompes de ",dist,"km")
                else:
                    print("Rapproche toi encore, tu es à ", dist,"km")
        except:
            print("Entre de vraies coordonnées géographiques en dégrés décimaux marin d'eau douce !")
    return False


def devine_la_dist(idPort,LatB,LongB,tour = 8):

    coords = carthaPirates.recupererCoordsPort(idPort)  # On réutilise l'identifiant du port choisi
    distance_bateau_port=distanceGPS(coords[1],coords[0],LatB,LongB)
    n = 0
    while n <= tour:
        n += 1
        D = input("Estime la distance en km : ")

        try:
            D = int(D)
            if distance_bateau_port <= 10:
                print("Bravo, tu es à moins de 10km !")
                print("Distance réelle : ", distance_bateau_port)
                return True
            else:
                if distance_bateau_port >= 100:
                    print("Oulala, tu es encore loin !")
                else:
                    print("Tu t'approches !")
        except:
            print("Entre une vraie distance en km marin d'eau douce !")


def match(x):
    """
    :return:
    """
    scoreJoueur = 0
    scoreOrdi = 0
    dict = {"pierre": 0, "papier": 1, "ciseaux": 2}
    i = 0
    SO, SA, X = []

    while ((scoreJoueur < x and scoreOrdi < x)):
        choixJoueur = input('Tapez "pierre", "papier" ou "ciseaux" : ')
        choixJoueur = choixJoueur.lower()
        while choixJoueur not in dict:
            print("ecris correctement wesh!")
            choixJoueur = input('Tapez "pierre", "papier" ou "ciseaux"')
            choixJoueur = choixJoueur.lower()

        i += 1
        choixJoueur = dict[choixJoueur]
        # Choix ordi entre 0 et 2
        choixOrdi = rd.randint(0, 2)
        if (choixOrdi == choixJoueur):
            print("Egalité!")
        elif ((choixOrdi == 0 and choixJoueur == 2) or (choixOrdi == 1 and choixJoueur == 0) or (
                choixOrdi == 2 and choixJoueur == 1)):
            print("Ordi marque un point")
            scoreOrdi += 1
        else:
            print("Joueur marque un point")
            scoreJoueur += 1

        SA.append(scoreJoueur)
        SO.append(scoreOrdi)
        LINE = [x for j in range(i)]
        X.append(i)

        print(f"Le joueur a {scoreJoueur} points")
        print(f"L'ordi a {scoreOrdi} points")

    # Affichage du gagnant!
    if (scoreJoueur > scoreOrdi):
        print("Le joueur a gagné")
        print("L'ordi a gagné")


def dedoublonner():
    tailleTab = int(input("Veuillez saisir une taille de tableau : "))
    tab = []
    tabSDoublon = []

    for i in range(0, tailleTab):
        saisieUtilisateur = int(input("Saisir une valeur : "))
        tab.append(saisieUtilisateur)

    # Fonction qui renvoie un tableau trié
    tab.sort()
    tabSDoublon.append(tab[0])

    for i in range(1, tailleTab):
        if tab[i - 1] != tab[i]:
            tabSDoublon.append(tab[i])

    return (tabSDoublon)


def affichage(liste):
    """
    Fonction qui sert à afficher proprement les listes du pendu à l'écran
    :param liste:
    :return: string
    Chaîne de caractère à afficher
    """
    str = ''
    for lettre in liste:
        if lettre == '_':
            str += '_ '
        else:
            str += lettre.upper()
            str += ' '
    return (str)


def pendu(liste, mot_precis=None):
    """
    :param liste:
    :param mot_precis:
    :return: Booléen
    True en cas de victoire et False en cas de défaite
    """
    # On sélectionne le mot à faire deviner
    if mot_precis != None:
        mot = mot_precis  # un mot precis entré en parmètre
    else:
        mot = liste[rd.randint(0, len(liste_mot) - 1)]  # un mot aléatoire d'une liste de mots français

    mot = remplace(mot)
    liste_pleine = str.strip(mot)
    liste_vide = ["_" for i in range(len(liste_pleine))]
    liste_mv_choix = []

    compteur = 0
    TF = True
    trouve = 0

    while trouve < len(liste_pleine):
        TF = False
        choix = input("Choisis une lettre Pirate ! -> ")
        choix = choix.lower()
        choix = remplace(choix)

        if choix in liste_vide:
            print("Tu as déjà entré cette lettre tu n'as pas bonne mémoire")
            print(affichage(liste_vide))
        else:
            for i in range(len(liste_pleine)):
                if choix == liste_pleine[i]:
                    TF = True
                    liste_vide[i] = choix
                    trouve += 1

            if TF:
                print("Bien joué")
                print(affichage(liste_vide))
            else:
                compteur += 1
                liste_mv_choix.append(choix)
                print(Affichage[compteur - 1])
                print("Liste des mauvais choix:")
                print(affichage(liste_mv_choix))
                print('Mot à trouver :')
                print(affichage(liste_vide))

            if compteur == 7:
                print("Tu as perdu, il fallait trouver ", mot.upper())
                return False

    print("Bravo tu es super fort")
    return True


def transform():
    """

    :param tableau:
    :return:
    """
    tab = []
    for numligne in range(4):
        ligne = []
        for numcolonne in range(4):
            ligne.append(1)
        tab.append(ligne)

    nbTabL = len(tab)
    nbTabC = len(tab[0])

    for i in range(nbTabL):
        for j in range(nbTabC):
            if i == j:
                tab[i][j] = tab[i][j] * 2
            if ((i == 0) or (i == nbTabL - 1)):
                tab[i][j] = tab[i][j] + 1
            elif ((j == 0) or (j == nbTabC - 1)):
                tab[i][j] = tab[i][j] + 1

    print(tab)
