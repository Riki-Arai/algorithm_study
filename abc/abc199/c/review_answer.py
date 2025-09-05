# 入力
N=int(input())
S=list(input())
Q=int(input())

# 前半と後半に分ける
S1=S[:N]
S2=S[N:]

# クエリをQ回処理する
for _ in range(Q):
  T,A,B=map(int,input().split())
  # 0-indexedにする
  A-=1
  B-=1
  # A,Bが前半、後半に含まれるか場合分けして入れ替える
  if T==1:
    if B<N:
      S1[A],S1[B]=S1[B],S1[A]
    elif A<N<=B:
      S1[A],S2[B-N]=S2[B-N],S1[A]
    else:
      S2[A-N],S2[B-N]=S2[B-N],S2[A-N]
  # 前半と後半を入れ替える
  elif T==2:
    S1,S2=S2,S1

# 前半と後半をつながて出力
print(''.join(S1+S2))


## ほぼ解けていたのにもったない
## スワップ処理をした際に思わぬ上書きがあったので混乱したが、本来は別の文字列を書き換えることはないので、方針よりもバグを疑うべきだった
#import sys, math, itertools, bisect, functools, copy, decimal
#from functools import cmp_to_key
## 天井と床関数は丸める仕様らしく、桁数が上がると期待通りの動作をしないことを確認したのでimportしていない
#from decimal import Decimal, ROUND_HALF_UP, ROUND_HALF_EVEN, ROUND_UP, ROUND_DOWN # 左のROUND_HALF_UPから四捨五入、四捨五入(銀行丸め)、切り上げ、切り捨て
#from sortedcontainers import SortedSet, SortedList, SortedDict
#from collections import defaultdict, Counter, deque
#from atcoder.dsu import DSU
#sys.setrecursionlimit(10**7)
#
#N = int(input()) # 数値
#S = input().strip() # 文字列
#Q = int(input()) # 数値
#
#res_list = []
#res_dict = defaultdict(str)
#for i, s in enumerate(S, 1):
#    res_dict[i] = s
#    res_list.append(s)
#
#c = 0
#for _ in range(Q):
#    T, A, B = map(int, input().split())
#    if T == 1:
#        if c == 1:
#            if A >= N:
#                A -= N
#            else:
#                A += N
#            if B >= N:
#                B -= N
#            else:
#                B += N
#            res_list[A-1], res_list[B-1] = res_list[B-1], res_list[A-1]
#        else:
#            res_list[A-1], res_list[B-1] = res_list[B-1], res_list[A-1]
#    else:
#        if c == 0:
#            c = 1
#        else:
#            c = 0
#
#if c == 1:
#    print("".join(res_list[N:] + res_list[:N]))
#else:
#    print("".join(res_list))