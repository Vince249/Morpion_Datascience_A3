import Fonctions_de_base
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
    if(Fonctions_de_base.Terminal_Test(state)) : return Fonctions_de_base.Utility(state,joueur)
    #valeur infiniment haute
    v = 2
    #Ici ce sont les actions de l'opposant qu'on prend car c'est son tour
    for a in Fonctions_de_base.Action(state,opposant):
        v = min(v,Max_Value(Fonctions_de_base.Result(state,a),joueur,opposant))
    return v


'''
Reflexion pour le tour du joueur, qui va prendre l'action qui a le gain maximum pour lui

@ state     Une liste de liste au format [[-,-,-],[-,-,-],[-,-,-]] avec les symboles correspondants
@ joueur    Le symbole correspondant au joueur (X/O)
@ opposant  Le symbole correspondant à l'adversaire (X/O)
@ return    La valeur de l'utility d'un état
'''


def Max_Value(state, joueur, opposant, renvoyer_action = False):
    if(Fonctions_de_base.Terminal_Test(state)) : return Fonctions_de_base.Utility(state,joueur)
    #valeur infiniment basse
    v = -2
    if(renvoyer_action):
        sauvegarde_action = []
        #Ici ce sont les actions du joueur qu'on prend car c'est son tour
        for a in Fonctions_de_base.Action(state,joueur):
            ancien_v = v
            v = max(v,Min_Value(Fonctions_de_base.Result(state,a),joueur,opposant))
            if(ancien_v != v): sauvegarde_action=a
        return [v,sauvegarde_action]
    #Ici ce sont les actions du joueur qu'on prend car c'est son tour
    for a in Fonctions_de_base.Action(state,joueur):
        v = max(v,Min_Value(Fonctions_de_base.Result(state,a),joueur,opposant))
    return v
