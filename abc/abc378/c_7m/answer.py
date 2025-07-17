import math, itertools, bisect, functools, copy
from collections import defaultdict, Counter, deque
# 天井と床関数は丸める仕様らしく、桁数が上がると期待通りの動作をしないことを確認したのでimportしていない
from decimal import Decimal, ROUND_HALF_UP, ROUND_UP, ROUND_DOWN # 左のROUND_HALF_UPから四捨五入、続いて切り上げ、切り捨て

N = int(input())
A_list = list(map(int, input().split())) # 取得例：[1, 2, 3]、1行の入力用

res_list = []
res_dic =defaultdict(list)
for i, a in enumerate(A_list, 1):
    if a in res_dic:
        res_list.append(res_dic[a].pop(0))
        res_dic[a].append(i)
    else:
        res_dic[a].append(i)
        res_list.append(-1)

print(*res_list)