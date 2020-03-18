#PokemonShowdown

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
    liste_actions_possible = Action(state,joueur)
    value_et_action_a_return = [-2,None]
    for action in liste_actions_possible:
        #Si la value est mieux que ce qu'on avait on prend cette action
        value = Min_Value(Result(state,action),joueur,opposant)
        if(value > value_et_action_a_return[0]):
            value_et_action_a_return = [value,action]
    return value_et_action_a_return

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


def Max_Value(state, joueur, opposant):
    if(Terminal_Test(state)) : return Utility(state,joueur)
    #valeur infiniment basse
    v = -2
    #Ici ce sont les actions du joueur qu'on prend car c'est son tour
    for a in Action(state,joueur):
        v = max(v,Min_Value(Result(state,a),joueur,opposant))
    return v




etat = [['X','','O'],['X','O',''],['','','']]
print("MiniMax : ",MiniMax(etat,'X'))



'''
REFLEXION

L'algo perd contre un être humain
Il semble mettre son symbole dans le premier emplacement où il est 'possible' de gagner
De ce que je vois, il ne privilégie pas une victoire immédiate assurée à un play lui permettant théoriquement
de gagner plus tard
Dans la situation [['X','','O'],['X','O',''],['','','']] il met son X en [0,1]
Vu au debug, l'action ['X',0,1] renvoie une valeur finale de 1 c'est pour cela qu'il la conserve
Pourquoi renvoie-t-elle 1 ?
Vu au debug, quand on teste une action le state change. Mais quand on veut en tester une autre, le state
conserve son état et ajoute la nouvelle modification
Cad en voulant tester Option 1 OU Option 2 on fait en fait Option1 OU Option 1 + 2 
'''



####################### work in progress #######################
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
    liste_actions_possible = Action(state,joueur)
    value_et_action_a_return = [-2,None]
    for action in liste_actions_possible:
        #Si la value est mieux que ce qu'on avait on prend cette action
        value = Max_Value_Alpha_Beta(Result(state,action),joueur,opposant,-2,2) #-2 et 2 représentent -infini et +infini
        if(value > value_et_action_a_return[0]):
            value_et_action_a_return = [value,action]
    return value_et_action_a_return



'''
Reflexion pour le tour de l'opposant, qui va prendre l'action qui a le gain minimum pour le joueur avec la méthode alpha beta (plus opti)

@ state     Une liste de liste au format [[-,-,-],[-,-,-],[-,-,-]] avec les symboles correspondants
@ joueur    Le symbole correspondant au joueur (X/O)
@ opposant  Le symbole correspondant à l'adversaire (X/O)
@ return    La valeur de l'utility d'un état
'''

def Min_Value_Alpha_Beta(state,joueur,opposant,alpha,beta):
    if(Terminal_Test(state)) : return Utility(state,joueur)
    fin_fonction = False #on doit s'arrêter si on trouve une value inférieur à alpha
    #valeur infiniment haute
    v = 2
    #Ici ce sont les actions de l'opposant qu'on prend car c'est son tour
    for a in Action(state,opposant):
        if (fin_fonction) : break #permet de sortir de la boucle, check sur https://courspython.com/boucles.html si tu veux voir comment ça marche
        v = min(v,Max_Value_Alpha_Beta(Result(state,a),joueur,opposant,alpha,beta))
        if (v <= alpha) : fin_fonction = True
        beta = min(beta,v)
    return v


'''
Reflexion pour le tour du joueur, qui va prendre l'action qui a le gain maximum pour lui avec la méthode alpha beta (plus opti)

@ state     Une liste de liste au format [[-,-,-],[-,-,-],[-,-,-]] avec les symboles correspondants
@ joueur    Le symbole correspondant au joueur (X/O)
@ opposant  Le symbole correspondant à l'adversaire (X/O)
@ return    La valeur de l'utility d'un état
'''


def Max_Value_Alpha_Beta(state,joueur,opposant,alpha,beta):
    if(Terminal_Test(state)) : return Utility(state,joueur)
    fin_fonction = False #on doit s'arrêter si on trouve une value inférieur à alpha
    #valeur infiniment haute
    v = -2
    #Ici ce sont les actions de l'opposant qu'on prend car c'est son tour
    for a in Action(state,joueur):
        if (fin_fonction) : break #permet de sortir de la boucle, check sur https://courspython.com/boucles.html si tu veux voir comment ça marche
        v = max(v,Min_Value_Alpha_Beta(Result(state,a),joueur,opposant,alpha,beta))
        if (v >= beta) : fin_fonction = True
        alpha = max(alpha,v)
    return v


etat2 = [['X','','O'],['X','O',''],['','','']]
print("Alpha_Beta :",Alpha_Beta(etat2,'X'))


'''
l'algo attribut la value 1 à ['X', 0, 1] donc il me renvoit celle-ci
je verrai demain ou tout à l'heure pour résoudre le problème
'''

