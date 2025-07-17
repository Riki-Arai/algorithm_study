import sys, math, itertools, bisect, functools, copy, decimal
# 天井と床関数は丸める仕様らしく、桁数が上がると期待通りの動作をしないことを確認したのでimportしていない
from decimal import Decimal, ROUND_HALF_UP, ROUND_HALF_EVEN, ROUND_UP, ROUND_DOWN # 左のROUND_HALF_UPから四捨五入、四捨五入(銀行丸め)、切り上げ、切り捨て
from collections import defaultdict, Counter, deque
from atcoder.dsu import DSU
sys.setrecursionlimit(10**7)

N = int(input()) # 数値：1
S_list = [input() for _ in range(N)] # 取得例：["A","B"・・・"E"]、N行の入力用
M = int(input()) # 数値：1
T_list = [input() for _ in range(M)] # 取得例：["A","B"・・・"E"]、N行の入力用

res_dict = defaultdict(int)
for s in S_list:
    res_dict[s] += 1

for t in T_list:
    res_dict[t] -= 1

res_list = sorted(list(res_dict.values()), reverse=True)
print(max(res_list[0], 0))