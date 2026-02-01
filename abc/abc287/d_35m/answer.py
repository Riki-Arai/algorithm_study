import sys, math, itertools, bisect, functools, copy, decimal
from more_itertools import distinct_permutations
from functools import cmp_to_key
# 天井と床関数は丸める仕様らしく、桁数が上がると期待通りの動作をしないことを確認したのでimportしていない
from decimal import Decimal, ROUND_HALF_UP, ROUND_HALF_EVEN, ROUND_UP, ROUND_DOWN # 左のROUND_HALF_UPから四捨五入、四捨五入(銀行丸め)、切り上げ、切り捨て
from sortedcontainers import SortedSet, SortedList, SortedDict
from collections import defaultdict, Counter, deque
from atcoder.dsu import DSU
sys.setrecursionlimit(10**7)

S = input().strip()
T = input().strip()

not_match_set = set()
s_dict = defaultdict(str)
t_dict = defaultdict(str)
s = S[-len(T):]
for i in range(len(T)):
    s_dict[i] = s[i]
    t_dict[i] = T[i]
    if s[i] != "?" and T[i] != "?" and s[i] != T[i]:
        not_match_set.add(i)

if len(not_match_set) == 0:
    print("Yes")
else:
    print("No")

for i in range(len(T)):
    s_dict[i] = S[i]
    if s_dict[i] != "?" and t_dict[i] != "?" and s_dict[i] != t_dict[i]:
        not_match_set.add(i)
    elif s_dict[i] == "?" or t_dict[i] == "?" or s_dict[i] == t_dict[i]:
        if i in not_match_set:
            not_match_set.discard(i)

    if len(not_match_set) == 0:
        print("Yes")
    else:
        print("No")