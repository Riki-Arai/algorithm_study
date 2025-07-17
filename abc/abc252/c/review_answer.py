# 重複がある場合は+10秒など1通りのことは気づけたが、maxをとってそのあとにminをとる処理に気づけなかった
# 知識が不要なタイプの問題だったのでこれは解きたかったところ
# WAのコードのようにやはりナイーブに条件を加えるようなコードを書いている時点で大体うまくいなかない
N = int(input())
S_list = [input() for _ in range(N)]

res = float("INF")
for i in range(10):
    tmp_res = 0
    n_list = [0] * 10
    for s in S_list:
        n_list[s.index(str(i))] += 1
    for i, n in enumerate(n_list):
        # 仮に1回転のみであれば一番右にあるidxがresとなる
        if n == 1:
            tmp_res = max(i, tmp_res)
        # 2回転以上の場合は10秒*n+idxとなる
        elif n > 1:
            tmp_res = max((n-1)*10+i, tmp_res)

    res = min(tmp_res, res)

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