#PokemonShowdown

'''
Liste les actions possibles à partir d'un état donné
@ state     Une liste de liste au format [[-,-,-],[-,-,-],[-,-,-]] avec les symboles correspondants
@ joueur    Le symbole correspondant au joueur (X/O)
@ return    Une liste de listes au format [[X/O , x , y],...] avec x,y les coordonnées du X/O que l'action ajoute

UNIT TEST FAIT
'''
def Action (state, joueur):
    listeactions = []
    for i in range(len(state)):
        for j in range (len(state)):
            if(state[i][j] != 'X' and state[i][j] != 'O'):
                listeactions.append([joueur,i,j])
    return listeactions

'''
Applique l'action à l'état state
@ state     Une liste de liste au format [[-,-,-],[-,-,-],[-,-,-]] avec les symboles correspondants
@ action    Liste [joueur,i,j] avec joueur : 'X' ou 'O'
@ return    /

UNIT TEST FAIT
'''
def Result(state,action):
     state[action[1]][action[2]]=action[0]
     return

'''
Vérifie si l'état state est terminal
@ state     Une liste de liste au format [[-,-,-],[-,-,-],[-,-,-]] avec les symboles correspondants
@ nb        Le nombre de cases qui doivent être alignées pour finir
@ return    True/False

UNIT TEST FAIT
'''
def Terminal_Test(state,nb):
    reponse = False
    plein = True
    #si toutes les cases sont remplies, fini
    #si 3 croix/ronds sont alignés
    for element in state:
        for case in element:
            if(case != 'X' and case != 'O'): plein = False 
    if(not plein):
        #lignes
        for element in state :
            if (element == ['X','X','X'] or element == ['O','O','O']):
                reponse = True
        if(not reponse):
            #colonnes
            for i in range (len(state)):
                listetemp = []
                for j in range (len(state)):
                    listetemp.append(state[j][i])
                if (listetemp == ['X','X','X'] or listetemp == ['O','O','O']) :
                    reponse = True
            if(not reponse):
                #diagonales
                if((state[0][0] == state[1][1] and state[2][2] == state[1][1]) or (state[1][1] == state[2][0] and state[2][0] == state[0][2])):
                    reponse = True
    else:
        reponse= True
    return reponse

'''
Détermine l'intérêt d'un état
@ return    +1 pour une victoire, 0 pour une défaite, -1 pour une défaite
'''

            

