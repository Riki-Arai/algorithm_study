import sys; sys.setrecursionlimit(10**7)

s = int(input()) # 数値：1

res_set = set()
res_set.add(s)
for i in range(2, 10**7):
    if s%2 == 0:
        s //= 2
    else:
        s = 3*s + 1

    if s in res_set:
        print(i)
        exit()
    else:
        res_set.add(s)