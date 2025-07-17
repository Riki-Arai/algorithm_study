# DSUを利用すると実装が楽
import sys, math, itertools, bisect, functools, copy, decimal
# 天井と床関数は丸める仕様らしく、桁数が上がると期待通りの動作をしないことを確認したのでimportしていない
from decimal import Decimal, ROUND_HALF_UP, ROUND_HALF_EVEN, ROUND_UP, ROUND_DOWN # 左のROUND_HALF_UPから四捨五入、四捨五入(銀行丸め)、切り上げ、切り捨て
from collections import defaultdict, Counter, deque
from atcoder.dsu import DSU
sys.setrecursionlimit(10**7)


N, M = map(int, input().split())

dsu = DSU(N)
for _ in range(M):
    u, v = map(int, input().split())
    dsu.merge(u-1, v-1)

print(len(list(dsu.groups())))


### DFSの場合
#import math, itertools, bisect, functools, copy, decimal
## 天井と床関数は丸める仕様らしく、桁数が上がると期待通りの動作をしないことを確認したのでimportしていない
#from decimal import Decimal, ROUND_HALF_UP, ROUND_HALF_EVEN, ROUND_UP, ROUND_DOWN # 左のROUND_HALF_UPから四捨五入、四捨五入(銀行丸め)、切り上げ、切り捨て
#from collections import defaultdict, Counter, deque
#
#N, M = map(int, input().split())
#
#res_dict = defaultdict(set)
#for _ in range(M):
#    u, v = map(int, input().split())
#    res_dict[u].add(v)
#    res_dict[v].add(u)
#
#res_set = set()
#seen_lists = [False] * (N+1)
#def dfs(e):
#    # iの値を受け取ってすでに訪問済みであれば、別のiの時に連結成分として探索済みなのでTrueを返却
#    if seen_lists[e]:
#        return True
#    # 探索済み出ない場合であれば連結成分に該当するものをTrueとして更新していく
#    seen_lists[e] = True
#    e_set = res_dict[e]
#    for e in e_set:
#        dfs(e)
#
#res = 0
#for i in range(1, N+1):
#    if dfs(i):
#        continue
#    # 最初のiの入力でTrueが返却されなければカウントする処理をできる
#    res += 1
#
#print(res)