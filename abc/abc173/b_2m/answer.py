import math, itertools, bisect, functools, copy
from collections import defaultdict, Counter, deque
# 天井と床関数は丸める仕様らしく、桁数が上がると期待通りの動作をしないことを確認したのでimportしていない
from decimal import Decimal, ROUND_HALF_UP, ROUND_UP, ROUND_DOWN # 左のROUND_HALF_UPから四捨五入、続いて切り上げ、切り捨て

N = int(input()) # 取得例：1
A_list = [input() for _ in range(N)] # 取得例：[A1,A2・・・An]、N行の入力用

res_dic = defaultdict(int)
for a in A_list:
    res_dic[a] += 1

for s in ["AC", "WA", "TLE", "RE"]:
    if s in res_dic:
        print(f"{s} x {res_dic[s]}")
    else:
        print(f"{s} x 0")