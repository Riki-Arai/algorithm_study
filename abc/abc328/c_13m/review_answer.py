# (1) [0, 0, 1, 0, 0, 1, 0, ・・・]のように連続文字列の出現箇所を記録
# (2) [0, 0, 0, 1, 1, 1, 2, ・・・]のように出現した時点で累積する形で記録
# 累積和を作る際には(2)のリストも参照する点に注意
N, Q = map(int, input().split())
S = input().strip()

# 隣接する文字の一致を記録
# a[i] = 1 ⇔ S[i] == S[i+1], 0-based
a = [0] * (N - 1)
for i in range(N - 1):
    if S[i] == S[i + 1]:
        a[i] = 1

# 累積和 b
# b[i] = a[0] + a[1] + ... + a[i-1]（b[0] = 0）
b = [0] * N
for i in range(1, N):
    b[i] = b[i - 1] + a[i - 1]

for _ in range(Q):
    l, r = map(int, input().split())
    l -= 1
    r -= 1
    print(b[r] - b[l])

# first
#import math, itertools, bisect, functools, copy, decimal
## 天井と床関数は丸める仕様らしく、桁数が上がると期待通りの動作をしないことを確認したのでimportしていない
#from decimal import Decimal, ROUND_HALF_UP, ROUND_HALF_EVEN, ROUND_UP, ROUND_DOWN # 左のROUND_HALF_UPから四捨五入、四捨五入(銀行丸め)、切り上げ、切り捨て
#from collections import defaultdict, Counter, deque
#
#N, Q = map(int, input().split())
#S = input().strip()
#
#idx_list = []
#for i in range(1, N):
#    if S[i-1] == S[i]:
#        idx_list.append(i+1)
#
#s_l = len(S)
#for _ in range(Q):
#    l, r = map(int, input().split())
#    l_idx = bisect.bisect_right(idx_list, l)
#    r_idx = bisect.bisect_right(idx_list, r)
#    print(r_idx-l_idx)