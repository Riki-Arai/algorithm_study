# サブマスクの経験がなかったのができなかったことが原因
import sys, math, itertools, bisect, functools, copy, decimal
# 天井と床関数は丸める仕様らしく、桁数が上がると期待通りの動作をしないことを確認したのでimportしていない
from decimal import Decimal, ROUND_HALF_UP, ROUND_HALF_EVEN, ROUND_UP, ROUND_DOWN # 左のROUND_HALF_UPから四捨五入、四捨五入(銀行丸め)、切り上げ、切り捨て
from sortedcontainers import SortedSet, SortedList, SortedDict
from collections import defaultdict, Counter, deque
from atcoder.dsu import DSU
sys.setrecursionlimit(10**7)

N = int(input())

n_b = str(bin(N)[2:])
one_idx_list = []
# 最大で15桁でも単純な全探索では厳しいので、あらかじめ1のフラグが立っているidxのみを抽出
for i in range(len(n_b)):
    if int(n_b[i]):
        one_idx_list.append(i)

def convert_base(num_str: str, from_base: int, to_base: int) -> str:
    decimal_value = int(num_str, from_base)
    digits = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    if decimal_value == 0:
        return "0"
    result = ""
    while decimal_value > 0:
        remainder = decimal_value % to_base
        result = digits[remainder] + result
        decimal_value //= to_base
    return result

# 1のフラグが立っているidxを抽出するかどうかの2択だと考えてbit全探索をしてしまえば良い
res_list = []
p_lists = list(itertools.product([0, 1], repeat=len(one_idx_list)))
for p_list in p_lists:
    bit_list = ["0"]*len(n_b)
    for i, p in enumerate(p_list):
        if p == 1:
            bit_list[one_idx_list[i]] = "1"

    res_list.append(convert_base("".join(bit_list), 2, 10))

for res in res_list:
    print(res)