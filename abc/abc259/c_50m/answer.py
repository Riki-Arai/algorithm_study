import sys, math, itertools, bisect, functools, copy, decimal
# 天井と床関数は丸める仕様らしく、桁数が上がると期待通りの動作をしないことを確認したのでimportしていない
from decimal import Decimal, ROUND_HALF_UP, ROUND_HALF_EVEN, ROUND_UP, ROUND_DOWN # 左のROUND_HALF_UPから四捨五入、四捨五入(銀行丸め)、切り上げ、切り捨て
from collections import defaultdict, Counter, deque
from atcoder.dsu import DSU
sys.setrecursionlimit(10**7)

S = input().strip()
T = input().strip()

if len(S) > len(T):
    print("No")
    exit()

if len(list(itertools.groupby(S))) != len(list(itertools.groupby(T))):
    print("No")
    exit()

if len(set(S)) != len(set(T)):
    print("No")
    exit()

for s, t in zip(itertools.groupby(S), itertools.groupby(T)):
    sk, sg = s
    tk, tg = t
    if sk == tk:
        s_list = list(sg)
        t_list = list(tg)
        if len(s_list) == len(t_list):
            continue
        else:
            if len(s_list) >= 2 and len(t_list) >= len(s_list):
                continue
            else:
                print("No")
                exit()
    else:
        print("No")
        exit()

print("Yes")