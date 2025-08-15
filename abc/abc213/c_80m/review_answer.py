# 座標圧縮と呼ばれる技術
# 何も知らないのと知っているのでだいぶ実装が違うので、やはり解法を理解・覚えることが大事
H, W, N = map(int,input().split())

X, Y = [], []
for i in range(N):
    x,y = map(int,input().split())
    X.append(x)
    Y.append(y)

Xdict = {x:i for i, x in enumerate(sorted(list(set(X))), 1)}
Ydict = {y:i for i, y in enumerate(sorted(list(set(Y))), 1)}

for i in range(N):
    print(Xdict[X[i]], Ydict[Y[i]])


#import sys, math, itertools, bisect, functools, copy, decimal
#from functools import cmp_to_key
## 天井と床関数は丸める仕様らしく、桁数が上がると期待通りの動作をしないことを確認したのでimportしていない
#from decimal import Decimal, ROUND_HALF_UP, ROUND_HALF_EVEN, ROUND_UP, ROUND_DOWN # 左のROUND_HALF_UPから四捨五入、四捨五入(銀行丸め)、切り上げ、切り捨て
#from sortedcontainers import SortedSet, SortedList, SortedDict
#from collections import defaultdict, Counter, deque
#from atcoder.dsu import DSU
#sys.setrecursionlimit(10**7)
#
#H, W, N = map(int, input().split())
#A_lists = []
#for i in range(N):
#    tmp_list = list(map(int, input().split()))
#    tmp_list.append(i)
#    A_lists.append(tmp_list)
#
#min_w, min_h = float("INF"), float("INF")
#for h, w, _ in A_lists:
#    min_h = min(h-1, min_h)
#    min_w = min(w-1, min_w)
#
#s_a_lists = sorted(A_lists, key=lambda x: x[0])
#split_h_dict = defaultdict()
#split_h = 0
#for i in range(N-1):
#    f_h = s_a_lists[i][0]
#    s_h = s_a_lists[i+1][0]
#    if f_h + 1 < s_h:
#        split_h += s_h - f_h - 1
#        split_h_dict[s_h] = split_h
#    else:
#        split_h_dict[s_h] = split_h
#
#s_a_lists = sorted(A_lists, key=lambda x: x[1])
#split_w_dict = defaultdict()
#split_w = 0
#for i in range(N-1):
#    f_w = s_a_lists[i][1]
#    s_w = s_a_lists[i+1][1]
#    if f_w + 1 < s_w:
#        split_w += s_w - f_w - 1
#        split_w_dict[s_w] = split_w
#    else:
#        split_w_dict[s_w] = split_w
#
#res_lists = [None] * N
#for h, w, i in s_a_lists:
#    if h in split_h_dict:
#        h -= split_h_dict[h]
#    if w in split_w_dict:
#        w -= split_w_dict[w]
#    res_lists[i] = (h-min_h, w-min_w)
#
#for h, w in res_lists:
#    print(h, w)