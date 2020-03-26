import time
import Fonctions_de_base
import MiniMax
import AlphaBetaMiniMax

"""
! Je sais que la disposition que j'ai mise en dessous est impossible parce qu'il y a trop de O
! Mais elle permet d'assurer qu'un élagage ait lieu 
! Placer le X en [2,0] fait gagner direct, le placer en [2,1] te laisse 2 possibilités pour le placement du O (les deux faisant perdre le joueur)
! Si l'élagage fonctionne correctement, l'algo devrait placer O en [2,0], voir que la value est -1 et donc élager l'autre possibilité (faire une coupure alpha)
? Et c'est bien ce qui a lieu, tu peux le voir au debug

todo Fais un test pour chacun avec un etat vide ( [['','',''],['','',''],['','','']]  ) avec un vrai élagage et surtout en utilisant correctement les fonctions principales y a une vraie différence
"""
t0=time.time()
etat = [['','',''],['','',''],['','','']] 
print("MiniMax : ",MiniMax.MiniMax(etat,'X'))
print(time.time()-t0) #affiche temps d'exécution
t1=time.time()
etat2 = [['','',''],['','',''],['','','']] 
print("Alpha_Beta :",AlphaBetaMiniMax.Alpha_Beta(etat2,'X'))
print(time.time()-t1) #affiche temps d'exécution