N, M = map(int, input().split()) # 取得例：1 2

res = 0
while M > 0:
    M = N%M
    res += 1

print(res)