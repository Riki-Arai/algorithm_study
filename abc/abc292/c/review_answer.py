# ABとCDは同じペアを持つ、N//i+1なので計算量が重くならないといったことがポイント
import sys, math, itertools, bisect, functools, copy, decimal
from functools import cmp_to_key
# 天井と床関数は丸める仕様らしく、桁数が上がると期待通りの動作をしないことを確認したのでimportしていない
from decimal import Decimal, ROUND_HALF_UP, ROUND_HALF_EVEN, ROUND_UP, ROUND_DOWN # 左のROUND_HALF_UPから四捨五入、四捨五入(銀行丸め)、切り上げ、切り捨て
from sortedcontainers import SortedSet, SortedList, SortedDict
from collections import defaultdict, Counter, deque
from atcoder.dsu import DSU
sys.setrecursionlimit(10**7)

N = int(input())

res_dict = defaultdict(int)
res_lists = []
# こちらは+1がなくても良い
for i in range(1, N+1):
    # +1をしておかないとN//(N-1)のケースで1となってしまうので探索してくれない
    for j in range(1, N//i+1):
        # A~Dはいずれも1以上なのでi*j=Nの組み合わせは排除
        if i*j < N:
            res_lists.append((i, j))
            # ペア数を事前にカウント
            res_dict[i*j] += 1

res = 0
for i in range(len(res_lists)):
    a, b = res_lists[i]
    y = N - a*b
    res += res_dict[y]

print(res)


#N = int(input())
#
## num[v] := 「v を x*y として表せる組 (x,y) の個数」
## 1 <= x, y かつ x*y = v の組の数
#num = [0] * (N+1)
## 下記は調和級数の性質から O(N log N)である
#for x in range(1, N+1):
#    limit = N // x  # x*y <= N となる y の最大値
#    for y in range(1, limit+1):
#        num[x*y] += 1
#
#res = 0
## X+Y=NはN通りしかないのでrange(1, N+1)で探索
#for v in range(1, N+1):
#    # ABが2パターン、CDが3パターンあれば6パターンあることになるので、それをresに足していく
#    # AB=vとしたときにCDはN-vと表すことができる
#    res += num[v] * num[N - v]
#
#print(res)