# 入力
N=int(input())
L=set()
for _ in range(N):
    L.add(input())
print(len(L))

## first
#import math, itertools, bisect, functools, copy
#from collections import defaultdict, Counter, deque
## 天井と床関数は丸める仕様らしく、桁数が上がると期待通りの動作をしないことを確認したのでimportしていない
#from decimal import Decimal, ROUND_HALF_UP, ROUND_UP, ROUND_DOWN # 左のROUND_HALF_UPから四捨五入、続いて切り上げ、切り捨て
#
#N = int(input())
#A_lists = [list(map(int, input().split())) for _ in range(N)] # 取得例:[[1,2], [3,4]・・[9,10]]
#
#res_dic = defaultdict(int)
#for A_list in A_lists:
#    res_list = []
#    for a in A_list[:1]:
#        res_list.append(a)
#    res_dic[tuple(A_list)] = 1
#
#print(len(res_dic.keys()))