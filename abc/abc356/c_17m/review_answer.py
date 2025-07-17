# ビット探索を用いてテストパターンごとに使える鍵を先に数え上げてあげる
# 数え上げたら矛盾がないかどうかをチェック

from itertools import product

N, M, K = map(int, input().split())
A_lists = [input().split() for _ in range(M)]

res = 0
for pattern in product([0, 1], repeat=N):
    ok = True
    for test in A_lists:
        R_i = test[-1]
        keys = map(int, test[1:-1])
        # ビットで候補を挙げた物の中でも、keysとして列挙されたものでoのものをカウント
        used_count = sum(pattern[k - 1] for k in keys)

        if R_i == 'o':
            if used_count < K:
                ok = False
                break
        else:
            if used_count >= K:
                ok = False
                break

    if ok:
        res += 1

print(res)

#import math, itertools, bisect, functools, copy, decimal
## 天井と床関数は丸める仕様らしく、桁数が上がると期待通りの動作をしないことを確認したのでimportしていない
#from decimal import Decimal, ROUND_HALF_UP, ROUND_HALF_EVEN, ROUND_UP, ROUND_DOWN # 左のROUND_HALF_UPから四捨五入、四捨五入(銀行丸め)、切り上げ、切り捨て
#from collections import defaultdict, Counter, deque
#
#N, M, K = map(int, input().split())
#A_lists = [list(input().split()) for _ in range(M)]
#
#res = 0
#p_lists = list(itertools.product([0, 1], repeat=N))
#for p_list in p_lists:
#    key_list = [False] * N
#    res_flag = True
#    for i, p in enumerate(p_list):
#        if p == 1:
#            key_list[i] = True
#
#    for A_list in A_lists:
#        r = A_list[-1]
#        count = 0
#        if r == "o":
#            for a in A_list[1:-1]:
#                if key_list[int(a)-1]:
#                    count += 1
#            if count < K:
#                res_flag = False
#        else:
#            for a in A_list[1:-1]:
#                if key_list[int(a)-1]:
#                    count += 1
#            if count >= K:
#                res_flag = False
#
#    if res_flag:
#        res += 1
#
#print(res)