import sys, math, itertools, bisect, functools, copy, decimal
from more_itertools import distinct_permutations
from functools import cmp_to_key
# 天井と床関数は丸める仕様らしく、桁数が上がると期待通りの動作をしないことを確認したのでimportしていない
from decimal import Decimal, ROUND_HALF_UP, ROUND_HALF_EVEN, ROUND_UP, ROUND_DOWN # 左のROUND_HALF_UPから四捨五入、四捨五入(銀行丸め)、切り上げ、切り捨て
from sortedcontainers import SortedSet, SortedList, SortedDict
from collections import defaultdict, Counter, deque
from atcoder.dsu import DSU
sys.setrecursionlimit(10**7)

N = int(input())
A_list = list(map(int, input().split())) # 取得例：[1, 2, 3]、1行の入力用

n_c = Counter(A_list)
res = 0
# Ak*Aj=Aiとして考える
# AkとAjの数値を選択(重複あり)
for i in range(1, 2*10**5+1):
    for j in range(1, 2*10**5//i+1):
        if i in n_c and j in n_c and i*j in n_c:
            # 仮に「2 2 4」という数列でAk=2、Aj=2を選択
            # そうするとAk(2)の選び方は2通り、Aj(2)も2通り、Ak*Aj=4は1通りなので合計2*2*1=4通り
            # Ak=(1, 2)、Aj=(1, 2)であるので1→1,2、2→1, 2なのでこれで2*2=4通り
            res += n_c[i]*n_c[j]*n_c[i*j]

print(res)