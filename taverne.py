import random as rd

from navigateur import Navigateur

class Taverne(object):
    def __init__(self, listeDeNoms, listeDePrenoms):
        self.listDeNoms = listeDeNoms
        self.listDePrenoms = listeDePrenoms

    def debaucher(self):
        salaire = rd.randint(1, 10)
        argent = rd.randint(1, 200)
        force = salaire * 1.5
        nomPrenom = " ".join([self.listDeNoms[rd.randint(0, len(self.listDeNoms) - 1)],
                          self.listDePrenoms[rd.randint(0, len(self.listDePrenoms) - 1)]])
        return Navigateur(nomPrenom, salaire, argent=argent, force=int(force))

