import sys; sys.setrecursionlimit(10**7)

N = int(input()) # 数値：1

res = 0
for _ in range(N):
    x, v = input().split() # 取得例：1 2
    x = float(x)
    if v == "JPY":
        res += x
    else:
        res += x* 380000

print(res)