# この問題は尺取法でも解けるようだが、個人的には自分の回答の方がスマートなので尺取法は参考程度にしておく

import math, itertools, bisect, functools, copy
from collections import defaultdict, Counter, deque
# 天井と床関数は丸める仕様らしく、桁数が上がると期待通りの動作をしないことを確認したのでimportしていない
from decimal import Decimal, ROUND_HALF_UP, ROUND_UP, ROUND_DOWN # 左のROUND_HALF_UPから四捨五入、続いて切り上げ、切り捨て

N = int(input())
A_list = list(map(int, input().split())) # 取得例：[1, 2, 3]、1行の入力用

res = float("INF")
res_dic = defaultdict(int)
for i, a in enumerate(A_list):
    if a in res_dic:
        res = min((i - res_dic[a] + 1), res)
        res_dic[a] = i
    else:
        res_dic[a] = i

if res == float("INF"):
    print(-1)
else:
    print(res)


# 尺取法による回答
#from collections import defaultdict
#
#N = int(input())
#A_list = list(map(int, input().split()))
#
#count = defaultdict(int)
#r = 0
#ans = float('inf')
#dup_found = False
#
#for l in range(N):
#    # 重複が見つからない限り、右端をなるべく伸ばす
#    while r < N and not dup_found:
#        count[A_list[r]] += 1
#        if count[A_list[r]] == 2:
#            dup_found = True
#        r += 1
#    # 重複を見つけられないまま r が尽きれば以降は無理
#    if not dup_found:
#        break
#    # [l, r-1] の長さが重複あり区間
#    ans = min(ans, r - l)
#
#    # 左端要素を除去。もしそれが重複要素だったなら重複フラグを解除
#    if count[A_list[l]] == 2:
#        dup_found = False
#    count[A_list[l]] -= 1
#
#print(ans if ans != float('inf') else -1)