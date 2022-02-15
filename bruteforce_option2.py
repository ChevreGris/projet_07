budget = 500

#(Action, Prix, Benefice)
actions = [
    ("Action-1", 20, 5),
    ("Action-2", 30, 10),
    ("Action-3", 50, 15),
    ("Action-4", 70, 20),
    ("Action-5", 60, 17),
    ("Action-6", 80, 25),
    ("Action-7", 22, 7),
    ("Action-8", 26, 11),
    ("Action-9", 48, 13),
    ("Action-10", 34, 27),
    ("Action-11", 42, 17),
    ("Action-12", 110, 9),
    ("Action-13", 38, 23),
    ("Action-14", 14, 1),
    ("Action-15", 18, 3),
    ("Action-16", 8, 8),
    ("Action-17", 4, 12),
    ("Action-18", 10, 14),
    ("Action-19", 24, 21),
    ("Action-20", 114, 18)
]

actions = [
    (a[0], a[1], a[1] * a[2] / 100) for a in actions
]

def brut_force(budget, actions, action_selection = []):
    #tant qu'il y a des actions non traité la boucle continue.
    if actions:
        #ignore la première action de la liste 
        val1, lstVal1 = brut_force(budget, actions[1:], action_selection)
        #prend la premier action de la liste
        val = actions[0]
        #verifie si elle peut rentrer dans le budget, sinon est supprimé avec la ligne 32 appelé en ligne 46.
        if val[1] <= budget:
            #enlève du budget le coût de cette action, renvoie la liste sans la première action que nous venons de traité,
            #et envoie dans la liste des actions que nous gardon la première action que nous venons de traité.
            val2, lstVal2 = brut_force(budget - val[1], actions[1:], action_selection + [val])
            #avons nous un meilleur resultat en ajoutant l'action ou non.
            if val1 < val2:
                #si oui, retourne la fonction pour l'executer
                return val2, lstVal2
        #si non, retourne l'autre version pour l'executer
        return val1, lstVal1
    else:
        return sum([i[1] for i in action_selection]), action_selection  

print("ALGO Force Brut:")
print(brut_force(budget, actions))
