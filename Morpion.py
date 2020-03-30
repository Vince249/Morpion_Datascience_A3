#Rémi GUILLON BONY et Vincent POUPET

import time
import Fonctions_de_base
import MiniMax
import AlphaBetaMiniMax

'''
#! READ ME

Pour jouer contre l'IA, il faut utiliser les listes de liste etat et etat2
La variable etat est utilisée par la fonction MiniMax, etat2 par la fonction Elagage Alpha Beta
Nous avons laissé ces deux algorithmes fonctionner en parallèle afin de pouvoir montrer que l'un est plus rapide que l'autre


On initialise la partie en laissant ces listes vides
Si on lance le programme, l'IA va jouer son tour en étant les X (on peut le changer en modifiant le paramètre dans l'appel de la fonction)
Elle va alors indiquer le play qu'elle recommande et le programme s'arrête
Si on veut relancer le programme il faut auparavant mettre à jour les variables etat et etat2 avec le nouvel état du jeu

Nous n'avons pas mis de boucle afin de pouvoir afficher le temps que mettent chacune des méthodes (MiniMax et Elagage) pour chaque play

JOUER CONTRE L'IA

Pour jouer contre l'IA, on peut appliquer le play qu'elle conseille aux variables etat et etat2, puis placer le O là où on le veut
On peut ensuite relancer le programme pour que l'IA nous donne son play suivant

JOUER CONTRE UNE AUTRE IA

On informe notre IA de l'état du jeu à travers la variable etat et on lui demande quoi faire
Elle va nous indiquer le play qu'elle recommande


'''

#ALPHA BETA

t1=time.time()
etat2 = [['','',''],['','',''],['','','']] 
result_AlphaBetaMiniMax = AlphaBetaMiniMax.Alpha_Beta(etat2,'X')
print('Algorithme Elagage AlphaBeta')
print('Solution trouvée en '+ str(time.time()-t1 ) + ' s')
print("L'IA recommande de placer " + str(result_AlphaBetaMiniMax[1][0]) + " en " + str(result_AlphaBetaMiniMax[1][1]) + " " + str(result_AlphaBetaMiniMax[1][2]))
print('')
#MINIMAX NORMAL

t0=time.time()
etat = [['','',''],['','',''],['','','']] 
result_MiniMax = MiniMax.MiniMax(etat,'X')
print('Algorithme MiniMax')
print('Solution trouvée en '+ str(time.time()-t0 ) + ' s')
print("L'IA recommande de placer " + str(result_MiniMax[1][0]) + " en " + str(result_MiniMax[1][1]) + " " + str(result_MiniMax[1][2]))

