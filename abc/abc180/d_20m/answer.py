X, Y, A, B = map(int, input().split()) # 取得例：1 2

res = 0
while (X*A-X) < B and X < Y:
    X *= A
    res += 1

res += ((Y-1)-X)//B
print(res)