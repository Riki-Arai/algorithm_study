import math

T = int(input())

for _ in range(T):
    N, D, K = map(int, input().split())
    K -= 1
    g = math.gcd(N, D)
    d = D//g
    n = N//g
    print((d*K)%n*g+K//n)


import sys, math, itertools, bisect, functools, copy, decimal
from more_itertools import distinct_permutations
from functools import cmp_to_key
# 天井と床関数は丸める仕様らしく、桁数が上がると期待通りの動作をしないことを確認したのでimportしていない
from decimal import Decimal, ROUND_HALF_UP, ROUND_HALF_EVEN, ROUND_UP, ROUND_DOWN # 左のROUND_HALF_UPから四捨五入、四捨五入(銀行丸め)、切り上げ、切り捨て
from sortedcontainers import SortedSet, SortedList, SortedDict
from collections import defaultdict, Counter, deque
from atcoder.dsu import DSU
sys.setrecursionlimit(10**7)

T = int(input())
for i in range(T):
    n, d, k = map(int, sys.stdin.readline().split())
    k -= 1
    # 今回の問題ではd、2*d、3*d・・・とnのmodをとることから、最大公約数を求める方向で解いていく
    # 最大公約数を倍数としたいずれかの値を導出できる
    g = math.gcd(n, d)
    # 巡回できるようにブロックに分ける
    m = n // g
    # ブロックに分けた世界のdに変換
    # dが1プラスするごとにmが1プラスされるイメージ
    e = d // g
    # 変換したe個に対してk回移動し、%mをすることでmブロックのうちのどこにいるかを導出
    b = (e * k) % m
    # mブロックを1周するたびに着地点が右に1個ずれる
    i = k // m
    # 復元
    ans = b * g + i
    print(ans)