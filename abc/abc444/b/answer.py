import sys; sys.setrecursionlimit(10**7)

N, K = map(int, input().split()) # 取得例：1 2

res = 0
for i in range(1, N+1):
    if sum(map(int, list(str(i)))) == K:
        res += 1

print(res)