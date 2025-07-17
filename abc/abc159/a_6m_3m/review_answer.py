N,M=map(int,input().split())
print(N*(N-1)//2+M*(M-1)//2)

## 解説
#N, M = map(int, input().split())
#
#balls = [0] * N + [1] * M
#
#ans = 0
#for j in range(N + M):
#    for i in range(j):
#        x = balls[i] + balls[j]
#        if x % 2 == 0:
#            ans += 1
#
#print(ans)


## first
#import math, itertools, bisect, functools, copy
#from collections import defaultdict, Counter, deque
## 天井と床関数は丸める仕様らしく、桁数が上がると期待通りの動作をしないことを確認したのでimportしていない
#from decimal import Decimal, ROUND_HALF_UP, ROUND_UP, ROUND_DOWN # 左のROUND_HALF_UPから四捨五入、続いて切り上げ、切り捨て
#
#N, M = map(int, input().split()) # 取得例：1 2
#
#a_list = [2] * N
#b_list = [1] * M
#n_list = a_list + b_list
#res = 0
#c_n_list = itertools.combinations(n_list, 2)
#for c in c_n_list:
#    if (c[0] + c[1]) % 2 == 0:
#        res += 1
#
#print(res)