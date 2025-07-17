import math, itertools, bisect, functools, copy
from collections import defaultdict, Counter, deque
# 天井と床関数は丸める仕様らしく、桁数が上がると期待通りの動作をしないことを確認したのでimportしていない
from decimal import Decimal, ROUND_HALF_UP, ROUND_UP, ROUND_DOWN # 左のROUND_HALF_UPから四捨五入、続いて切り上げ、切り捨て

N, K = map(int, input().split()) # 取得例：1 2
P_list = list(map(int, input().split())) # 取得例：[1,2,3]、1行の入力用

P_list.sort()
print(sum(P_list[:K]))