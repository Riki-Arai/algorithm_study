import sys, math, itertools, bisect, functools, copy, decimal
from more_itertools import distinct_permutations
from functools import cmp_to_key
# 天井と床関数は丸める仕様らしく、桁数が上がると期待通りの動作をしないことを確認したのでimportしていない
from decimal import Decimal, ROUND_HALF_UP, ROUND_HALF_EVEN, ROUND_UP, ROUND_DOWN # 左のROUND_HALF_UPから四捨五入、四捨五入(銀行丸め)、切り上げ、切り捨て
from sortedcontainers import SortedSet, SortedList, SortedDict
from collections import defaultdict, Counter, deque
from atcoder.dsu import DSU
sys.setrecursionlimit(10**7)

A_list = list(map(int, input().split())) # 取得例：[1,2,3]、1行の入力用

for c in itertools.combinations(A_list, 5):
    counter = Counter(list(c))
    if len(counter.keys()) == 2:
        for v in counter.values():
            if v not in set([2, 3]):
                break
        else:
            print("Yes")
            exit()

print("No")