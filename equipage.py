"""
Ce module contient la classe Equipage ainsi que la fonction BuildEquipage qui automatise
le processus de création d'un équipage

"""
class Equipage(object):
    def __init__(self, marins):
        self.marins = marins

    def afficheInfo(self):
        for i in range(len(self.marins)):
            print("Nom :",self.marins[i].nom,"\nArgent : ",self.marins[i].argent, "\nSalaire : ",self.marins[i].salaire, "\nForce : ",self.marins[i].force)
    def calculDesRichesses(self):
        richesse = 0
        for p in self.marins:
            richesse = richesse + p.argent
        return richesse

    def rechercheDuPlusRiche(self):
        maxi = self.marins[0].argent
        for i in range(1, len(self.marins)):
            if self.marins[i].argent > maxi:
                maxi = self.marins[i].argent

        # plus_fort = max(self.marins.force)
        print(maxi)

    def rechercheDuPlusFort(self):
        maxi=self.marins[0].force
        for i in range(1,len(self.marins)):
            if self.marins[i].force > maxi:
                maxi=self.marins[i].force

        #plus_fort = max(self.marins.force)
        print(maxi)

    def calculForceEquipage(self):
        force = 0
        for p in self.marins:
            force = force + p.force
        return force

    def payerEquipage(self,total):
        for p in self.marins:
            if total - p.salaire <= 0:
                print("Il ne te reste plus rien")
                return 0
            else:
                total = total - p.salaire
                p.argent = p.argent + p.salaire
        return total

 # Fonction pour construire equipage
def buildEquipage(taverne, nbMarins,experience):
    """
    Fonction pour créer un équipage
    :param taverne:
    :param nbMarins:
    :param experience:
    :return:
    """
    equipage = []
    for i in range(nbMarins):
        equipage.append(taverne.debaucher(experience))
    return equipage