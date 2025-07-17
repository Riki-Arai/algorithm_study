N, M = map(int, input().split())
A_list = list(map(int, input().split())) # 取得例：[1, 2, 3]、1行の入力用

a_idx = 0
for i in range(1, N+1):
    if A_list[a_idx] - i == 0:
        a_idx += 1
        print(0)
    else:
        print(A_list[a_idx] - i)

## 以下はfirst
#import math, itertools, bisect, functools, copy, decimal
## 天井と床関数は丸める仕様らしく、桁数が上がると期待通りの動作をしないことを確認したのでimportしていない
#from decimal import Decimal, ROUND_HALF_UP, ROUND_HALF_EVEN, ROUND_UP, ROUND_DOWN # 左のROUND_HALF_UPから四捨五入、四捨五入(銀行丸め)、切り上げ、切り捨て
#from collections import defaultdict, Counter, deque
#
#N, M = map(int, input().split())
#A_list = list(map(int, input().split())) # 取得例：[1, 2, 3]、1行の入力用
#
#for i in range(1, N+1):
#    idx = bisect.bisect_left(A_list, i)
#    print(A_list[idx]-i)