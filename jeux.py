"""
Ce module contient l'ensemble des mini-jeux utilisés dans le jeu principal,
ainsi que les données qui servent à alimenter ces jeux.
"""
import random as rd
import string
import sys
import time
from math import sin, cos, acos, pi



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

# 2. Table des exceptions à prendre en compte dans la liste de mots français (pour le jeu du pendu)
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
            ### 5 pièces d'or ###
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
                       ### 40 pièces d'or ###
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
                  ### 150 pièces d'or ###
"""
                }

# 4. Création des messages de victoire et de Défaite pour le trésor
vict = """
╔══════════════════╗
║     VICTOIRE     ║
║ 500 pièces d'or  ║ 
╚══════════════════╝
"""

defa = """
╔══════════════════╗
║     DÉFAITE      ║
║    Tu es ruiné   ║ 
╚══════════════════╝
"""
# 5 . Création des listes de Noms et de Prénoms pour la Taverne (pardon pour les noms !! )
listeNom = ["Zanin","Mustière","Ribardière","Van Hamme","Boulier","Cura","Commenges","Fritsch","Payet","Gautier"]
listePrenom = ["Christine","Sébastien","Antonine","Adrien","Joel","Robin","Hadrien","Emmanuel","Nicolas","Jacques"]


# 6. Alphabet
# utile dans le cas de la bataille navale
alphabet = dict(zip([i+1 for i in range(26)],string.ascii_uppercase ))



#### FONCTIONS ####
def get_key(val,dictionnaire):
    """
    Permet d'obtenir la clé en ayant une valeur d'un dictionnaire
    :param val:
    Valeur dans le dictionnaire
    :param dictionnaire: dict
    Dictionnaire dans lequel on fait la recherche
    :return: key
    La clé qui correspond à la valeur
    """
    for key, value in dictionnaire.items():
        if val == value:
            return key
    return "La clé n'existe pas"


def deg2rad(dd):
    """
    Convertit un angle "degrés décimaux" en "radians"
    :param dd: float
    :return: float
    """
    return dd / 180 * pi
def rad2deg(rd):
    """
    Convertit un angle "radians" en "degrés décimaux"
    :param rd: float
    :return: float
    """
    return rd / pi * 180

def distanceGPS(latitude1, longitude1, latitude2, longitude2, unit='kilometers'):
    """
    Fonction de calcul d'une distance sur la Terre issu de la source suivante :
    https://fr.martech.zone/calculate-great-circle-distance/

    :param latitude1:
    :param longitude1:
    :param latitude2:
    :param longitude2:
    :param unit:
    :return:
    """
    theta = longitude1 - longitude2
    distance = 60 * 1.1515 * rad2deg(
        acos(
            (sin(deg2rad(latitude1)) * sin(deg2rad(latitude2))) +
            (cos(deg2rad(latitude1)) * cos(deg2rad(latitude2)) * cos(deg2rad(theta)))
        )
    )
    if unit == 'miles':
        return round(distance, 2)
    if unit == 'kilometers':
        return round(distance * 1.609344, 2)

def colorer(message, couleur):
    """
    Fonction issue du fichier exemple.py enrichi avec la couleur jaune
    :param message:
    :param couleur:
    :return:
    """
    couleurs = {"vert": "\033[92m","grisclair": "\033[37m","bleu": "\033[34m","jaune":'\033[93m', "rouge": "\033[91m", "normal": "\033[0m"}
    return couleurs[couleur] + message + couleurs["normal"]

def barre_chargement(tps=0.1, icone=colorer("■","rouge"), mot="",longueur=20):
    """
    Permet de faire une barre de chargement dans la console
    :param tps: float
    Temps de chargement
    :param icone: str
    Les icônes de chargement
    :param mot: string
    Si on veut mettre un mot au milieu
    :param longueur: int
    La longueur de la barre
    :return: string
    La barre de chargement
    """
    toolbar_width = longueur
    for i in range(toolbar_width):
        time.sleep(tps)
        # avancement de la barre
        if i == 10:
            sys.stdout.write(mot)
        sys.stdout.write(icone)

        sys.stdout.flush()

    sys.stdout.write("\n")

## Jeu pierre-papier-ciseaux
# Inutile pour le moment
def pierre_papier_ciseaux(x):
    """
    Jeu pierre papier ciseaux
    :param x: int
    En combien
    :return: None
    """

    scoreJoueur = 0
    scoreOrdi = 0
    dict = {"pierre": 0, "papier": 1, "ciseaux": 2}
    i = 0
    SO, SA, X = [],[],[]

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


## Jeu du pendu
def remplace(mot):
    """
    Nettoie un mot en enlevant les lettres avec accent ou lettres particulières
    :param mot: str
    Le mot non nettoyé
    :return: str
    Le mot nettoyé
    """
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
    Jeu du pendu, possibilité de jouer avec un mot au hasard d'une liste en français, ou possibilité de chosir le mot
    :param liste: list
    Une liste de mot français
    :param mot_precis:
    Le mot à faire deviner
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

## Jeux devinettes
def devine_les_coords(LatAtrouver,LongAtrouver, tour = 8):
    """
    Deviner une latitude et une longitude (être à moins de 10 km
    :param LatAtrouver: float
    La latitude recherchée
    :param LongAtrouver: float
    La longitude recherchée
    :param tour: int
    En combien de coups
    :return: boolean
    Victoire ou pas
    """

    n=0
    while n <= tour:
        n+=1
        Lat = input("Tape la latitude : ")
        Long = input("Tape la longitude : ")


        try:
            Lat, Long = float(Lat), float(Long)
            dist = distanceGPS(LatAtrouver, LongAtrouver, Lat, Long)
            if dist<=200:
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

def devine_la_dist(coords,LatB,LongB,tour = 8):
    """
    Deviner la distance du bateau à un port bien précisé par ses coordonnées
    :param coords: list
    Liste des coordonnées d'un point (le port)
    :param LatB: float
    La latitude du bateau
    :param LongB: float
    La longitude du bateau
    :param tour: int
    En combien de coups
    :return: boolean
    Victoire ou pas
    """
    distance_bateau_port=distanceGPS(coords[1],coords[0],LatB,LongB)
    n = 0
    while n <= tour:
        n += 1
        D = input("Estime la distance en km : ")

        try:
            D = int(D)
            if abs(D-distance_bateau_port) <= 10:
                print(colorer("Bravo, tu es à moins de 10km !","vert"))
                print("Distance réelle : ", distance_bateau_port)
                print('')
                return True
            else:
                if abs(D-distance_bateau_port) >= 100:
                    print("Oulala, tu es encore loin !")
                    if D > distance_bateau_port:
                        print("Essaye beaucoup moins")
                    else:
                        print("Essaye beaucoup plus")
                else:
                    print("Tu t'approches !")
        except:
            print("Entre une vraie distance en km marin d'eau douce !")


## Bataille Navale
def affiche_quadrillage(liste,type = 0):
    """
    Affichage de la grille dans la console
    :param liste: list
    La liste qui correspond au plateau de jeu
    :param type: int
    Entier qui permet de changer la couleur si on veut afficher la grille du joueur ou de l'adversaire
    :return: str
    Le plateau
    """
    carte = ''
    ligne_finale='  '
    for i in range(len(liste)):
        carte += str(i+1)+' '
        for j in range(len(liste[0])):
            if liste[i][j] == 0:
                if type ==1:
                    carte+=colorer('■ ',"bleu")
                else:
                    carte += colorer('■ ', "grisclair")
            elif liste[i][j] == 50:
                carte+=colorer('♦ ',"rouge")
            else:
                carte += colorer('♦ ',"jaune")
        carte += '\n'
        ligne_finale += alphabet[i+1]+' '
    carte += ligne_finale
    print(carte)

def conv_pos(pos):
    """
    Convertisseur d'une postition, par exemple 'A2' sous la forme de coordonnées du tableau python
    ex/ 'A2' sera converti en [1,0] car 'A2' et la case du tableau t tel que 'A2' = T[1][0]
    :param pos:str
    Une position littérale par exemple 'A2'
    :return: list
    Une position comprise par Python par exemple [1,0]
    """
    tab_coords=[]
    tab_coords.append(int(pos[1::])-1)
    tab_coords.append(get_key(pos[0].upper(),alphabet)-1)
    return tab_coords

def conv_coords(tab_coords):
    """
    Convertisseur de coordonnées du tableau python, par exemple [1,0] sous la forme d'une postition
    ex/ [1,0] sera converti en 'A2' car 'A2' et la case du tableau t tel que 'A2' = T[1][0]
    :param tab_coords:list
    Une position comprise par Python par exemple [1,0]
    :return: str
    Une position littérale par exemple 'A2'

    """
    pos=''
    pos+=alphabet[tab_coords[1]+1]
    pos+=str(tab_coords[0]+1)
    return pos

def detection(grille):
    """
    Renvoie False si Coulé
    :param grille: list
    plateau de jeu python
    :return: boolean
    True s'il reste des parties à couler, False sinon
    """
    for i in range(len(grille)):
        for j in range(len(grille)):
            if grille[i][j]==100:
                return True
    return False

def intelligence_ordi(liste,case,tailleJoueur,x):
    """
    Un fois touché, l'ordi ne doit viser que les cases sur lesquels le bateau peut se situer
    Ce programme prend la liste de l'ensemble des possibilités de tire et la restreint aux cases possibles

    :param liste: list
    Liste des cases qu'il reste à l'ordi pour tirer un missile
    :param case: string
    La case qui a été touchée à partir de laquelle il faut raisonner
    :param tailleJoueur: int
    La taille du bateau du joueur pour savoir où chercher autour
    :param x: int
    la taille du plateau
    :return: list
    La liste restreinte aux seules possibilités maintenant
    """
    # 1. On trouve les coordonnées de la case où se trouve une partie du bateau
    coords = conv_pos(case)

    # 2. On fait une liste en croix des cases où le bateau peut se trouver
    croix=[]
    for i in range(-tailleJoueur+1,tailleJoueur):
        for j in range(-tailleJoueur+1,tailleJoueur):
            if i*j == 0 and i!=j: # condition qui ne garde que les cases en dessous au au dessus (cases potentielles)
                if coords[0]+i >= x or coords[0]+i < 0 or coords[1]+j >= x or coords[1]+j < 0:
                    # la case est en dehors de la grille
                    pass
                else:
                    case_possible = conv_coords([coords[0]+i,coords[1]+j])
                    croix.append(case_possible)

    # 3. On élimine les cases de cette croix qui ont déjà été testées
    croix_nettoye=[]
    for position in croix:
        if position in liste:
            croix_nettoye.append(position)

    return croix_nettoye



def bataille_navale(x, tailleJoueur,tailleOrdi):
    """
    Jeu de la bataille Navale
    :param x: int
    Taille du plateau qui est carré
    :param tailleJoueur: int
    Taille du bateau du joueur
    :param tailleOrdi: int
    Taille du bateau de l'ordi
    :return: bool
    True en cas de victoire, False en cas de défaite
    """

    # 1. Initialisation des grilles joueur et Ordi
    print(f"Bienvenue dans la bataille navale sur un plateau ({x}x{x})")
    print("Taille du bateau du joueur : ",tailleJoueur)
    print("Taille du bateau de l'adversaire : ",tailleOrdi)
    grilleJ1 = [[0 for i in range(x)] for j in range(x)]
    grilleOrdi = [[0 for i in range(x)] for j in range(x)]

    ## Création d'une liste de l'ensemble des positions possibles dans la grille
    ## Cette liste sera utilisée pour éviter à l'ordi de taper 2 fois au même endroit
    cases_possibles=[]
    for i in range(x):
        for j in range(x):
            case = alphabet[i+1]+str(j+1)
            cases_possibles.append(case)


    # 2. Placement des bateaux
    ## Placement du bateau du joueur
    affiche_quadrillage(grilleJ1,1)
    print("Commence par positionner ton bateau sur le plateau.")
    sens = None
    if tailleJoueur > 1:
        while sens != 'V' and sens != 'H':
            sens = input("Vertical ou horizontal ? [Tape v ou h] ")
            sens = sens.upper()

    while True:
        try:
            test_proue = False
            while not test_proue: #on vérifie que l'on peut bien positionner le bateau dans le quadrillage
                proue = input("Tape la case correspondant à la proue de ton bateau (ex A2) : ")
                coords_proue = conv_pos(proue)

                # On vérifie que la case choisie est bien dans le plateau
                if coords_proue[0] >= x or coords_proue[0] < 0 or coords_proue[1] >= x or coords_proue[1] < 0:
                    print("Ne sors pas du plateau Ectoplasme !!!")
                else:
                    if sens == 'V':
                        if x-coords_proue[0] <2 : #bateau placé trop bas
                            print("Recommence, ici c'est pas possible")
                        else: #on place le bateau
                            grilleJ1[coords_proue[0]][coords_proue[1]] = 100
                            for i in range(tailleJoueur-1):
                                grilleJ1[coords_proue[0]+(i+1)][coords_proue[1]] = 100
                            test_proue = True

                    elif sens == 'H':
                        if x-coords_proue[1] <2: #bateau trop à droite
                            print("Recommence, ici c'est pas possible")
                        else: #on place le bateau
                            grilleJ1[coords_proue[0]][coords_proue[1]] = 100
                            for i in range(tailleJoueur-1):
                                grilleJ1[coords_proue[0]][coords_proue[1]+(i+1)] = 100
                            test_proue = True
                    else:
                        grilleJ1[coords_proue[0]][coords_proue[1]] = 100
                        test_proue = True
            break
        except ValueError:
            print("Tu ne tapes pas une case valide")
            print("Tape quelque chose du type 'a2' ou 'D9', c'est pas compliqué !")

    ## Placement du bateau de l'ordi
    sens = None
    if tailleOrdi > 1:
        d = rd.randint(0,1)
        if d == 0:
            sens='V'
        else:
            sens='H'

    positionne = False
    while not positionne:
        coords_proue_ordi = [rd.randint(0, tailleOrdi - 1), rd.randint(0, tailleOrdi - 1)]
        if sens == 'V':
            if x - coords_proue_ordi[0] < 2:  # bateau placé trop bas au hasard
                # Il faut recommencer le tirage au sort
                pass
            else:  # on place le bateau
                grilleOrdi[coords_proue_ordi[0]][coords_proue_ordi[1]] = 100
                for i in range(tailleOrdi - 1):
                    grilleOrdi[coords_proue_ordi[0] + (i + 1)][coords_proue_ordi[1]] = 100
                positionne = True

        elif sens == 'H':
            if x - coords_proue_ordi[1] < 2:  # bateau placé trop à droite au hasard
                # Il faut recommencer le tirage au sort
                pass
            else:  # on place le bateau
                grilleOrdi[coords_proue_ordi[0]][coords_proue_ordi[1]] = 100
                for i in range(tailleOrdi - 1):
                    grilleOrdi[coords_proue_ordi[0]][coords_proue_ordi[1] + (i + 1)] = 100
                positionne = True
        else:
            grilleOrdi[coords_proue_ordi[0]][coords_proue_ordi[1]] = 100
            positionne = True

    affiche_quadrillage(grilleJ1,1)
    print("Grille du joueur")
    
    """
    #Affichage de la grille de l'ordi
    affiche_quadrillage(grilleOrdi)
    print("Grille de l'ordi")
    """


    # 2. Jeu
    Tour=True

    while detection(grilleJ1) or detection(grilleOrdi):
        if Tour:
            print("A ton tour, tire un boulet de canon !")
            while True:
                try:
                    missile = input("Tape une case (ex A2) : ")
                    coords_missile = conv_pos(missile)
                    break
                except ValueError:
                    print("Tu ne tapes pas une case valide")
                    print("Tape quelque chose du type 'a2' ou 'D9', c'est pas compliqué bachi-bouzouks!")
            # On vérifie que la case choisie est bien dans le plateau
            if coords_missile[0] >= x or coords_missile[0] < 0 or coords_missile[1] >= x or coords_missile[1] < 0:
                print("Ne sors pas du plateau Ectoplasme !!!")
            else:
                if grilleOrdi[coords_missile[0]][coords_missile[1]] == 0:
                    print("Plouf, dans la mer")
                    Tour = not Tour
                elif grilleOrdi[coords_missile[0]][coords_missile[1]] == 100:
                    print(colorer("Touché","vert"))
                    grilleOrdi[coords_missile[0]][coords_missile[1]] = 50
                else:
                    print("Tu as déjà tiré ici, tu perds la boule")

            # Test pour la victoire ou la défaite
            if not detection(grilleOrdi):
                print(colorer("BRAVO, c'est une belle victoire","bleu"))
                return True

        else:
            print(colorer("Attention, l'adversaire va attaquer","jaune"))
            barre_chargement(0.4,"•",longueur=4)
            # On empêche l'ordinateur de tirer deux fois au même endroit
            # On pioche le missile dans la liste puis on enlève
            indice_missile = rd.randint(0, len(cases_possibles) - 1)
            case_vise = cases_possibles[indice_missile]
            print("On t'attaque en ", case_vise)
            missile = conv_pos(cases_possibles[indice_missile])

            # on enlève l'élément de la liste des possibilités
            cases_possibles.pop(indice_missile)

            if grilleJ1[missile[0]][missile[1]] == 0:
                print("Chanceux ! C'est dans la mer")
                Tour = not Tour
            elif grilleJ1[missile[0]][missile[1]] == 100:
                print(colorer("Tu es touché","rouge"))
                grilleJ1[missile[0]][missile[1]] = 50

                # on restreint les possibilités de l'ordi
                cases_possibles = intelligence_ordi(cases_possibles, case_vise, tailleJoueur, x)

            affiche_quadrillage(grilleJ1)

            if not detection(grilleJ1):
                print(colorer("DEFAITE","rouge"))
                return False



