"""
Ce module contient l'ensemble des mini-jeux utilisés dans le jeu principal,
ainsi que les données qui servent à alimenter ces jeux.
"""
import random as rd
import time
import sys
from math import sin, cos, acos, pi
import carthaPirates
from navigateur import Navigateur
import string

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

# 4. Création du dictionnaire du butin à voler dans les ports
butinPort={1:300,2:300,3:300,4:300,5:300,6:300,7:300,8:300,9:300,10:300,11:300,12:300,13:300,14:300,15:300,16:300,
           17:300,18:300,19:300,20:300,}

# 5 . Création des listes de Noms et de Prénoms pour la Taverne
listeNom = ["Zanin","Mustière","Ribardière","Van Hamme","Boulier","Cura","Commenges","Fritsch","Payet","Gautier"]
listePrenom = ["Christine","Sébastien","Antonine","Adrien","Joel","Robin","Hadrien","Emmanuel","Nicolas","Jacques"]


# 6. Alphabet
# utile dans le cas de la bataille navale
alphabet = dict(zip([i+1 for i in range(26)],string.ascii_uppercase ))

#### FONCTIONS ####

def get_key(val,dictionnaire):
    for key, value in dictionnaire.items():
        if val == value:
            return key
    return "La clé n'existe pas"

#print(get_key('A',alphabet))

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
    couleurs = {"vert": "\033[92m","grisclair": "\033[37m","bleu": "\033[34m","jaune":'\033[93m', "rouge": "\033[91m", "normal": "\033[0m"}
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
            Lat, Long = float(Lat), float(Long)
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

def affiche_cadrillage(liste,type = 0):
    """Affichage de la grille"""
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
    :param pos:
    :return:
    """
    tab_coords=[]
    tab_coords.append(int(pos[1::])-1)
    tab_coords.append(get_key(pos[0].upper(),alphabet)-1)
    return tab_coords

def conv_coords(tab_coords):
    pos=''
    pos+=alphabet[tab_coords[1]]
    pos+=str(tab_coords[0]+1)
    return pos

def detection(grille):
    for i in range(len(grille)):
        for j in range(len(grille)):
            if grille[i][j]==100:
                return True
    return False
def bataille_navale(x, tailleJoueur,tailleOrdi):

    # 1. Initialisation des grilles joueur et Ordi
    print(f"Bienvenue dans la bataille navale sur un plateau ({x},{x})")
    print("Taille du bateaux du joueur : ",tailleJoueur)
    print("Taille du bateaux de l'adversaire : ",tailleOrdi)
    grilleJ1 = [[0 for i in range(x)] for j in range(x)]
    grilleOrdi = [[0 for i in range(x)] for j in range(x)]

    # 2. Placement des bateaux
    ## Placement du bateau du joueur
    affiche_cadrillage(grilleJ1,1)
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
                        if x-coords_proue[0] <=2 : #bateau placé trop bas
                            print("Recommence, ici c'est pas possible")
                        else: #on place le bateau
                            grilleJ1[coords_proue[0]][coords_proue[1]] = 100
                            for i in range(tailleJoueur-1):
                                grilleJ1[coords_proue[0]+(i+1)][coords_proue[1]] = 100
                            test_proue = True

                    elif sens == 'H':
                        if x-coords_proue[1] <=2: #bateau trop à droite
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
            if x - coords_proue_ordi[0] <= 2:  # bateau placé trop bas au hasard
                # Il faut recommencer le tirage au sort
                pass
            else:  # on place le bateau
                grilleOrdi[coords_proue_ordi[0]][coords_proue_ordi[1]] = 100
                for i in range(tailleOrdi - 1):
                    grilleOrdi[coords_proue_ordi[0] + (i + 1)][coords_proue_ordi[1]] = 100
                positionne = True

        elif sens == 'H':
            if x - coords_proue_ordi[1] <= 2:  # bateau placé trop à droite au hasard
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

    affiche_cadrillage(grilleJ1,1)
    print("Grille du joueur")

    affiche_cadrillage(grilleOrdi)
    print("Grille de l'ordi")



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

            if grilleOrdi[missile[0]][missile[1]] == 0:
                print("Plouf, dans la mer")
                Tour = not Tour
            elif grilleOrdi[missile[0]][missile[1]] == 100:
                print(colorer("Touché","vert"))
                grilleOrdi[missile[0]][missile[1]] = 50
            else:
                print("Tu as déjà tiré ici, tu perds la boule")
            if not detection(grilleJ1):
                pass

        else:
            print("Attention on t'attaque")
            missile = [rd.randint(0,x-1),rd.randint(0,x-1)]
            print("Tire en ", conv_coords(missile))
            if grilleJ1[missile[0]][missile[1]] == 0:
                print("Chanceux ! C'est dans la mer")
                Tour = not Tour
            elif grilleJ1[missile[0]][missile[1]] == 100:
                print(colorer("Tu es touché","rouge"))
                grilleJ1[missile[0]][missile[1]] == 50

    if not detection(grilleJ1):
        pass



bataille_navale(7,3,3)

