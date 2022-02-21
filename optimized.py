import csv
import time


def optimized(budget, stocks):
    matrice = [[0 for x in range(budget + 1)] for x in range(len(stocks) + 1)]

    for i in range(1, len(stocks) + 1):
        for w in range(1, budget + 1):
            if stocks[i-1][1] <= w:
                matrice[i][w] = max(stocks[i-1][2] + matrice[i-1][w-stocks[i-1][1]], matrice[i-1][w])
            else:
                matrice[i][w] = matrice[i-1][w]

    w = budget
    n = len(stocks)
    stocks_selection = []

    while w >= 0 and n >= 0:
        e = stocks[n-1]
        if matrice[n][w] == matrice[n-1][w-e[1]] + e[2]:
            stocks_selection.append(e)
            w -= e[1]

        n -= 1

    return stocks_selection


file = open('data.csv')
csvreader = csv.reader(file)
header = next(csvreader)
stocks = []
for stock in csvreader:
    stocks.append(stock)
file.close()

stocks = [
        (a[0], int(a[1]), int(a[1]) * int(a[2]) / 100) for a in stocks
    ]

sac = (optimized(500, stocks))

start_time = time.time()
print("\nBest combinations : \n")
for a in sac:
    print(str(a[0]) + ' for ' + str(a[1]) + '€ and ' + str(a[2]) + '€ of profits.')
print("\nTotal profits : \n")
print('    ' + str(round(sum(i[2] for i in sac), 2)) + '€ for a budget of ' + str(sum(i[1] for i in sac)) + '€.\n')

print("Execution time : --- %s seconds ---" % round(time.time() - start_time, 4))
