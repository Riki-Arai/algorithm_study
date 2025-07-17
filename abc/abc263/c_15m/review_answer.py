# 母集団がすでに単調増加が成立しているのであれば組み合わせを選べば良いだけ
# productだと無駄な処理が走ってしまって10^10の計算量になってしまう
import sys, math, itertools, bisect, functools, copy, decimal
# 天井と床関数は丸める仕様らしく、桁数が上がると期待通りの動作をしないことを確認したのでimportしていない
from decimal import Decimal, ROUND_HALF_UP, ROUND_HALF_EVEN, ROUND_UP, ROUND_DOWN # 左のROUND_HALF_UPから四捨五入、四捨五入(銀行丸め)、切り上げ、切り捨て
from collections import defaultdict, Counter, deque
from atcoder.dsu import DSU

N, M = map(int, input().split())

n_list = [i for i in range(1, M+1)]
for p in itertools.combinations(n_list, N):
    print(*list(p))