X, Y = map(int, input().split()) # 取得例：1 2

res = 0
common = 0
for a in range(1, 7):
    for b in range(1, 7):
        if a+b >= X:
            res += 1
        if abs(a-b) >= Y:
            res += 1
        if a+b >= X and abs(a-b) >= Y:
            common += 1

print((res-common)/36)