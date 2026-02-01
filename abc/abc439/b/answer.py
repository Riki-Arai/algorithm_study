N, K = map(int, input().split()) # 取得例：1 2

res = 0
add = N
while N < K:
    add += 1
    N += add
    res += 1

print(res)