X, Y = map(int, input().split()) # 取得例：1 2

a1 = X
a2 = Y
res = a1+a2
for _ in range(8):
    res = int(str(a1+a2)[::-1])
    a1 = a2
    a2 = res

print(res)