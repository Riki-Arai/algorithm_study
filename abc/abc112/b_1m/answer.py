import sys; sys.setrecursionlimit(10**7)

N, T = map(int, input().split()) # 取得例：1 2

res = float("INF")
for _ in range(N):
    c, t = map(int, input().split()) # 取得例：1 2
    if t <= T:
        res = min(c, res)

if res == float("INF"):
    print("TLE")
else:
    print(res)