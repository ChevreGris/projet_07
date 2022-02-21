import csv
import time


def optimized(budget, stocks):
    # la matrice représente le tableau
    matrice = [[0 for x in range(budget + 1)] for x in range(len(stocks) + 1)]

    # localise chaques actions
    for i in range(1, len(stocks) + 1):
        # budget decomposé un par un
        for w in range(1, budget + 1):
            # si la valeur i est inf ou = au budget dispo, alors :
            if stocks[i-1][1] <= w:
                # inscit dans la matrice le resultat en comparant l'action courente et l'action d'avant.
                matrice[i][w] = max(stocks[i-1][2] + matrice[i-1][w-stocks[i-1][1]], matrice[i-1][w])
            # sinon :
            else:
                # garde l'action d'avant
                matrice[i][w] = matrice[i-1][w]

    # Retrouver les éléments en fonction de la somme
    w = budget
    n = len(stocks)
    stocks_selection = []

    # tant que le budget est >= 0 ou que nous n'avons pas fini de parcourir les actions:
    while w >= 0 and n >= 0:
        # selectionne la dernière action
        e = stocks[n-1]
        # si = au max :
        if matrice[n][w] == matrice[n-1][w-e[1]] + e[2]:
            # ajoute l'action au actions sélectionnées
            stocks_selection.append(e)
            # retire du budget le prix de l'action retenu
            w -= e[1]
        # passe à l'action suivente
        n -= 1
    
    # retourne les actions sélectionnées
    return stocks_selection


file = open('dataset1_Python+P7.csv')
csvreader = csv.reader(file)
header = next(csvreader)
stocks = []
for stock in csvreader:
    if float(stock[1]) > 0.0:
        stocks.append(stock)
file.close()

stocks = [
        (a[0], int(float(a[1])*100), (float(a[1]) * float(a[2]))) for a in stocks
    ]

start_time = time.time()
sac = (optimized(50000, stocks))

print('\n------------------------------------------------------')
print('\nNumber of usable stocks : ' + str(len(stocks)))
print("\nBest combinations : \n")
for a in sac:
    print('    ' + str(a[0]) + ' for ' + str(round(a[1]/100, 2)) + '€ and ' + str(round(a[2]/100, 2)) 
    + '€ of profits.')
print("\nTotal profits : \n")
print('    ' + str(round(sum(i[2]/100 for i in sac), 2)) + '€ for a budget of ' 
+ str(round(sum(i[1]/100 for i in sac), 2)) + '€.\n')
print("\nExecution time : --- %s seconds ---" % round(time.time() - start_time, 4))
print('\n------------------------------------------------------')

