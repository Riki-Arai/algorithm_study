import math

N = int(input())
res = 0
for i in range(N):
    if i == 0:
        X_1, Y_1 = 0, 0
        X_2, Y_2 = list(map(int, input().split()))
        res += math.sqrt(pow(abs(X_2 - X_1), 2) + pow(abs(Y_2 - Y_1), 2))
        X_1, Y_1 = X_2, Y_2
    else:
        X_2, Y_2 = list(map(int, input().split()))
        res += math.sqrt(pow(abs(X_2 - X_1), 2) + pow(abs(Y_2 - Y_1), 2))
        X_1, Y_1 = X_2, Y_2

X_2, Y_2 = 0, 0
res += math.sqrt(pow(abs(X_1 - X_2), 2) + pow(abs(Y_1 - Y_2), 2))
print(res)
