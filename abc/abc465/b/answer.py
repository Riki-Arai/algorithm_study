X, Y, L, R, A, B = map(int, input().split()) # 取得例：1 2

res = 0
for i in range(A, B):
    if L < i+1 <= R:
        res += X
    else:
        res += Y

print(res)