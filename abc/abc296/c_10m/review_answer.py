N, X = map(int, input().split())
A = list(map(int, input().split()))

S = set(A)
for val in A:
    if (val - X) in S:
        print("Yes")
        break
else:
    print("No")

## これは数分以内に解くべき問題
## bisectの仕様を正しく把握できていないところがあったことも原因だったので見直しておいた
## あとidxを導出するところを値の導出だと勘違いしていたことも手間取った原因かも
## ただ典型的な問題なので慣れることで数分内で解けるようには全然いけそう
#import math, itertools, bisect, functools, copy, decimal
## 天井と床関数は丸める仕様らしく、桁数が上がると期待通りの動作をしないことを確認したのでimportしていない
#from decimal import Decimal, ROUND_HALF_UP, ROUND_HALF_EVEN, ROUND_UP, ROUND_DOWN # 左のROUND_HALF_UPから四捨五入、四捨五入(銀行丸め)、切り上げ、切り捨て
#from collections import defaultdict, Counter, deque
#
#N, X = map(int, input().split())
#A_list = list(map(int, input().split())) # 取得例：[1, 2, 3]、1行の入力用
#
#A_list.sort()
#for i in range(N):
#    ai = A_list[i]
#    j = bisect.bisect_left(A_list, ai+X)
#    if j >= 0 and j < N and A_list[j] - ai == X:
#        print("Yes")
#        exit()
#
#print("No")