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

bit_dict = defaultdict(int)
# ややこしいかもしれないが、1<<0とは別物でこちらは偶奇のパターンをカウントするための0なので注意
# 0=0000000000だだdだtだと思えばいい
# r=0の時点では何も出現していないので0の状態で1カウント
bit_dict[0] += 1
bit = 0
for s in S:
    # 1 << 0の場合だと1となるが、0が1回出現したとみなせる
    bit = bit ^ 1 << int(s)
    bit_dict[bit] += 1

res = 0
# 同じパターン同士でないと
for count in bit_dict.values():
    # 例えば01であれば2が奇数回出ており、3-1=2となり偶数回になるため条件を満たす
    # 偶数回出ていた場合でも4-2=2などで偶数回になるのでやはり条件を満たす
    # 同じ数字が出ている状態同士の組み合わせとなるので下記の計算となる
    # 2個選ぶ = lとrを選択していると解釈できる
    res += count * (count - 1) // 2

print(res)