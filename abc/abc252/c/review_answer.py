# 重複がある場合は+10秒など1通りのことは気づけたが、maxをとってそのあとにminをとる処理に気づけなかった
# 知識が不要なタイプの問題だったのでこれは解きたかったところ
# WAのコードのようにやはりナイーブに条件を加えるようなコードを書いている時点で大体うまくいなかない
from collections import Counter

N = int(input().strip())
S_list = [input().strip() for _ in range(N)]

res = float("INF")
n_lists = []
for i in range(10):
    tmp_list = []
    for s in S_list:
        tmp_list.append(s.index(str(i)))

    c_lists = sorted(Counter(tmp_list).items(), key=lambda x: [-x[1], -x[0]])
    if c_lists[0][1] >= 2:
        res = min(c_lists[0][0]+10*(c_lists[0][1]-1), res)
    else:
        res = min(c_lists[0][0], res)

print(res)


## first(WA)
#import sys, math, itertools, bisect, functools, copy, decimal
## 天井と床関数は丸める仕様らしく、桁数が上がると期待通りの動作をしないことを確認したのでimportしていない
#from decimal import Decimal, ROUND_HALF_UP, ROUND_HALF_EVEN, ROUND_UP, ROUND_DOWN # 左のROUND_HALF_UPから四捨五入、四捨五入(銀行丸め)、切り上げ、切り捨て
#from collections import defaultdict, Counter, deque
#from atcoder.dsu import DSU
#sys.setrecursionlimit(10**7)
#
#N = int(input())
#S_list = [input() for _ in range(N)] # 取得例：[A1、A2・・・An]、N行の入力用
#
#res_list = []
#min_idx = float("INF")
#for i in range(10):
#    tmp_list = []
#    tmp_idx = 0
#    for s in S_list:
#        s_idx = s.index(str(i))
#        tmp_list.append(s_idx)
#        tmp_idx = max(s_idx, tmp_idx)
#    if tmp_idx < min_idx and len(set(tmp_list)) > len(set(res_list)):
#        res_list = tmp_list.copy()
#        min_idx = tmp_idx
#
#if len(set(res_list)) == N:
#    print(max(res_list))
#else:
#    counter = Counter(res_list)
#    max_time = 0
#    for position, count in counter.items():
#        candidate_time = position + 10 * (count - 1)
#        max_time = max(max_time, candidate_time)
#    print(max_time)