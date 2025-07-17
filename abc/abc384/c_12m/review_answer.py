import sys, math, itertools, bisect, functools, copy, decimal
# 天井と床関数は丸める仕様らしく、桁数が上がると期待通りの動作をしないことを確認したのでimportしていない
from decimal import Decimal, ROUND_HALF_UP, ROUND_HALF_EVEN, ROUND_UP, ROUND_DOWN # 左のROUND_HALF_UPから四捨五入、四捨五入(銀行丸め)、切り上げ、切り捨て
from sortedcontainers import SortedSet, SortedList, SortedDict
from collections import defaultdict, Counter, deque
from atcoder.dsu import DSU
sys.setrecursionlimit(10**7)

a, b, c, d, e = map(int, input().split())

res_lists = []
score_dict = {'A':a, 'B':b, 'C':c, 'D':d, 'E':e}
alp_list = ['A', 'B', 'C', 'D', 'E']
p_lists = list(itertools.product([0, 1], repeat=5))
for p_list in p_lists:
    tmp_alp_list = []
    score = 0
    for i, p in enumerate(p_list):
        if p == 1:
            tmp_alp_list.append(alp_list[i])
            score += score_dict[alp_list[i]]

    if len(tmp_alp_list):
        res_lists.append((''.join(tmp_alp_list), -score))

res_lists.sort(key=lambda x: (x[1], x[0]))
for res_list in res_lists:
    print(res_list[0])