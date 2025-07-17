# まずは電源は常に明かりがあるので、電源ではない点で最低でもどのくらいの距離が必要かを調べる
# 全探索をする際には電源については調べる必要がないので、ムシをするようにする
# 距離を計算し終えたら導出した距離の中で最大のものを選択すれば、すべての点が明かりを得ることができる

import math, itertools, bisect, functools, copy
from collections import defaultdict, Counter, deque
# 天井と床関数は丸める仕様らしく、桁数が上がると期待通りの動作をしないことを確認したのでimportしていない
from decimal import Decimal, ROUND_HALF_UP, ROUND_UP, ROUND_DOWN # 左のROUND_HALF_UPから四捨五入、続いて切り上げ、切り捨て

N, K = map(int, input().split())
A_list = list(map(int, input().split())) # 取得例：[1, 2, 3]、1行の入力用
B_lists = [list(map(int, input().split())) for _ in range(N)] # 取得例:[[1,2], [3,4]・・[9,10]

res_list = []
a_set = set(A_list)
for i, B_list in enumerate(B_lists, 1):
    if i in a_set:
        continue
    tmp_list = []
    for a in A_list:
        x, y = B_lists[a-1]
        xx, yy = B_lists[i-1]
        tmp_list.append(math.sqrt(pow(abs(x-xx), 2)+pow(abs(y-yy), 2)))
    if len(tmp_list) > 0:
        res_list.append(min(tmp_list))

print(max(res_list))


## first
#import math, itertools, bisect, functools, copy
#from collections import defaultdict, Counter, deque
#from decimal import Decimal, ROUND_HALF_UP, ROUND_UP, ROUND_DOWN # 左からROUND_HALF_UPが四捨五入、続いて切り上げ、切り捨て
#
#N, K = map(int, input().split())
#A_list = list(map(int, input().split())) # 取得例：[1, 2, 3]、1行の入力用
#B_lists = [list(map(int, input().split())) for _ in range(N)] # 取得例:[[1,2], [3,4]・・[9,10]]
#
#res = 0
#for i, B_list in enumerate(B_lists, 1):
#    tmp_res = float("INF")
#    x, y = B_list
#    for a in A_list:
#        if i == a:
#            tmp_res = float("INF")
#            break
#        else:
#            xx, yy = B_lists[a-1]
#            tmp_res = min(tmp_res, pow(abs(x-xx), 2) + pow(abs(y-yy), 2))
#
#    if tmp_res != float("INF"):
#        res = max(res, tmp_res)
#
#print(math.sqrt(res))