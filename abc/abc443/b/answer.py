import sys; sys.setrecursionlimit(10**7)

N, K = map(int, input().split()) # 取得例：1 2

total = N
res = 0
while total < K:
    res += 1
    N += 1
    total += N

print(res)