import csv
import time

file = open('dataset1_Python+P7.csv')
csvreader = csv.reader(file)
header = next(csvreader)
stocks = []
for stock in csvreader:
    if float(stock[1]) > 0.0 :
        stocks.append(stock)
file.close()

stocks = [
        (a[0], int(float(a[1])*100), (float(a[1]) * float(a[2]))) for a in stocks
    ]

start_time = time.time()

def optimized(capacite, stocks):
    matrice = [[0 for x in range(capacite + 1)] for x in range(len(stocks) + 1)]

    for i in range(1, len(stocks) + 1):
        for w in range(1, capacite + 1):
            if stocks[i-1][1] <= w:
                matrice[i][w] = max(stocks[i-1][2] + matrice[i-1][w-stocks[i-1][1]], matrice[i-1][w])
            else:
                matrice[i][w] = matrice[i-1][w]

    # Retrouver les éléments en fonction de la somme
    w = capacite
    n = len(stocks)
    stocks_selection = []

    while w >= 0 and n >= 0:
        e = stocks[n-1]
        if matrice[n][w] == matrice[n-1][w-e[1]] + e[2]:
            stocks_selection.append(e)
            w -= e[1]

        n -= 1

    return stocks_selection

sac = (optimized(50000, stocks))

print('\n------------------------------------------------------')
print('\nNumber of usable stocks : ' +  str(len(stocks)))
print("\nBest combinations : \n")
for a in sac:
    print('    ' + str(a[0]) + ' for ' + str(round(a[1]/100, 2)) + '€ and ' + str(round(a[2]/100, 2)) + '€ of profits.')
print("\nTotal profits : \n")    
print('    ' + str(round(sum(i[2]/100 for i in sac), 2)) + '€ for a budget of ' + str(round(sum(i[1]/100 for i in sac), 2)) + '€.\n')
print("\nExecution time : --- %s seconds ---" % round(time.time() - start_time, 4))
print('\n------------------------------------------------------')
