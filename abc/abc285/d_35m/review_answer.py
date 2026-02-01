### 別解
# サイクル性があること、またlocalとglobalのsetを用意することがポイント
import sys
from collections import defaultdict
sys.setrecursionlimit(10**7)

N = int(input().strip())

g_dict = defaultdict(str)
for _ in range(N):
    s, t = input().split()
    g_dict[s] = t

seen_set = set()
def dfs(s):
    if s in local_set:
        print("No")
        exit()
    seen_set.add(s)
    local_set.add(s)
    if s in g_dict:
        dfs(g_dict[s])

for k in g_dict.keys():
    if k not in seen_set:
        local_set = set()
        dfs(k)

print("Yes")

#import sys, math, itertools, bisect, functools, copy, decimal
#from more_itertools import distinct_permutations
#from functools import cmp_to_key
## 天井と床関数は丸める仕様らしく、桁数が上がると期待通りの動作をしないことを確認したのでimportしていない
#from decimal import Decimal, ROUND_HALF_UP, ROUND_HALF_EVEN, ROUND_UP, ROUND_DOWN # 左のROUND_HALF_UPから四捨五入、四捨五入(銀行丸め)、切り上げ、切り捨て
#from sortedcontainers import SortedSet, SortedList, SortedDict
#from collections import defaultdict, Counter, deque
#from atcoder.dsu import DSU
#sys.setrecursionlimit(10**7)
#
#N = int(input().strip())
#S = []
#T = []
#for _ in range(N):
#    s, t = input().split()
#    S.append(s)
#    T.append(t)
#
#id_of_S = {s: i for i, s in enumerate(S)}
#dsu = DSU(N)
#for s, t in zip(S, T):
#    if s == t:
#        continue
#    if t in id_of_S:
#        u = id_of_S[s]
#        v = id_of_S[t]
#        # merge してみて、もしすでに同じ根だったらサイクル → 不可能
#        if dsu.same(u, v):
#            print("No")
#            exit()
#        dsu.merge(u, v)
#
#print("Yes")