import sys, math, itertools, bisect, functools, copy, decimal
# 天井と床関数は丸める仕様らしく、桁数が上がると期待通りの動作をしないことを確認したのでimportしていない
from decimal import Decimal, ROUND_HALF_UP, ROUND_HALF_EVEN, ROUND_UP, ROUND_DOWN # 左のROUND_HALF_UPから四捨五入、四捨五入(銀行丸め)、切り上げ、切り捨て
from collections import defaultdict, Counter, deque
from atcoder.dsu import DSU
sys.setrecursionlimit(10**7)

N = int(input())
A_list = list(map(int, input().split())) # 取得例：[1, 2, 3]、1行の入力用

res = 0
pair_count = 0
for i, a in enumerate(A_list, 1):
    if i == a:
        pair_count += 1

# 単調増加のリストから2つの組み合わせ数を求める
res += math.comb(pair_count, 2)
count = 0
for i in range(N):
    # 入力1の「1 3 2 4」でいえば「3 2」のような箇所をカウント
    if A_list[i] != i+1 and A_list[A_list[i]-1] == i+1:
        count += 1

#　counttについては2重になっているので2で割る
print(res + count//2)