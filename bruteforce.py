from itertools import combinations
import time

Stocks = [
    ("Stock-1", 20, 5),
    ("Stock-2", 30, 10),
    ("Stock-3", 50, 15),
    ("Stock-4", 70, 20),
    ("Stock-5", 60, 17),
    ("Stock-6", 80, 25),
    ("Stock-7", 22, 7),
    ("Stock-8", 26, 11),
    ("Stock-9", 48, 13),
    ("Stock-10", 34, 27),
    ("Stock-11", 42, 17),
    ("Stock-12", 110, 9),
    ("Stock-13", 38, 23),
    ("Stock-14", 14, 1),
    ("Stock-15", 18, 3),
    ("Stock-16", 8, 8),
    ("Stock-17", 4, 12),
    ("Stock-18", 10, 14),
    ("Stock-19", 24, 21),
    ("Stock-20", 114, 18)
]

Stocks = [
    (a[0], a[1], a[1] * a[2] / 100) for a in Stocks
]

start_time = time.time()

max = 500
best_profit = 0
best_comb = None
for i in range(len(Stocks)):
    for comb in combinations(Stocks, i + 1):
        price = sum(i[1] for i in comb)
        profit = sum(i[2] for i in comb)
        if price <= max and profit > best_profit:
            best_profit = profit
            best_comb = comb

print("\nBest combinations : \n")
for a in best_comb:
    print(str(a[0]) + ' for ' + str(a[1]) + '€ and ' + str(a[2]) + '€ of profits.')
print("\nTotal profits : \n")    
print('    ' + str(round(best_profit, 2)) + '€ for a budget of ' + str(sum(i[1] for i in best_comb)) + '€.\n')

print("Execution time : --- %s seconds ---" % round(time.time() - start_time, 4))
