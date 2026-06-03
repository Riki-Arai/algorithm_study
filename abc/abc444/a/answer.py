import sys; sys.setrecursionlimit(10**7)

N = int(input()) # 数値：1

if len(set(str(N))) == 1:
    print("Yes")
else:
    print("No")