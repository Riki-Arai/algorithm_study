T = int(input()) # 数値：1

for _ in range(T):
    X1, Y1, R1, X2, Y2, R2 = map(int, input().split()) # 取得例：1 2
    if pow(abs(X1-X2), 2) + pow(abs(Y1-Y2), 2) > pow(R1+R2, 2) or pow(pow(abs(X1-X2), 2) + pow(abs(Y1-Y2), 2), 0.5) + min(R1, R2) < max(R1, R2):
        print("No")
    else:
        print("Yes")