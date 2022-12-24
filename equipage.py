class Equipage(object):
    def __init__(self, marins):
        self.marins = marins

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
        print(force)
        return force

 # Fonction pour construire equipage
def buildEquipage(taverne, nbMarins):
    equipage = []
    for i in range(nbMarins):
        equipage.append(taverne.debaucher())
    return equipage