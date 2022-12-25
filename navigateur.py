class Navigateur(object):

 def __init__(self, nom, salaire=0, yeux=2, bras=2, jambes=2, argent=0, force=1, grade="minable"):
  self.nom = nom
  self.salaire = salaire
  self.tete = 1
  self.nbYeux = yeux
  self.nbBras = bras
  self.nbJambes = jambes
  self.argent = argent
  self.force = force
  self.grade = grade
  #self.afficheInfo()  # c'est ce qui affichait les infos

 def augmenteGrade(self):
  if self.grade == "minable":
   self.grade = "minus"
  elif self.grade == "minus":
   self.grade = "chef"
  elif self.grade == "chef":
   self.grade = "capitaine"

  self.force = self.force + 1

 def afficheArgent(self):
  print(self.nom, ": ", self.argent)
 def afficheInfo(self):
  print("Tu as ", self.nbYeux, "yeux, ", self.tete, " tête, ", self.nbBras, " bras, et ", self.nbJambes,
        " jambes.\n Grade: ",self.grade)

 def accident(self, typeAcc):
  if typeAcc == "bras":
   self.nbBras = self.nbBras - 1
  elif typeAcc == "jambe":
   self.nbJambes = self.nbJambes - 1
  elif typeAcc == "yeux":
   self.nbYeux = self.nbYeux - 1

 def tempete(self):
  self.accident("bras")

 def initGrade(self):
  self.grade = "minable"

 def afficheGrade(self):
  print(self.grade)

 def descendGrade(self):
  if self.grade == "minus":
   self.grade = "minable"
  elif self.grade == "chef":
   self.grade = "minus"
  elif self.grade == "capitaine":
   self.grade = "chef"

 def jourDePaye(self):
  self.argent+=self.salaire
  print("Salaire payé",self.salaire)


# You is - a Navigateur
class Pirate(Navigateur):
    def __init__(self,nom,argent,victoires,experience=0):
        super(Pirate, self).__init__(nom,argent=argent)
        self.victoires = victoires
        self.experience = experience


    def afficheInfo(self):
     print("Nom : ",self.nom)
     print("Victoires :",self.victoires," batailles gagnées")
     print("Grade :",self.grade)
     print("Butin :", self.argent," pièces d'or")
     print("Salaire :",self.salaire," pièces d'or")
     print("Etat de santé : ",self.nbYeux,"yeux,",self.nbJambes,"jambes,",self.nbBras,"bras")