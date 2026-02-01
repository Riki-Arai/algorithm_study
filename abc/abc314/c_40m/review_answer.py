import sys, math, itertools as it, bisect as bi, functools as ft, copy, decimal, heapq as hq
from more_itertools import distinct_permutations
from functools import cmp_to_key
# 天井と床関数は丸める仕様らしく、桁数が上がると期待通りの動作をしないことを確認したのでimportしていない
from decimal import Decimal, ROUND_HALF_UP, ROUND_HALF_EVEN, ROUND_UP, ROUND_DOWN # 左のROUND_HALF_UPから四捨五入、四捨五入(銀行丸め)、切り上げ、切り捨て
from sortedcontainers import SortedSet, SortedList, SortedDict
from collections import defaultdict, Counter, deque
from atcoder.dsu import DSU
sys.setrecursionlimit(10**7)

N, M = map(int, input().split())
S = input().strip()
C_list = list(map(int, input().split()))

tmp_dict = defaultdict(deque)
for i in range(N):
    tmp_dict[int(C_list[i])].append(S[i])

res_dict = defaultdict(deque)
for k, v in tmp_dict.items():
    first_v = v.pop()
    v.appendleft(first_v)
    res_dict[k] = v

res_list = []
for i in range(N):
    res_list.append(res_dict[C_list[i]].popleft())

print("".join(res_list))

# 以下は2回目に解答したもの（模範解答よりもコードが短い）
#N, M = map(int, input().split())
#S = input().strip()
#C_list = list(map(int, input().split()))
#
#idx_lists = [[] for _ in range(M)]
#for i, c in enumerate(C_list):
#    idx_lists[c-1].append(i)
#
#s_list = list(S)
#res_list = [""] * N
#for idx_list in idx_lists:
#    for i in range(len(idx_list)):
#        res_list[idx_list[(i+1)%len(idx_list)]] = s_list[idx_list[i]]
#
#print("".join(res_list))

#N, M = map(int, input().split())
#S = input().strip()
#C_list = list(map(int, input().split())) # 取得例：[1, 2, 3]、1行の入力用
#
#alp_lists = [[] for _ in range(M)]
#idx_lists = [[] for _ in range(M)]
#for j, c in enumerate(C_list):
#    alp_lists[c-1].append(S[j])
#    idx_lists[c-1].append(j)
#
#res_dict = {}
#for i in range(M):
#    alp_list = alp_lists[i]
#    idx_list = idx_lists[i]
#    for k in range(1, len(alp_list)+1):
#        res_dict[idx_list[k%len(idx_list)]] = alp_list[k-1]
#
#res_list = []
#for i in range(N):
#    res_list.append(res_dict[i])
#
#print("".join(res_list))