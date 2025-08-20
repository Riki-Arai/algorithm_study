# 尺取り法でも解けるようだが、dqとdictを組み合わせた方法でも解ける
import sys, math, itertools, bisect, functools, copy, decimal
from functools import cmp_to_key
# 天井と床関数は丸める仕様らしく、桁数が上がると期待通りの動作をしないことを確認したのでimportしていない
from decimal import Decimal, ROUND_HALF_UP, ROUND_HALF_EVEN, ROUND_UP, ROUND_DOWN # 左のROUND_HALF_UPから四捨五入、四捨五入(銀行丸め)、切り上げ、切り捨て
from sortedcontainers import SortedSet, SortedList, SortedDict
from collections import defaultdict, Counter, deque
from atcoder.dsu import DSU
sys.setrecursionlimit(10**7)

N, K = map(int, input().split())
A_list = list(map(int, input().split())) # 取得例：[1, 2, 3]、1行の入力用

dq = deque()
res_dict = defaultdict(int)
for i in range(K):
    res_dict[A_list[i]] += 1
    dq.append(A_list[i])

res = len(res_dict.keys())
for i in range(K, N):
    dq.append(A_list[i])
    res_dict[A_list[i]] += 1
    pop_a = dq.popleft()
    if res_dict[pop_a] - 1 == 0:
        del res_dict[pop_a]
        res = max(len(res_dict.keys()), res)
    else:
        res_dict[pop_a] -= 1
        res = max(len(res_dict.keys()), res)

print(res)


## 尺取り法
#import math, itertools, bisect, functools, copy, decimal
## 天井と床関数は丸める仕様らしく、桁数が上がると期待通りの動作をしないことを確認したのでimportしていない
#from decimal import Decimal, ROUND_HALF_UP, ROUND_HALF_EVEN, ROUND_UP, ROUND_DOWN # 左のROUND_HALF_UPから四捨五入、四捨五入(銀行丸め)、切り上げ、切り捨て
#from collections import defaultdict, Counter, deque
#
#N, K = map(int, input().split())
#C_list = list(map(int, input().split())) # 取得例：[1, 2, 3]、1行の入力用
#
#res = 0
#res_dict = defaultdict(int)
#res_set = set()
#dq = deque()
#for i in range(N):
#    dq.append(C_list[i])
#    res_set.add(C_list[i])
#    res_dict[C_list[i]] += 1
#    while len(dq) and len(dq) > K:
#        l = dq.popleft()
#        res_dict[l] -= 1
#        if res_dict[l] == 0:
#            res_set.discard(l)
#
#    res = max(len(res_set), res)
#
#print(res)