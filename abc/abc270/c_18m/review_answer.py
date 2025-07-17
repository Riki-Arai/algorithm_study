# Cythonなら通った。再帰はCythonの方が早いことが多いらしい。
import sys, math, itertools, bisect, functools, copy, decimal
# 天井と床関数は丸める仕様らしく、桁数が上がると期待通りの動作をしないことを確認したのでimportしていない
from decimal import Decimal, ROUND_HALF_UP, ROUND_HALF_EVEN, ROUND_UP, ROUND_DOWN # 左のROUND_HALF_UPから四捨五入、四捨五入(銀行丸め)、切り上げ、切り捨て
from collections import defaultdict, Counter, deque
from atcoder.dsu import DSU
sys.setrecursionlimit(10**7)

N, X, Y = map(int, input().split())
e_dict = defaultdict(set)
for _ in range(N-1):
    U, V = map(int, input().split())
    e_dict[U].add(V)
    e_dict[V].add(U)

res_list = []
n_list = [False] * (N+1)
def dfs(i):
    if n_list[i]:
        return
    n_list[i] = True
    res_list.append(i)
    for e in e_dict[i]:
        if e == Y:
            res_list.append(e)
            print(*res_list)
            break
        dfs(e)
    res_list.pop(-1)

dfs(X)


### 以下はBFS版
# 親情報を記録しておくとうのは知らない方法で、最初は探索終了後にpopで頑張ろうとしていた
# しかし今回の問題においてはDFSの方がだいぶ楽に実装できるので、この実装は勉強としておく
import sys, math, itertools, bisect, functools, copy, decimal
# 天井と床関数は丸める仕様らしく、桁数が上がると期待通りの動作をしないことを確認したのでimportしていない
from decimal import Decimal, ROUND_HALF_UP, ROUND_HALF_EVEN, ROUND_UP, ROUND_DOWN # 左のROUND_HALF_UPから四捨五入、四捨五入(銀行丸め)、切り上げ、切り捨て
from collections import defaultdict, Counter, deque
from atcoder.dsu import DSU
sys.setrecursionlimit(10**7)

N, X, Y = map(int, input().split())
e_dict = defaultdict(set)
for _ in range(N-1):
    U, V = map(int, input().split())
    e_dict[U].add(V)
    e_dict[V].add(U)

n_list = [False] * (N+1)
parent_list = [-1]*(N+1)
dq = deque()
dq.append(X)
while len(dq):
    cur_e = dq.popleft()
    if n_list[cur_e]:
        continue
    n_list[cur_e] = True
    for e in e_dict[cur_e]:
        # ゴールから逆算してたどる時に利用する
        if parent_list[e] == -1:
            parent_list[e] = cur_e
        if n_list[e]:
            continue
        if e == Y:
            res_list = [Y]
            # 親のエッジさえわかればゴールからスタートへと逆算で辿れる
            while res_list[-1] != X:
                res_list.append(parent_list[res_list[-1]])
            print(*res_list[::-1])
            exit()
        dq.append(e)