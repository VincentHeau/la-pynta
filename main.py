import jeux
from capitaine import Capitaine
from equipage import buildEquipage, Equipage
from navigateur import Navigateur, Pirate
from navire import Navire
from taverne import Taverne
from jeux import *
from carthaPirates import CarthaPirates

"""
#Documentation des classes et modules utilisés
print(jeux.__doc__)
"""

if __name__ == "__main__":


    """
    # Pour lister et choisir un port parmi tous les ports
                    ports = carthapirates.listerTousLesPorts()
                    for port in ports:
                        print(port["id"], ":", port["nom"])
                    idPortChoisi = input(colorer("Dans quel port souhaitez-vous aller maintenant ? ", "rouge"))

                    # Pour récupérer les coordonnées d'un port, à partir de son identifiant
                    coords = carthapirates.recupererCoordsPort(
                        idPortChoisi)  # On réutilise l'identifiant du port choisi
                    print("Les coordonnées du port n°", idPortChoisi, "sont", coords)
                    
                    
    # Pour récupérer les coordonnées du bateau
    coords = carthapirates.recupererCoordsMonBateau()
    print("Les coordonnées du bateau sont", coords)
    # Pour rechercher les n ports à proximité de coordonnées
    portsProches = carthapirates.trouverPortsProchesCoords(coords, 5)  # On réutilise les coordonnées du bateau
    for port in portsProches:
        print(port["id"], ":", port["nom"], "(situé à", port["distance"], "milles nautiques du bateau)")

    # Pour retirer le bateau et ses trajets de la carte à la fin de votre programme
    confirmation = input(colorer("Souhaitez-vous arrêter ? [Y/n] ", "rouge"))
    if confirmation == "Y":
        carthapirates.rentrerMonBateau()
        print(colorer("Le bateau et ses trajets ont bien été retirés. Regardez la carte !", "vert"))
    else:
        carthapirates.rentrerMonBateau()
        print(colorer("Et bha le bateau et ses trajets ont quand même été retirés. Na ! Regardez la carte !", "vert"))
    """



    #Initialisation des paramètres de départ du jeu
    fin = False
    carthapirates = CarthaPirates(7)  # Numero du bateau LaPynta
    carthapirates.rentrerMonBateau() # Nettoyge préliminaire

    navireLaPynta = 'Chaloupe'
    E= None #Equipage

    # menu du jeu
    menu = colorer("""     A. Partir à la recherche du trésor
     B. Aller à la Taverne
     C. Lancer une attaque
     D. Quitter la piraterie""","vert")
    #pendu(jeux.liste_mot)
    print("Bienvenue jeune pirate !")
    barre_chargement(0.01)
    # 1** Choix du nom du capitaine
    Nom = input("Choisis ton nom : ")
    joueur = Pirate(Nom,0,experience=0)


    print("Alors comme ça tu te lances dans la piraterie ",Nom," ! Résumons un peu... ")
    joueur.afficheInfo()
    print('')

    while not fin:

        barre_chargement(0.01,mot=colorer(" MENU ","rouge"))
        print(menu)
        MODE=input('A toi de choisir A,B,C ou D : ')
        MODE=MODE.upper()
        print('')

        if MODE == 'A':
            if navireLaPynta == None:# or E == None:
               print('Il sera difficile de commencer la chance au trésor sans navire ou sans équipage, retourne à la Taverne.')
            elif navireLaPynta == 'Chaloupe':
                abandon = input("Avec une embarcation aussi maigre, l'aventure sera rude !\n Veux-tu abandonner [Oui/Non] ?")
                abandon=abandon.lower()

                if abandon == "non":
                    print("Que l'aventure commence, ouvre la page web https://carthapirates.fr/ pour voir la carte !!")

                    long = 12.4
                    lat = 39.5
                    carthapirates.deplacerMonBateauVersCoords((12.4, 39.5))
                    print("Prouve à ton équipage que tu es un bon marin :")
                    print("Regarde la carte et évalue les coordonnées géographiques en longitude et latitude du navire.")
                    print("Tu dois te tromper de moins de 100km et tu as 8 tentatives ")
                    test1 = devine_les_coords(lat,long,8)
                    if test1:
                        # Pour déplacer le bateau vers des coordonnées
                        # carthapirates.deplacerMonBateauVersCoords(coords)  # On réutilise les coordonnées du port choisi
                        print(colorer("Le bateau a bien été déplacé. Regardez la carte !", "vert"))
                    else:
                        print("L'aventure s'arrête là pour toi marin d'eau douce.")



            elif navireLaPynta == 'Navire':
                #print(embarcations[navireLaPynta])
                print("Que l'aventure commence, ouvre la page web https://carthapirates.fr/ pour voir la carte !!")

                long = 12.4
                lat = 39.5
                carthapirates.deplacerMonBateauVersCoords((12.4, 39.5))
                print("Prouve à ton équipage que tu es un bon marin :")
                print("Regarde la carte et évalue les coordonnées géographiques en longitude et latitude du navire.")
                print("Tu dois te tromper de moins de 100km et tu as 8 tentatives ")
                test1 = devine_les_coords(lat, long, 8)
            elif navireLaPynta == 'Caravelle':
                print(embarcations[navireLaPynta])
        elif MODE == 'B':
            pass
        elif MODE == 'C':
            pass
        elif MODE == 'D':
            #on juge le pirate et on le condamne
            if joueur.experience == 0:
                print("Tu t'en sors bien moussaillon, tu n'as encore rien fait de grave, retourne faire un métier honnête\nTu n'es pas fait pour la piraterie de toute façon !")
                fin = True
            if joueur.experience == 1:
                # amende payée, fin, retour dans la piraterie
                print("Tu ne vas pas t'en sortir comme ça ! La justice te condamne à une amende de 180 pièces d'or")
                print("A. Accepter le jugement (Ton butin est de ",joueur.argent," pièces d'or.)")
                print("B. Echapper à la justice et tenter à nouveau sa chance dans la piraterie ")
                choixModeD=input("Alors que fais-tu A ou B ? ")
                if choixModeD == "A":
                    if joueur.argent>=180:
                        joueur.argent = joueur.argent-180
                        choixModeD_revenir = input("Tu en a fini avec la justice, Veux revenir dans la piraterie ou abandonner à jamais tel un lâche ? [Oui/Non]")
                        choixModeD_revenir = choixModeD_revenir.upper()
                        if choixModeD_revenir == "NON":
                            print('Aurevoir,en espérant te revoir bientôt dans la piraterie !')
                            fin = True
                        elif choixModeD_revenir == "NON":
                            print('Formidable ;-)')
                        else:
                            print('Je ne comprends pas ta réponse mais je prends ça pour un oui')
                    else:
                        print("Tu ne peux pas payer l'amende, la justice décide donc de te condamner à mort. \nUne dernière chance de t'échapper, retrouve le code secret du cadenas de la prison et échappe toi !")
                        destin = pendu(jeux.liste_mot)
                        if destin:
                            print('')
                            print('Tu as eu de la chance, ne te fais plus avoir maintenant')
                        else:
                            print("Les gens se rappelleront de toi", joueur.nom, "\nAurevoir")
                            fin = True

                elif choixModeD == 'B':
                    print("Sage décision pirate ;)")
                else:
                    print("On ne t'a pas compris ! Tu étais trop occupé à t'enfuir c'est pour ça ....\n Petit coquin, bienvenue à toi")

            if joueur.experience == 2:
                # jeu du pendu pour revenir au menu ou mort du personnage
                print("Comme tout grand pirate tu seras pendu haut et court...")
                print("... sauf si tu envoies un mot secret à tes amis pirates pour qu'ils viennent te délivrer")

                destin = pendu(jeux.liste_mot)
                if destin:
                    print('')
                    print('Bienvenue dans la piraterie vieux loup de mer, retente ta chance !')
                else:
                    print("Les gens se rappelleront de toi", joueur.nom, "\nAurevoir")
                    fin =True
        else:
            print("Tape A,B,C ou D, pas autre chose enfin !")

        # Choix de l'équipage
        #nomDePirate = ["Bonny", "Jack", "Teach", "Drake", "Morgan", "Nau", "Read"]
        #prenomDePirate = ["Anne", "Calico", "Edward", "Francis", "Henry", "Jean", "Mary"]
        #taverneAPirate = Taverne(nomDePirate, prenomDePirate)
        #E = Equipage(buildEquipage(taverneAPirate, 5))

        """
        print(" A la taverne, vous débauchez une belle brochette de rigolos")
        print("Vous devez acheter le bateau la Pynta car votre bateau actuel est trop faible pour affronter la mer")
        print("Vous décidez d'utiliser de mettre en commun les économies de votre équipage")
        print("Ce montant s'élève à ",E.calculDesRichesses())
        print("Mais votre équipage se révolte et menace de ne pas poursuivre l'aventure avec vous.")
        print("Vous décidez de tuer un marin pour l'exemple, Qui choississez-vous ?")
        
    
        for i in range(len(E.marins)):
            print(i,". ",E.marins[i].nom, " : ", E.marins[i].argent, " roupies pakistanaises")
    
        choix = input("Tapez le numéro du marin que vous voulez donner à manger aux requins : ")
    
        #diminuer l'équipage
        you.butin=E.calculDesRichesses()
        print(you.butin)
        if choix == "A":
            print("Bienvenue au magasin de bateau, vous avez",you.nom)
    
        jack = Navigateur("Jack Calico", argent=10, force=20, grade="capitaine")
        edward = Navigateur("Edward Drake", argent=2, force=30, grade="minable")
        anne = Navigateur("Anne Bonny", argent=3, force=200, grade="minable")
    
        equipe1 = [jack, edward, anne]
    
    
    
        
        Equipage(equipe1).calculForceEquipage()
        Equipage(equipe1).rechercheDuPlusFort()
        Equipage(equipe1).rechercheDuPlusRiche()
        Equipage(equipe1).calculDesRichesses()
        """
        """
        navire1 = Navire("Queen Anne's Revenge", [jack, edward, anne])
        navire2 = Navire("La Pynta", buildEquipage(taverneAPirate,3))
    
        print(navire1)
        print(navire2)
    
    
    
    
        navire1.combat(navire2)
        You = Capitaine("toto",navire1)
        You.afficheInfo()
        """
        """
        carthapirates = CarthaPirates(9)  # Indiquez le numéro du bateau
        
        for i in range(3):
            # Pour lister et choisir un port parmi tous les ports
            ports = carthapirates.listerTousLesPorts()
            for port in ports:
                print("Port n°", port["id"], ":", port["nom"])
            idPortChoisi = str(input("Dans quel port souhaitez-vous aller maintenant ? "))
    
            # Pour récupérer les coordonnées d'un port à partir de son identifiant
            coords = carthapirates.recupererCoordsPort(idPortChoisi)  # On réutilise l'identifiant du port choisi
            print("Les coordonnées du port n°", idPortChoisi, "sont", coords)
    
            # Pour déplacer le bateau vers des coordonnées
            carthapirates.deplacerMonBateauVersCoords(coords)  # On réutilise les coordonnées du port choisi
            print("Le bateau a bien été déplacé. Regardez la carte !")
    
        # Pour récupérer les coordonnées du bateau
        coords = carthapirates.recupererCoordsMonBateau()
        print("Les coordonnées du bateau sont", coords)
    
        # Pour rechercher les n ports à proximité de coordonnées
        portsProches = carthapirates.trouverPortsProchesCoords(coords, 5)  # On réutilise les coordonnées du bateau
        for port in portsProches:
            print("Port n°", port["id"], ":", port["nom"], "(situé à", port["distance"], "miles nautiques du bateau)")
    
        # Pour retirer le bateau de la carte
        carthapirates.rentrerMonBateau()
        print("Le bateau et ses trajets ont bien été déplacés. Regardez la carte !")
        """

    print("Jeu LaPynta2023")




