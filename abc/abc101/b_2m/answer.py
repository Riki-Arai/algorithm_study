import sys; sys.setrecursionlimit(10**7)

N = int(input()) # 数値：1

if N%sum(map(int, list(str(N)))) == 0:
    print("Yes")
else:
    print("No")