import sys; sys.setrecursionlimit(10**7)

P, Q = map(int, input().split()) # 取得例：1 2
X, Y = map(int, input().split()) # 取得例：1 2

if P <= X <= P+99 and Q <= Y <= Q+99:
    print("Yes")
else:
    print("No")