import math

P = int(input())

ans = 0
for i in range(10, 0, -1):
    coin = math.factorial(i)
    while(P >= coin):
        P -= coin
        ans += 1
print(ans)


## first
#import math, itertools, bisect, functools, copy
#from collections import defaultdict, Counter, deque
## 天井と床関数は丸める仕様らしく、桁数が上がると期待通りの動作をしないことを確認したのでimportしていない
#from decimal import Decimal, ROUND_HALF_UP, ROUND_UP, ROUND_DOWN # 左のROUND_HALF_UPから四捨五入、続いて切り上げ、切り捨て
#
#P = int(input())
#
#res = 0
#while P > 0:
#    for n in range(10, 0, -1):
#        i = math.factorial(n)
#        while True:
#            if P >= i:
#                P -= i
#                res += 1
#            else:
#                break
#
#print(res)