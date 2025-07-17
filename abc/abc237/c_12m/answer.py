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
else:
    g_lists = []
    for k, v in itertools.groupby(S):
        g_lists.append((k, len(list(v))))
    if g_lists[-1][0] == "a":
        a_num = g_lists[-1][1]
        if g_lists[0][0] == "a":
            h_a_num = g_lists[0][1]
            if h_a_num < a_num:
                add_s = "a"*(a_num-h_a_num) + S
                if add_s == add_s[::-1]:
                    print("Yes")
                else:
                    print("No")
            else:
                print("No")
        else:
            add_s = "a"*a_num + S
            if add_s == add_s[::-1]:
                print("Yes")
            else:
                print("No")
    else:
        print("No")