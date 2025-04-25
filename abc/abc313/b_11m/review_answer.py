N, B = map(int, input().split())
A_lists = [list(map(int, input().split())) for _ in range(B)]

st = set(range(1, N + 1))
# A_lists の各 (a, b_val) について st から b_val を削除 (存在しなければ無視)
for a, b_val in A_lists:
    st.discard(b_val)

if len(st) >= 2:
    print(-1)
else:
    print(next(iter(st)))

#import math, itertools, bisect, functools, copy
#from collections import defaultdict, Counter, deque
## 天井と床関数は丸める仕様らしく、桁数が上がると期待通りの動作をしないことを確認したのでimportしていない
#from decimal import Decimal, ROUND_HALF_UP, ROUND_UP, ROUND_DOWN # 左のROUND_HALF_UPから四捨五入、続いて切り上げ、切り捨て
#
#N, B = map(int, input().split())
#A_lists = [list(map(int, input().split())) for _ in range(B)] # 取得例:[[1,2], [3,4]・・[9,10]]
#
#res_dic = defaultdict(int)
#for A_list in A_lists:
#    a, b = A_list[0], A_list[1]
#    res_dic[b] = a
#
#res_list = []
#n_list = [i for i in range(1, N+1)]
#for n in n_list:
#    while True:
#        if n in res_dic:
#            n = res_dic[n]
#        else:
#            res_list.append(n)
#            break
#
#if len(set(res_list)) == 1:
#    print(res_list[0])
#else:
#    print(-1)