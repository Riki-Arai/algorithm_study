import sys; sys.setrecursionlimit(10**7)

N = int(input()) # 数値：1

for i in range(N, 1000):
    if len(set(list(str(i)))) == 1:
        print(i)
        exit()