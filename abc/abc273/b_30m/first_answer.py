X, K = map(int, input().split())

for i in range(K):
    j = (i + 1)
    y_1 = 10 ** j * (X // (10 ** j))
    y_2 = 10 ** j * (X // (10 ** j) + 1)
    if abs(y_1 - X) > abs(y_2 - X):
        X = y_2
    elif abs(y_1 - X) < abs(y_2 - X):
        X = y_1
    else:
        X = max(y_1, y_2)

print(X)