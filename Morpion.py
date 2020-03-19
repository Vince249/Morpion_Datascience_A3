import time

'''
Liste les actions possibles à partir d'un état donné
@ state     Une liste de liste au format [[-,-,-],[-,-,-],[-,-,-]] avec les symboles correspondants
@ joueur    Le symbole correspondant au joueur (X/O)
@ return    Une liste de listes au format [[X/O , x , y],...] avec x,y les coordonnées du X/O que l'action ajoute

UNIT TEST FAIT
'''
def Action (state, joueur):
    liste_actions = []
    for i in range(len(state)):
        for j in range (len(state)):
            if(state[i][j] != 'X' and state[i][j] != 'O'):
                liste_actions.append([joueur,i,j])
    return liste_actions

'''
Applique l'action à l'état state, on procède avec la fonction .copy() pour ne pas modifier le state d'origine
@ state     Une liste de liste au format [[-,-,-],[-,-,-],[-,-,-]] avec les symboles correspondants
@ action    Liste [joueur,i,j] avec joueur : 'X' ou 'O'
@ return    Le nouveau state au format [[-,-,-],[-,-,-],[-,-,-]] avec les symboles correspondants

UNIT TEST FAIT
'''
def Result(state,action):
    resultat = []
    for liste in state:
        resultat.append(liste.copy())
    resultat[action[1]][action[2]]=action[0]
    return resultat

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
                if((state[0][0] == state[1][1] and state[2][2] == state[1][1] and (state[1][1] == 'X' or state[1][1] == 'O')) or (state[1][1] == state[2][0] and state[2][0] == state[0][2] and (state[2][0] =='X' or state[2][0] =='O'))):
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

    if((state[0][0] == state[1][1] and state[2][2] == state[1][1] ) or (state[1][1] == state[2][0] and state[2][0] == state[0][2])):
        if(state[1][1] == joueur):
            result = 1
        else:
            result = -1

    return result


'''
Renvoie le meilleur play à faire suivant le state donné en considérant que l'adversaire va faire les plays optimum
Attention la fonction Utility est faite telle qu'on considère pouvoir étudier l'arbre en entier en sachant jusqu'où va nous mener chaque play

@ state     Une liste de liste au format [[-,-,-],[-,-,-],[-,-,-]] avec les symboles correspondants
@ joueur    Le symbole correspondant au joueur (X/O)
@ return    Une action optimale à faire par le joueur
'''
def MiniMax(state, joueur):
    if(joueur == 'X') : opposant = 'O'
    if(joueur == 'O') : opposant = 'X'
    resultat = Max_Value(state,joueur,opposant,True)
    return resultat

'''
Reflexion pour le tour de l'opposant, qui va prendre l'action qui a le gain minimum pour le joueur

@ state     Une liste de liste au format [[-,-,-],[-,-,-],[-,-,-]] avec les symboles correspondants
@ joueur    Le symbole correspondant au joueur (X/O)
@ opposant  Le symbole correspondant à l'adversaire (X/O)
@ return    La valeur de l'utility d'un état
'''

def Min_Value(state, joueur,opposant):
    if(Terminal_Test(state)) : return Utility(state,joueur)
    #valeur infiniment haute
    v = 2
    #Ici ce sont les actions de l'opposant qu'on prend car c'est son tour
    for a in Action(state,opposant):
        v = min(v,Max_Value(Result(state,a),joueur,opposant))
    return v


'''
Reflexion pour le tour du joueur, qui va prendre l'action qui a le gain maximum pour lui

@ state     Une liste de liste au format [[-,-,-],[-,-,-],[-,-,-]] avec les symboles correspondants
@ joueur    Le symbole correspondant au joueur (X/O)
@ opposant  Le symbole correspondant à l'adversaire (X/O)
@ return    La valeur de l'utility d'un état
'''


def Max_Value(state, joueur, opposant, renvoyer_action = False):
    if(Terminal_Test(state)) : return Utility(state,joueur)
    #valeur infiniment basse
    v = -2
    if(renvoyer_action):
        sauvegarde_action = []
        #Ici ce sont les actions du joueur qu'on prend car c'est son tour
        for a in Action(state,joueur):
            ancien_v = v
            v = max(v,Min_Value(Result(state,a),joueur,opposant))
            if(ancien_v != v): sauvegarde_action=a
        return [v,sauvegarde_action]
    #Ici ce sont les actions du joueur qu'on prend car c'est son tour
    for a in Action(state,joueur):
        v = max(v,Min_Value(Result(state,a),joueur,opposant))
    return v

''' 
Renvoie le meilleur play à faire suivant le state donné en considérant que l'adversaire va faire les plays optimum
mais ici on va élaguer des options afin de gagner en rapidité d'exécution (remplacerai fonction MiniMax)

@ state     Une liste de liste au format [[-,-,-],[-,-,-],[-,-,-]] avec les symboles correspondants
@ joueur    Le symbole correspondant au joueur (X/O)
@ return    Une action optimale à faire par le joueur
'''
def Alpha_Beta(state,joueur):
    if(joueur == 'X') : opposant = 'O'
    if(joueur == 'O') : opposant = 'X'
    resultat = Max_Value_Alpha_Beta(state,joueur,opposant,-2,2,True)
    return resultat


"""
Reflexion pour le tour de l'opposant, qui va prendre l'action qui a le gain minimum pour le joueur avec la méthode alpha beta (plus opti)

@ state     Une liste de liste au format [[-,-,-],[-,-,-],[-,-,-]] avec les symboles correspondants
@ joueur    Le symbole correspondant au joueur (X/O)
@ opposant  Le symbole correspondant à l'adversaire (X/O)
@ alpha     La valeur max déjà obtenue avec les autres options à cet étage, permet de déterminer quand faire une coupure alpha
@ beta      La valeur min déjà obtenue avec les autres options à cet étage, permet de déterminer quand faire une coupure beta
@ return    La valeur de l'utility d'un état
"""

def Min_Value_Alpha_Beta(state,joueur,opposant,alpha,beta):
    if(Terminal_Test(state)) : return Utility(state,joueur)
    #valeur infiniment haute
    v = 2
    #Ici ce sont les actions de l'opposant qu'on prend car c'est son tour
    for a in Action(state,opposant):
        v = min(v,Max_Value_Alpha_Beta(Result(state,a),joueur,opposant,alpha,beta))
        if (v <= alpha) : return v
        beta = min(beta,v)
    return v


'''
Reflexion pour le tour du joueur, qui va prendre l'action qui a le gain maximum pour lui avec la méthode alpha beta (plus opti)

@ state             Une liste de liste au format [[-,-,-],[-,-,-],[-,-,-]] avec les symboles correspondants
@ joueur            Le symbole correspondant au joueur (X/O)
@ opposant          Le symbole correspondant à l'adversaire (X/O)
@ alpha             La valeur max déjà obtenue avec les autres options à cet étage, permet de déterminer quand faire une coupure alpha
@ beta              La valeur min déjà obtenue avec les autres options à cet étage, permet de déterminer quand faire une coupure beta
@ renvoyer_action   Détermine s'il faut uniquement renvoyer la value ou aussi l'action associée
@ return            La valeur de l'utility d'un état (+ l'action associée)
'''


def Max_Value_Alpha_Beta(state,joueur,opposant,alpha,beta, renvoyer_action = False):
    if(Terminal_Test(state)) : return Utility(state,joueur)
    #valeur infiniment haute
    v = -2
    if(renvoyer_action):
        sauvegarde_action = []
        #Ici ce sont les actions du joueur qu'on prend car c'est son tour
        for a in Action(state,joueur):
            ancien_v = v
            v = max(v,Min_Value_Alpha_Beta(Result(state,a),joueur,opposant,alpha,beta))
            if(ancien_v != v): sauvegarde_action=a
            if (v >= beta) : return [v,sauvegarde_action]
            alpha = max(alpha,v)
        return [v,sauvegarde_action]
    #Ici ce sont les actions de l'opposant qu'on prend car c'est son tour
    for a in Action(state,joueur):
        v = max(v,Min_Value_Alpha_Beta(Result(state,a),joueur,opposant,alpha,beta))
        if (v >= beta) : return v
        alpha = max(alpha,v)
    return v



"""
! Je sais que la disposition que j'ai mise en dessous est impossible parce qu'il y a trop de O
! Mais elle permet d'assurer qu'un élagage ait lieu 
! Placer le X en [2,0] fait gagner direct, le placer en [2,1] te laisse 2 possibilités pour le placement du O (les deux faisant perdre le joueur)
! Si l'élagage fonctionne correctement, l'algo devrait placer O en [2,0], voir que la value est -1 et donc élager l'autre possibilité (faire une coupure alpha)
? Et c'est bien ce qui a lieu, tu peux le voir au debug

todo Fais un test pour chacun avec un etat vide ( [['','',''],['','',''],['','','']]  ) avec un vrai élagage et surtout en utilisant correctement les fonctions principales y a une vraie différence
"""
t0=time.time()
etat = [['X','O','O'],['X','O','O'],['','','']] 
print("MiniMax : ",MiniMax(etat,'X'))
print(time.time()-t0) #affiche temps d'exécution
t1=time.time()
etat2 = [['X','O','O'],['X','O','O'],['','','']] 
print("Alpha_Beta :",Alpha_Beta(etat2,'X'))
print(time.time()-t1) #affiche temps d'exécution