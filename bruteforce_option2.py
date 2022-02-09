budget = 500

#(Action, Prix, Benefice, %)
actions = [(1, 20, 1, 0.05),
           (2, 30, 3, 0.10),
           (3, 50, 7.5, 0.15),
           (4, 70, 14, 0.20),
           (5, 60, 10.2, 0.17),

           (6, 80, 21.6, 0.27),
           (7, 22, 1.54, 0.07),
           (8, 26, 2.86, 0.11),
           (9, 48, 6.24, 0.13),
           (10, 34, 9.18, 0.27),

           (11, 42, 7.14, 0.17),
           (12, 110, 9.9, 0.09),
           (13, 38, 8.74, 0.23),
           (14, 14, 0.14, 0.01),
           (15, 18, 0.54, 0.03),

           (16, 8, 0.64, 0.08),
           (17, 4, 0.48, 0.12),
           (18, 10, 1.4, 0.14),
           (19, 24, 5.04, 0.21),
           (20, 114, 20.52, 0.18)]

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
