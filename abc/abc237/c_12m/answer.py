import sys, math, itertools, bisect, functools, copy, decimal
# 天井と床関数は丸める仕様らしく、桁数が上がると期待通りの動作をしないことを確認したのでimportしていない
from decimal import Decimal, ROUND_HALF_UP, ROUND_HALF_EVEN, ROUND_UP, ROUND_DOWN # 左のROUND_HALF_UPから四捨五入、四捨五入(銀行丸め)、切り上げ、切り捨て
from sortedcontainers import SortedSet, SortedList, SortedDict
from collections import defaultdict, Counter, deque
from atcoder.dsu import DSU
sys.setrecursionlimit(10**7)

S = input().strip()

if S == S[::-1]:
    print("Yes")
    exit()
else:
    l = 0
    for i in range(len(S)):
        if S[i] == "a":
            l += 1
        else:
            break
    r = 0
    r_s = S[::-1]
    for i in range(len(S)):
        if r_s[i] == "a":
            r += 1
        else:
            break

    if r > l:
        new_s = "a"*(r-l) + S
        if new_s == new_s[::-1]:
            print("Yes")
            exit()

print("No")