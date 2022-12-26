import jeux
from carthaPirates import CarthaPirates
from equipage import buildEquipage, Equipage
from jeux import *
from navigateur import Pirate
from taverne import Taverne


if __name__ == "__main__":

    # Initialisation des paramètres de départ du jeu
    fin = False
    carthapirates = CarthaPirates(7)  # Numero du bateau LaPynta
    carthapirates.rentrerMonBateau()  # Nettoyge préliminaire

    LoupsDeMer = Taverne(listeNom, listePrenom)  # taverne
    navireLaPynta = None  # navire
    E = None  # Equipage

    # menu du jeu
    menu = colorer("""     A. Partir à la recherche du trésor
     B. Aller à la Taverne
     C. Acheter un bateau
     D. Lancer une attaque
     E. Voir mon profil de pirate
     F. Quitter la piraterie""", "bleu")

    print("Bienvenue jeune pirate !")
    barre_chargement(0.01,colorer("•","jaune"))

    # 1** Choix du nom du capitaine
    Nom = input("Choisis ton nom : ")
    joueur = Pirate(Nom, argent=10, victoires=0, experience=1)

    print("Alors comme ça tu te lances dans la piraterie ", Nom, " ! Résumons un peu... ")
    joueur.afficheInfo()
    print('')

    while not fin:
        barre_chargement(0.05,colorer("×","jaune"), mot=" MENU ")
        print(menu)
        MODE = input('A toi de choisir A,B,C,D,E ou F: ')
        MODE = MODE.upper()
        print('')

        if MODE == 'A':
            if navireLaPynta == None or E == None:
                print(
                    'Il sera difficile de commencer la chance au trésor sans navire ou sans équipage, retourne à la Taverne.')
            elif navireLaPynta == 'Chaloupe':
                abandon = input(
                    "Avec une embarcation aussi maigre, l'aventure sera rude !\n Veux-tu abandonner [Oui/Non] ?")
                abandon = abandon.lower()

                if abandon == "non":
                    print("Que l'aventure commence, ouvre la page web https://carthapirates.fr/ pour voir la carte !!")

                    long = 12.4
                    lat = 39.5
                    carthapirates.deplacerMonBateauVersCoords((12.4, 39.5))
                    print("Prouve à ton équipage que tu es un bon marin :")
                    print(
                        "Regarde la carte et évalue les coordonnées géographiques en longitude et latitude du navire.")
                    print("Tu dois te tromper de moins de 100km et tu as 8 tentatives ")
                    test1 = devine_les_coords(lat, long, 8)

                    if test1:
                        input("Sans indice, il faut retourner à terre, c'est ok ? [Tape une touche]")
                        ports = carthapirates.listerTousLesPorts()

                        for port in ports:
                            print(port["id"], ":", port["nom"])
                        idPortChoisi = input(colorer("Dans quel port souhaites-tu aller maintenant ? ", "rouge"))

                        # Pour récupérer les coordonnées d'un port, à partir de son identifiant
                        coords = carthapirates.recupererCoordsPort(idPortChoisi)  # On réutilise l'identifiant du port choisi
                        # Pour déplacer le bateau vers des coordonnées
                        carthapirates.deplacerMonBateauVersCoords(coords)

                        print(colorer("Le bateau a bien été déplacé. Regarde la carte !", "vert"))

                        input("Dirige toi vers Melilla, tu en sauras plus, ok ? [Tape sur une touche]")
                        idPortChoisi = input(colorer("Tape l'identifiant du port correspondant ? ", "rouge"))

                        if int(idPortChoisi) == 5:
                            coords = carthapirates.recupererCoordsPort(idPortChoisi)
                            carthapirates.deplacerMonBateauVersCoords(coords)
                            barre_chargement(0.3,colorer('~',"bleu"))
                            print(colorer("Le bateau a bien été déplacé. Regarde la carte !", "vert"))
                            print("Bravo, pour trouver le trésor, il ne reste plus qu'à gagner cette bataille navale :")
                            if bataille_navale(4,1,1):
                                print(colorer(vict,"vert"))
                                joueur.argent += 500
                            else:
                                print("C'est malheureux si proche du but !")
                                print(colorer(defa,"rouge"))
                                joueur.argent = 0
                                navireLaPynta = None
                        else:
                            print("L'aventure s'arrête là pour toi marin d'eau douce.")
                            print(colorer(defa, "rouge"))
                            joueur.argent = 0
                            navireLaPynta = None
                    else:
                        print("L'aventure s'arrête là pour toi marin d'eau douce.")
                        print(colorer(defa, "rouge"))
                        joueur.argent = 0
                        navireLaPynta = None

            elif navireLaPynta == 'Navire':
                print("Que l'aventure commence, ouvre la page web https://carthapirates.fr/ pour voir la carte !!")
                long = 12.4
                lat = 39.5
                carthapirates.deplacerMonBateauVersCoords((12.4, 39.5))
                print("Prouve à ton équipage que tu es un bon marin :")
                print("Regarde la carte et évalue la distance au port de Marseille ")
                print("Tu dois te tromper de moins de 10km et tu as 8 tentatives ")

                test1 = devine_la_dist(carthapirates.recupererCoordsPort(1),lat, long, 8)

                if test1:
                    input("Sans indice, il faut retourner à terre, c'est ok ? [Tape une touche]")
                    ports = carthapirates.listerTousLesPorts()

                    for port in ports:
                        print(port["id"], ":", port["nom"])
                    idPortChoisi = input(colorer("Dans quel port souhaites-tu aller maintenant ? ", "rouge"))

                    # Pour récupérer les coordonnées d'un port, à partir de son identifiant
                    coords = carthapirates.recupererCoordsPort(idPortChoisi)  # On réutilise l'identifiant du port choisi
                    # Pour déplacer le bateau vers des coordonnées
                    carthapirates.deplacerMonBateauVersCoords(coords)

                    print(colorer("Le bateau a bien été déplacé. Regarde la carte !", "vert"))

                    print("Dirige toi vers Melilla, tu en sauras plus...")
                    idPortChoisi = input(colorer("Tape l'identifiant du port correspondant ? ", "rouge"))

                    if int(idPortChoisi) == 5:
                        coords = carthapirates.recupererCoordsPort(idPortChoisi)
                        carthapirates.deplacerMonBateauVersCoords(coords)
                        barre_chargement(0.2, colorer('~', "bleu"),longueur=10)

                        print(colorer("Le bateau a bien été déplacé. Regarde la carte !", "vert"))
                        print("Bravo, pour trouver le trésor, il ne reste plus qu'à gagner cette bataille navale :")
                        if bataille_navale(5, 2, 2):
                            print(colorer(vict, "vert"))
                            joueur.argent += 500
                        else:
                            print("C'est malheureux si proche du but !")
                            print(colorer(defa, "rouge"))
                            joueur.argent = 0
                            navireLaPynta = None
                    else:
                        print("L'aventure s'arrête là pour toi marin d'eau douce.")
                        print(colorer(defa, "rouge"))
                        joueur.argent = 0
                        navireLaPynta = None
                else:
                    print("L'aventure s'arrête là pour toi marin d'eau douce.")
                    print(colorer(defa, "rouge"))
                    joueur.argent = 0
                    navireLaPynta = None

            elif navireLaPynta == 'Caravelle':
                print("Que l'aventure commence, ouvre la page web https://carthapirates.fr/ pour voir la carte !!")
                long = 12.4
                lat = 39.5
                carthapirates.deplacerMonBateauVersCoords((12.4, 39.5))
                print("Prouve à ton équipage que tu es un bon marin, ok ? ")

                ports = carthapirates.listerTousLesPorts()

                for port in ports:
                    print(port["id"], ":", port["nom"])

                idPortChoisi1 = input(colorer("Tape le numéro correspondant au port de Melilla : ", "rouge"))
                coords = carthapirates.recupererCoordsPort(idPortChoisi1)
                carthapirates.deplacerMonBateauVersCoords(coords)

                idPortChoisi2 = input(colorer("Tape le numéro du port le plus au nord de la carte : ", "rouge"))
                coords = carthapirates.recupererCoordsPort(idPortChoisi2)
                carthapirates.deplacerMonBateauVersCoords(coords)


                print(colorer("Le bateau a bien été déplacé. Regarde la carte !", "vert"))

                input("Vérifions cela... [Tape sur une touche]")

                if int(idPortChoisi1) == 5 and int(idPortChoisi2) == 17:
                    barre_chargement(0.2, colorer('~', "bleu"), longueur=10)
                    print(colorer("Le bateau a bien été déplacé. Regarde la carte !", "vert"))
                    print("Bravo, pour trouver le trésor, il ne reste plus qu'à gagner cette bataille navale :")
                    if bataille_navale(6, 3, 3):
                        print(colorer(vict, "vert"))
                        joueur.argent += 500
                    else:
                        print("C'est malheureux si proche du but !")
                        print(colorer(defa, "rouge"))
                        joueur.argent = 0
                        navireLaPynta = None
                else:
                    print("L'aventure s'arrête là pour toi marin d'eau douce.")
                    print(colorer(defa, "rouge"))
                    joueur.argent = 0
                    navireLaPynta = None

        elif MODE == 'B':
            biere = input("Un p'tit whisky ? [Oui/Non] ")
            biere = biere.lower()
            if biere == "oui":
                if joueur.argent < 5:
                    print("Tonerre de Brest, tu vas pas nous payer tu n'as que", joueur.argent, "pièces d'or")
                    print(
                        "Le whisky coûte 5 pièces d'or alors vends ton bateau si tu en as un, ou quitte la piraterie, personne ne veux de toi ici !")
                else:
                    print("Ca fera 5 pièces d'or")
                    joueur.argent = joueur.argent - 5
                    input("Il te reste " + str(joueur.argent) + " pièces d'or [Tapez ENTREE]")
                    print("Qu'est -ce qui t'amène ici ?")
                    print("A. Débaucher un équipage")
                    print("B. Juste pour boire du whisky")
                    choixTaverne = input("[Tape A ou B] ")
                    choixTaverne=choixTaverne.upper()
                    if choixTaverne == 'A':
                        E = Equipage(buildEquipage(LoupsDeMer,5,joueur.experience))
                        print("Voici ton équipage :")
                        E.afficheInfo()
                        joueur.grade='capitaine'

                    elif choixTaverne == 'B':
                        nbWhisky = 0
                        while joueur.argent >= 5:
                            nbWhisky += 1
                            joueur.argent = joueur.argent - 5
                        phrase = "Ivrogne, tu n'as plus un sou après "+ str(nbWhisky) + " whisky dehors ! "
                        print(colorer(phrase, "rouge"))
                    else:
                        input(
                            "Tu es déjà bien saoul ma parole, sors de là avant de faire n'importe quoi ! [Tapez ENTREE]")

            else:
                print("Mille millions de mille sabords, sors de là Moule à gaufres si tu ne bois pas de whisky")

        elif MODE == 'C':
            print("Que veux-tu acheter ?")
            print("1.Chaloupe (5po)  2.Navire(40po)  3.Caravelle(150po) ")

            type_bateau = {1 : 'Chaloupe', 2 : 'Navire', 3 : 'Caravelle'}
            prix = {1: 5, 2: 40, 3: 150}

            while True:
                try:
                    choix_bateau = int(input("[Tape 1,2 ou 3] "))
                    if prix[choix_bateau] > joueur.argent:
                        print("Oust ! Tu es bien trop pauvre pour ce bateau")
                    else:
                        navireLaPynta = type_bateau[choix_bateau]
                        joueur.argent = joueur.argent-prix[choix_bateau]
                        print("Voilà ton navire moussaillon :")
                        print(embarcations[navireLaPynta])
                    break
                except (KeyError,ValueError):
                    print("Je comprends pas ?")

        elif MODE == 'D':
            if navireLaPynta == None or E == None:
                input("Pas de d'équipage, pas de bateau \n pas de bateau pas d'attaque [Tapez ENTREE]")
            else:
                print(colorer("Tout le monde sur le pont, parer à l'abordage","vert"))
                print("Tu vas attaquer un navire de la marine marchande portugaise")
                print("Choisis l'experience du marin ennemi de 0 à 5.")
                print("Ton expérience est de ",joueur.experience,". Nous te recommandons de choisir un niveau similaire")
                print('')
                while True:
                    try:
                        niv = int(input("[Tape le niveau de 0 à 5] : "))
                        break
                    except ValueError:
                        print('Ecris correctement 0,1,2,3,4 ou 5 !')

                # On constitue un équipage ennemi de force semblable
                N = Equipage(buildEquipage(LoupsDeMer,5,niv))

                reponse = input("Veux tu voir connaître l'équipage ennemi avant l'abordage [oui/ non] ? ")
                reponse=reponse.upper()

                if reponse == 'OUI':
                    N.afficheInfo()
                elif reponse == 'NON':
                    pass
                else:
                    print("Hein.. bon pas grave, tu verras bien si tu gagnes ou tu perds !")

                print('')
                barre_chargement(0.3, colorer("¤", "vert"), mot=" Résumé de la situation ")
                print("Equipage de ",joueur.nom," :")
                print("Force de l'Equipage : ", E.calculForceEquipage())
                barre_chargement(0.2,"-",longueur=3)
                print(colorer("Equipage ennemi","rouge"))
                phrase = "Force de l'Equipage : "+str(N.calculForceEquipage())
                print(colorer(phrase,"rouge"))
                print('')

                barre_chargement(0.2, "•", longueur=3)
                if E.calculForceEquipage() >= N.calculForceEquipage():
                    print(colorer("VICTOIRE !", "vert"))
                    print("C'est l'heure de faire les comptes :")
                    print("La revente du bateau adverse te rapporte 15 pièces d'or")
                    print("Mais tu dois payer tes marins")
                    print("Total du butin : ", 15 + N.calculDesRichesses())
                    print("Total du butin après paiement des marins : ", E.payerEquipage(15 + N.calculDesRichesses()))

                    joueur.argent += E.payerEquipage(15 + N.calculDesRichesses())
                    joueur.victoires += 1
                    if joueur.experience<5:
                        joueur.experience+=1
                else:
                    print(colorer("DEFAITE !", "rouge"))

                    # mise à jour des paramètres
                    joueur.argent = 0
                    E = None
                    navireLaPynta = None
                    print("Terrible, ton équipage s'est fait massacrer, tu es ruiné, il ne reste certainement plus qu'à quitter la piraterie...")

        elif MODE == 'E':
            print('')
            barre_chargement(0.05,mot=" Résumé ")
            joueur.afficheInfo()
            barre_chargement(0.01)
            print('')

        elif MODE == 'F':
            # on juge le pirate et on le condamne
            if joueur.experience == 0:
                print(
                    "Tu t'en sors bien moussaillon, tu n'as encore rien fait de grave, retourne faire un métier honnête\nTu n'es pas fait pour la piraterie de toute façon !")
                fin = True
            if joueur.experience == 1:
                # amende payée, fin, retour dans la piraterie
                print("Tu ne vas pas t'en sortir comme ça ! La justice te condamne à une amende de 180 pièces d'or")
                print("A. Accepter le jugement (Ton butin est de ", joueur.argent, " pièces d'or.)")
                print("B. Echapper à la justice et tenter à nouveau sa chance dans la piraterie ")
                choixModeD = input("Alors que fais-tu A ou B ? ")
                if choixModeD == "A":
                    if joueur.argent >= 180:
                        joueur.argent = joueur.argent - 180
                        choixModeD_revenir = input(
                            "Tu en a fini avec la justice, Veux revenir dans la piraterie ou abandonner à jamais tel un lâche ? [Oui/Non]")
                        choixModeD_revenir = choixModeD_revenir.upper()
                        if choixModeD_revenir == "NON":
                            print('Aurevoir,en espérant te revoir bientôt dans la piraterie !')
                            fin = True
                        elif choixModeD_revenir == "NON":
                            print('Formidable ;-)')
                        else:
                            print('Je ne comprends pas ta réponse mais je prends ça pour un oui')
                    else:
                        print(
                            "Tu ne peux pas payer l'amende, la justice décide donc de te condamner à mort. \nUne dernière chance de t'échapper, retrouve le code secret du cadenas de la prison et échappe toi !")
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
                    print(
                        "On ne t'a pas compris ! Tu étais trop occupé à t'enfuir c'est pour ça ....\n Petit coquin, bienvenue à toi")

            if joueur.experience >= 2:
                # jeu du pendu pour revenir au menu ou mort du personnage
                print("Comme tout grand pirate tu seras pendu haut et court...")
                print("... sauf si tu envoies un mot secret à tes amis pirates pour qu'ils viennent te délivrer")

                destin = pendu(jeux.liste_mot)
                if destin:
                    print('')
                    print(" Bienvenue dans la piraterie vieux loup de mer, retente ta chance avec 10 pièces d'or !")
                    joueur.argent = 10
                else:
                    print("Les gens se rappelleront de toi", joueur.nom, "\nAurevoir")
                    fin = True

        else:
            print("Tape A,B,C ou D, pas autre chose enfin !")


    print("Jeu LaPynta2023")
