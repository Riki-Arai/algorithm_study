import sys, math, itertools, bisect, functools, copy, decimal
# 天井と床関数は丸める仕様らしく、桁数が上がると期待通りの動作をしないことを確認したのでimportしていない
from decimal import Decimal, ROUND_HALF_UP, ROUND_HALF_EVEN, ROUND_UP, ROUND_DOWN # 左のROUND_HALF_UPから四捨五入、四捨五入(銀行丸め)、切り上げ、切り捨て
from collections import defaultdict, Counter, deque
from atcoder.dsu import DSU
sys.setrecursionlimit(10**7)

N = int(input())
A_list = list(map(int, input().split())) # 取得例：[1, 2, 3]、1行の入力用

res_dict = defaultdict(int)
s_a_list = list(set(A_list))
s_a_list.sort()
for i, a in enumerate(s_a_list, 1):
    res_dict[a] = len(s_a_list) - i

res_list = [0] * N
for a in A_list:
    res_list[res_dict[a]] += 1

print(*res_list, sep='\n')