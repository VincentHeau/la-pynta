class Capitaine(object):
    def __init__(self, nom, navire):
        self.nom = nom
        self.navire = navire

    def afficheInfo(self):
        print("Le Capitaine s'appelle",self.nom,". Il commande le navire ",self.navire.nom)

