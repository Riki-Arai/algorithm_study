import math, itertools, bisect, functools
from collections import defaultdict, Counter, deque

N, M = map(int, input().split())
A_list = [input() for _ in range(N)] # 取得例：[A1、A2・・・An]、N行の入力用

res = 0
for c in itertools.combinations([i for i in range(N)], 2):
    i, j = c[0], c[1]
    for k in range(M):
        if A_list[i][k] == "o" or A_list[j][k] == "o":
            continue
        else:
            break
    else:
        res += 1

print(res)


### 以下はfirst
#N, M = map(int, input().split())
#A_list = [input() for _ in range(N)] # 取得例：[A1、A2・・・An]、N行の入力用
#
#res = 0
#for x in range(N):
#    for y in range(N):
#        if x != y:
#            for j in range(M):
#                if (A_list[x][j] == "o" or A_list[y][j] == "o"):
#                    continue
#                else:
#                    break
#            else:
#                res += 1
#
#print(res//2)