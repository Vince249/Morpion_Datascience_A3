import Fonctions_de_base
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
    if(Fonctions_de_base.Terminal_Test(state)) : return Fonctions_de_base.Utility(state,joueur)
    #valeur infiniment haute
    v = 2
    #Ici ce sont les actions de l'opposant qu'on prend car c'est son tour
    for a in Fonctions_de_base.Action(state,opposant):
        v = min(v,Max_Value_Alpha_Beta(Fonctions_de_base.Result(state,a),joueur,opposant,alpha,beta))
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
    if(Fonctions_de_base.Terminal_Test(state)) : return Fonctions_de_base.Utility(state,joueur)
    #valeur infiniment haute
    v = -2
    if(renvoyer_action):
        sauvegarde_action = []
        #Ici ce sont les actions du joueur qu'on prend car c'est son tour
        for a in Fonctions_de_base.Action(state,joueur):
            ancien_v = v
            v = max(v,Min_Value_Alpha_Beta(Fonctions_de_base.Result(state,a),joueur,opposant,alpha,beta))
            if(ancien_v != v): sauvegarde_action=a
            if (v >= beta) : return [v,sauvegarde_action]
            alpha = max(alpha,v)
        return [v,sauvegarde_action]
    #Ici ce sont les actions de l'opposant qu'on prend car c'est son tour
    for a in Fonctions_de_base.Action(state,joueur):
        v = max(v,Min_Value_Alpha_Beta(Fonctions_de_base.Result(state,a),joueur,opposant,alpha,beta))
        if (v >= beta) : return v
        alpha = max(alpha,v)
    return v
