import sys; sys.setrecursionlimit(10**7)

S = input().strip() # 取得例："A"

res = 0
for s in S:
    if s in ("i", "j"):
        res += 1

print(res)