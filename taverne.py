import random as rd

from navigateur import Navigateur

class Taverne(object):
    def __init__(self, listeDeNoms, listeDePrenoms):
        self.listDeNoms = listeDeNoms
        self.listDePrenoms = listeDePrenoms

    def debaucher(self,experience=0):
        if experience == 0:
            salaire = rd.randint(1, 10)
            argent = rd.randint(1, 20)
        elif experience == 1:
            salaire = rd.randint(5, 15)
            argent = rd.randint(10, 30)
        elif experience == 2:
            salaire = rd.randint(12, 20)
            argent = rd.randint(25, 50)
        elif experience == 3:
            salaire = rd.randint(15, 30)
            argent = rd.randint(30, 60)
        elif experience == 4:
            salaire = rd.randint(18, 35)
            argent = rd.randint(40, 75)
        elif experience == 5:
            salaire = rd.randint(25, 50)
            argent = rd.randint(50, 100)

        force = salaire * 1.5 # règle dans ce jeu

        nomPrenom = " ".join([self.listDeNoms[rd.randint(0, len(self.listDeNoms) - 1)],
                          self.listDePrenoms[rd.randint(0, len(self.listDePrenoms) - 1)]])
        return Navigateur(nomPrenom, salaire, argent=argent, force=float(force),grade="minable")

