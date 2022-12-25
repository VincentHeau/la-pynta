from equipage import Equipage

class Navire(object):
    def __init__(self, nom, marins, categorie):
        self.nom = nom
        self.equipage = Equipage(marins)
        self.categorie = categorie



    def combat(self, ennemi):
        print( "combat le bateau ennemi ! ")
        if self.equipage.calculForceEquipage() > ennemi.equipage.calculForceEquipage():
            print("on a gagné")
            for marin in self.equipage.marins:
                marin.jourDePaye()

        else:
            print("ennemi a gagné")
