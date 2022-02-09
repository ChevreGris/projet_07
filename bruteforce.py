from itertools import combinations
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

max = 500
best_profit = 0
best_comb = None
for i in range(len(actions)):
    for comb in combinations(actions, i + 1):
        price = sum(i[1] for i in comb)
        profit = sum(i[2] for i in comb)
        if price <= max and profit > best_profit:
            best_profit = profit
            best_comb = comb
print(best_comb, best_profit, sum(i[1] for i in best_comb))