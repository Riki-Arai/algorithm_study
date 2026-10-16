import sys, math, itertools as it, bisect as bi, functools as ft, copy, decimal, heapq as hq
from more_itertools import distinct_permutations
from functools import cmp_to_key
#  天井と床関数は丸める仕様らしく、桁数が上がると期待通りの動作をしないことを確認したのでimportしていない
from decimal import Decimal, ROUND_HALF_UP, ROUND_HALF_EVEN, ROUND_UP, ROUND_DOWN # 左のROUND_HALF_UPから四捨五入、四捨五入(銀行丸め)、切り上げ、切り捨て
#  SortedDictはlistやsetの値を持てる、peekitem(bisect_left(1))のイメージで1に近いキーの値を取得可能
from sortedcontainers import SortedSet, SortedList, SortedDict
from collections import defaultdict, deque, Counter
from atcoder.dsu import DSU
#  使用例：SegTree(定義した関数, 単位元, 対象のリスト) ※詳細：https://atcoder.github.io/ac-library/production/document_ja/segtree.html?utm_source=chatgpt.com
from atcoder.segtree import SegTree # 単位元→和：0、乗算：1、最大：-float('INF'), 最小：float('INF')、GCD：0、LCM：1、OR：0、XOR：0、AND：(1<<60)-1(bit数が不足していれば増やす)
from atcoder.lazysegtree import LazySegTree
sys.setrecursionlimit(10**7)

N, K = map(int, input().split()) # 取得例：1 2

res_list = [0] * N
for _ in range(K):
    d = int(input())
    A_list = list(map(int, input().split()))
    for a in A_list:
        res_list[a-1] += 1

print(res_list.count(0))