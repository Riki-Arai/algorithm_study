import sys, math, itertools, bisect, functools, copy, decimal
# 天井と床関数は丸める仕様らしく、桁数が上がると期待通りの動作をしないことを確認したのでimportしていない
from decimal import Decimal, ROUND_HALF_UP, ROUND_HALF_EVEN, ROUND_UP, ROUND_DOWN # 左のROUND_HALF_UPから四捨五入、四捨五入(銀行丸め)、切り上げ、切り捨て
from sortedcontainers import SortedSet, SortedList, SortedDict
from collections import defaultdict, Counter, deque
from atcoder.dsu import DSU
sys.setrecursionlimit(10**7)

N, Q = map(int, input().split())
A_list = list(map(int, input().split())) # 取得例：[1, 2, 3]、1行の入力用

res_dict = defaultdict(list)
for i, a in enumerate(A_list, 1):
    res_dict[a].append(i)

for _ in range(Q):
    x, k = map(int, input().split())
    if x in res_dict:
        if len(res_dict[x]) > k-1:
            print(res_dict[x][k-1])
        else:
            print(-1)
    else:
        print(-1)