#!/usr/bin/env python
# coding: utf-8

# ## Travail Pratique du cours d'Intelligence Artificielle

# En cryptographie, le chiffrement par décalage, également connu sous le nom de chiffre de César ou code de César, est une méthode de chiffrement simple utilisée par Jules César dans ses communications secrètes. Cette méthode consiste à remplacer chaque lettre du texte original par une lettre à une distance fixe, dans l'ordre de l'alphabet. Par exemple, avec un décalage de 3 vers la gauche, A est remplacé par Y, B devient Z, et ainsi de suite jusqu'à ce que W devienne U, puis X devienne V, etc. Le texte chiffré est donc une permutation circulaire de l'alphabet. La clé du chiffrement est la longueur du décalage qui doit être transmis au destinataire pour que celui-ci puisse déchiffrer le message. ([source](https://fr.wikipedia.org/wiki/Chiffrement_par_d%C3%A9calage))
# 
# Le code Python suivant, qui implémente un jeu mystère, est chiffré en utilisant le chiffrement par décalage décrit ci-dessus. Vous êtes invité à déchiffrer et expliquer chaque ligne du code, et à expliquer brièvement ce que fait ce jeu mystère.

# In[ ]:


#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import random
import time


################### LE MESSAGE DE BIENVENUE ET DEXPLICATION ##################

def WELCOMEMESSAGE():
    print("""
----------------------------------------------------------------------------
                        REGLES DU JEU MYSTERE
----------------------------------------------------------------------------
REGLES : 1 - L'UTILISATEUR ET LORDINATEUR JOUENT A TOUR DE ROLE
         2 - LORDINATEUR COMMENCE
         3 - SEULEMENT UN OU DEUX BATONS PEUVENT ETRE RETIRES A CHAQUE COU
         4 - CELUI QUI TIRE LE DERNIER BATON A GAGNE
         
----------------------------------------------------------------------------
                           APPRENTISSAGE
----------------------------------------------------------------------------                        
SUIVANT QU'IL GAGNE OU PERD L'ORDINATEUR RECOIT UNE RECOMPENSE OU UNE PUNITION
----------------------------------------------------------------------------
""")

#### NOUS FAISONS COMMENCER LORDINATEUR PARCE QUE LE PREMIER JOUEUR A UNE
#### STRATEGIE GAGNANTE SI LE JOUEUR COMMENCE ET QUIL JOUE BIEN LA MACHINE
#### PERDRA QUOIQUELLE FASSE ET NAPPRENDRA RIEN 

###############################################################################


################## DEFINITION ET IMPRESSION DE LA POSITION DE JEU #############

#  cette fonction imprime le tableau de jeu
def PRINTBOARD(n): # n est le nombre d'allumettes restantes
    BOARD=[]  # le tableau de jeu
    for _ in range(n): # on ajoute les allumettes restantes au tableau
        BOARD.append("/") # on ajoute une allumette au tableau
    print("\n----------------------------------------------------------------------------")
    print("      ",*BOARD, sep="   ") # on imprime le tableau de jeu
    print("----------------------------------------------------------------------------\n")
    print("IL RESTE " + str(n) + " ALLUMETTES") # on imprime le nombre d'allumettes restantes
    
###############################################################################


################### INITIALISATION DE LA MACHINE ##############################

NOMBREALLUMETTES=8   # on initialise le nombre d'allumettes a 8
BOARD = []   #  on definit le tableau de jeu
BOULESJAUNES = []  # on definit le tableau de boules jaunes
BOULESROUGES = [] #   on definit le tableau de boules rouges
TIRAGE = []  # on definit le tableau de tirage

for _ in range(NOMBREALLUMETTES): # on ajoute les allumettes au tableau de jeu
    BOULESJAUNES.append(2) # on ajoute les boules jaunes au tableau de boules jaunes
    BOULESROUGES.append(2) # on ajoute les boules rouges au tableau de boules rouges
    TIRAGE.append(0) # on ajoute les tirages au tableau de tirage
BOULESROUGES[0]=0 # on enleve une boule rouge du premier tirage

###############################################################################


#################### PROGRAMME PRINCIPAL #################
WELCOMEMESSAGE() # on affiche le message de bienvenue
UNEAUTREPARTIE=True # on initialise la variable qui permet de jouer une autre partie
COMPTEURPARTIE=0 # on initialise le compteur de parties
time.sleep(1) # on attend 1 seconde
print("LA PROBABILITE DE GAIN DE LORDINATEUR A LA PREMIERE PARTIE SI LE JOUEUR JOUE DE MANIERE OPTIMALE EST DE 12,5 %")
# on attend 1 seconde
time.sleep(1)
while UNEAUTREPARTIE :  # cette boucle permet de jouer une autre partie
    PLAYER = "AKN" # on initialise le joueur
    ALLUMETTES=NOMBREALLUMETTES # on initialise le nombre d'allumettes
    TIRAGE=[0,0,0,0,0,0,0,0]  # on initialise le tirage pour chaque allumette
    while ALLUMETTES>0:
        # on imprime le tableau de jeu
        PRINTBOARD(ALLUMETTES)  
        #  on attend 1 seconde
        time.sleep(1)
        
        # si c'est le tour de l'ordinateur 
        if PLAYER=='AKN': # si c'est le tour de l'ordinateur
            print("\n L'ORDINATEUR CHOISIT DE RETIRER...") # on affiche le message
            time.sleep(1) # on attend 1 seconde
            
            SOMME=BOULESJAUNES[ALLUMETTES-1] + BOULESROUGES[ALLUMETTES-1] # on calcule la somme des boules jaunes et rouges
            BOULEHASARD=random.randint(1,SOMME)  # on tire un nombre au hasard entre 1 et la somme des boules jaunes et rouges
            if BOULEHASARD <= BOULESJAUNES[ALLUMETTES-1]:  # si le nombre tire est inferieur ou egal au nombre de boules jaunes
                TIRAGE[ALLUMETTES-1]=1 # on ajoute une boule jaune au tirage
                ALLUMETTES=ALLUMETTES-1 # on enleve une allumette
                print("UNE ALLUMETTE") # on imprime le nombre d'allumettes retirees
            else:
                TIRAGE[ALLUMETTES-1]=2 # on ajoute une boule rouge au tirage
                ALLUMETTES=ALLUMETTES-2 # on enleve deux allumettes
                print("DEUX ALLUMETTES") # on imprime le nombre d'allumettes retirees
            if ALLUMETTES==0: # si le nombre d'allumettes est nul
                WINNER='AKN' # l'ordinateur a gagne
            else:
                PLAYER='USER'   # sinon c'est au tour du joueur
        else: 
            COUPJOUEUR=0 # on initialise le coup du joueur
            print("\n-- A VOUS DE JOUER !--") # on affiche le message
            while COUPJOUEUR not in range(1, 3) or COUPJOUEUR>ALLUMETTES: # tant que le coup du joueur n'est pas valide
                try:  # on essaye de convertir le coup du joueur en entier
                    COUPJOUEUR = int(input("\n QUEL EST VOTRE CHOIX ?")) # on demande le coup du joueur
                    if COUPJOUEUR == 0: # si le coup du joueur est nul
                        print("\n VOUS DEVEZ ENLEVER AU MOINS UNE ALLUMETTE !") # on affiche le message
                    elif COUPJOUEUR not in range(1, 3) or COUPJOUEUR>ALLUMETTES: # si le coup du joueur n'est pas valide
                        print("\n VOUS NE POUVEZ PAS ENLEVER AUTANT D'ALLUMETTES !") # on affiche le message
                        COUPJOUEUR = int(input("\n QUEL EST VOTRE CHOIX ?")) # on redemande le coup du joueur
                except Exception as e: # si le coup du joueur n'est pas un entier
                    print("\n CELA NE SEMBLE PAS UNE REPONSE VALIDE.\n ERROR: " + str(e) + "\n RECOMMENCEZ !")  # on affiche le message d'erreur

            ALLUMETTES=ALLUMETTES-COUPJOUEUR # on enleve le coup du joueur au nombre d'allumettes
            if ALLUMETTES==0: # si le nombre d'allumettes est nul
                WINNER='USER' # le joueur a gagne
            else:
                PLAYER='AKN'  # sinon c'est au tour de l'ordinateur
    COMPTEURPARTIE+=1 # on incremente le compteur de parties
    
    if WINNER=='AKN': # si l'ordinateur a gagne
        # on affiche le tableau de jeu
        print("\n----------------------------------------------------------------------------")
        print("L'ORDINATEUR A GAGNE NOUS ALLONS LE RECOMPENSER")
        print("----------------------------------------------------------------------------\n")
    else: # sinon le joueur a gagne
        # on affiche le tableau de jeu
        print("\n----------------------------------------------------------------------------")
        print("BRAVO  VOUS AVEZ GAGNE  NOUS ALLONS PUNIR LORDINATEUR")
        print("----------------------------------------------------------------------------\n")
     
    if WINNER=='AKN':  # si l'ordinateur a gagne
        for i in range(NOMBREALLUMETTES): # pour chaque allumette du jeu
            if TIRAGE[i]==1: # si la boule est jaune
                BOULESJAUNES[i]=BOULESJAUNES[i]+1   # on ajoute une boule jaune
            if TIRAGE[i]==2: # si la boule est rouge
                BOULESROUGES[i]=BOULESROUGES[i]+1  # on ajoute une boule rouge
    else:  # sinon le joueur a gagne
        for i in range(NOMBREALLUMETTES): # pour chaque allumette du jeu
            if TIRAGE[i]==1: # si la boule est jaune
                BOULESJAUNES[i]=BOULESJAUNES[i]-1 # on enleve une boule jaune
            if TIRAGE[i]==2: # si la boule est rouge
                BOULESROUGES[i]=BOULESROUGES[i]-1 # on enleve une boule rouge

    for i in range(NOMBREALLUMETTES): # pour chaque allumette du jeu
        if (BOULESJAUNES[i]==0) and (BOULESROUGES[i]==0): # si il n'y a plus de boules jaunes et plus de boules rouges
            BOULESJAUNES[i]=2 # on ajoute deux boules jaunes
            BOULESROUGES[i]=2 # on ajoute deux boules rouges

    time.sleep(1) # on attend une seconde
    for i in range(NOMBREALLUMETTES): # pour chaque allumette du jeu
        print("DANS LE VERRE " + str(i+1) +", IL Y A " + str(BOULESJAUNES[i]) + " BOULES JAUNES ET " + str(BOULESROUGES[i]) + "  BOULES ROUGES.") # on affiche le nombre de boules jaunes et rouges dans le verre i+1

    time.sleep(1) # on attend une seconde
    if (BOULESJAUNES[3]/(BOULESJAUNES[3]+BOULESROUGES[3]))>(BOULESROUGES[4]/(BOULESJAUNES[4]+BOULESROUGES[4])): # si la proba de tirer une boule jaune dans le verre 4 est plus grande que la proba de tirer une boule rouge dans le verre 5
        proba=(BOULESROUGES[7]/(BOULESJAUNES[7]+BOULESROUGES[7]))*(BOULESROUGES[4]/(BOULESJAUNES[4]+BOULESROUGES[4]))*(BOULESROUGES[1]/(BOULESJAUNES[1]+BOULESROUGES[1])) # on calcule la proba de gagner
    else: # sinon
        proba=(BOULESROUGES[7]/(BOULESJAUNES[7]+BOULESROUGES[7]))*(BOULESJAUNES[3]/(BOULESJAUNES[3]+BOULESROUGES[3]))*(BOULESROUGES[1]/(BOULESJAUNES[1]+BOULESROUGES[1]))  # on calcule la proba de gagner
    print("\n----------------------------------------------------------------------------")
    print("VOUS AVEZ JOUE "+ str(COMPTEURPARTIE) +" PARTIES") # on affiche le nombre de parties jouees
    print("----------------------------------------------------------------------------\n")
    print("LA PROBABILITE DE GAIN DE LORDINATEUR A  LA PROCHAINE PARTIE SI LE JOUEUR JOUE DE MANIERE OPTIMALE (EN CONNAISSANT L'ETAT DES VERRES :-)) EST DE " + str(round(proba*100,2)) + "%") # on affiche la proba de gagner
    print("----------------------------------------------------------------------------\n")
    
    TEST=True # on initialise la variable TEST a True
    while TEST: # tant que TEST est True
        ANOTHERGO = input("\n VOULEZ-VOUS REJOUER ?[O/N]: ") # on demande si le joueur veut rejouer
        if ANOTHERGO in ("o","O"): # si le joueur veut rejouer il doit taper o ou O
            UNEAUTREPARTIE=True # on initialise la variable UNEAUTREPARTIE a True
            TEST=False # on initialise la variable TEST a False
        elif ANOTHERGO in ("n","N"): # si le joueur ne veut pas rejouer il doit taper n ou N
            UNEAUTREPARTIE=False # on initialise la variable UNEAUTREPARTIE a False
            TEST=False # on initialise la variable TEST a False
        else: # sinon
            print("\n CHOIX INVALIDE RECOMMENCEZ !")     # on affiche un message d'erreur pour demander au joueur de recommencer
############################################ 



############################## EXPLICATION BREVE DU JEU ###########################################

# Le jeu mystère est un jeu des allumettes joué entre l'utilisateur etl'ordinateur. Le jeu commence
# avec un certain nombre d'allumettes (8 par défaut), et les joueurs retirent alternativement un ou
# deux allumettes à chaque tour. Le joueur qui retire la dernière allumette perd.

# Le programme utilise la bibliothèque Python random pour que l'ordinateur fasse des choix aléatoires
# lors de son tour de jeu, tandis que l'utilisateur entre son choix à l'aide d'une entrée utilisateur.
# À chaque partie jouée, l'ordinateur reçoit une récompense s'il gagne et est puni s'il perd, afin
# qu'il apprenne à jouer de manière plus efficace à l'avenir. L'utilisateur peut choisir de rejouer 
# autant de fois qu'il le souhaite et reçoit une estimation de la probabilité de gagner de l'ordinateur
# à la prochaine partie s'il joue de manière optimale.



# In[ ]:




