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
@ return    Le nouveau state au format [[-,-,-],[-,-,-],[-,-,-]] avec les symboles correspondants

UNIT TEST FAIT
'''
def Result(state,action):
    state[action[1]][action[2]]=action[0]
    return state

'''
Vérifie si l'état state est terminal
@ state     Une liste de liste au format [[-,-,-],[-,-,-],[-,-,-]] avec les symboles correspondants
@ nb        Le nombre de cases qui doivent être alignées pour finir
@ return    True/False

UNIT TEST FAIT
'''
def Terminal_Test(state,nb=3):
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
@ state     Une liste de liste au format [[-,-,-],[-,-,-],[-,-,-]] avec les symboles correspondants
@ joueur    Le symbole correspondant au joueur (X/O)
@ return    +1 pour une victoire, 0 pour une défaite, -1 pour une défaite

UNIT TEST FAIT
'''
def Utility (state, joueur):
    #ligne
    result = 0
    for element in state :
        if(element[0]==element[1] and element[2]==element[1]):
            if(element[0] == joueur):
                result = 1
            else:
                result = -1
    #colonne
    for i in range (len(state)):
        listetemp = []
        for j in range (len(state)):
            listetemp.append(state[j][i])
        if(listetemp[0]==listetemp[1] and listetemp[2]==listetemp[1]):
            if(listetemp[0] == joueur):
                result = 1
            else:
                result = -1
    #diagonale

    if((state[0][0] == state[1][1] and state[2][2] == state[1][1]) or (state[1][1] == state[2][0] and state[2][0] == state[0][2])):
        if(state[0][0] == joueur):
            result = 1
        else:
            result = -1

    return result

'''

///////////////////////////////////////////////////  WORK IN PROGRESS  //////////////////////////////////////////////////////////////

'''

'''
Renvoie le meilleur play à faire suivant le state donné en considérant que l'adversaire va faire les plays optimum
Attention la fonction Utility est faite telle qu'on considère pouvoir étudier l'arbre en entier en sachant jusqu'où va nous mener chaque play

@ state     Une liste de liste au format [[-,-,-],[-,-,-],[-,-,-]] avec les symboles correspondants
@ joueur    Le symbole correspondant au joueur (X/O)
@return     Une action optimale à faire par le joueur
'''
def MiniMax(state, joueur):
    listeactionspossible = Action(state,joueur)
    valueetactionareturn = [-2,None]
    for action in listeactionspossible:
        #Si la value est mieux que ce qu'on avait on prend cette action
        valeur = Result(state,action)
        if(valeur > valueetactionareturn[0]):
            valueetactionareturn = [valeur,action]
    return valueetactionareturn

#cette ligne est a supprimé c'est un test pour commit