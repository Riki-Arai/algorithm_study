### DFSを使った場合
import sys, math, itertools, bisect, functools, copy, decimal
# 天井と床関数は丸める仕様らしく、桁数が上がると期待通りの動作をしないことを確認したのでimportしていない
from decimal import Decimal, ROUND_HALF_UP, ROUND_HALF_EVEN, ROUND_UP, ROUND_DOWN # 左のROUND_HALF_UPから四捨五入、四捨五入(銀行丸め)、切り上げ、切り捨て
from collections import defaultdict, Counter, deque
from atcoder.dsu import DSU
sys.setrecursionlimit(10**7)

N, D = map(int, input().split())
A_lists = [list(map(int, input().split())) for _ in range(N)]

res_set = set([0])
def dfs(i):
    x, y = A_lists[i]
    for j in range(N):
        if i != j:
            xx, yy = A_lists[j]
            # DFSでも感染済みであるかどうかのチェックが必要で、このチェックをすればreturnが不要
            if j not in res_set and pow(abs(x-xx), 2) + pow(abs(y-yy), 2) <= D*D:
                res_set.add(j)
                dfs(j)

dfs(0)
for i in range(N):
    if i in res_set:
        print("Yes")
    else:
        print("No")


### BFSを使った場合
import sys, math, itertools, bisect, functools, copy, decimal
# 天井と床関数は丸める仕様らしく、桁数が上がると期待通りの動作をしないことを確認したのでimportしていない
from decimal import Decimal, ROUND_HALF_UP, ROUND_HALF_EVEN, ROUND_UP, ROUND_DOWN # 左のROUND_HALF_UPから四捨五入、四捨五入(銀行丸め)、切り上げ、切り捨て
from collections import defaultdict, Counter, deque
from atcoder.dsu import DSU
sys.setrecursionlimit(10**7)

N, D = map(int, input().split())
A_lists = [list(map(int, input().split())) for _ in range(N)]

res_list = ["No"] * N
dq = deque()
res_list[0] = "Yes"
dq.append(0)
while len(dq):
    n = dq.pop()
    for i in range(N):
        # 感染済みであるものは対象外であり、そこも探索対象にしてしまうと無限ループになる
        if i != n and res_list[i] == "No":
            x, y = A_lists[n]
            xx, yy = A_lists[i]
            if pow(abs(x-xx), 2) + pow(abs(y-yy), 2) <= D*D:
                dq.append(i)
                res_list[i] = "Yes"

print(*res_list, sep='\n')

### DSUを使った場合
import sys, math, itertools, bisect, functools, copy, decimal
# 天井と床関数は丸める仕様らしく、桁数が上がると期待通りの動作をしないことを確認したのでimportしていない
from decimal import Decimal, ROUND_HALF_UP, ROUND_HALF_EVEN, ROUND_UP, ROUND_DOWN # 左のROUND_HALF_UPから四捨五入、四捨五入(銀行丸め)、切り上げ、切り捨て
from collections import defaultdict, Counter, deque
from atcoder.dsu import DSU
sys.setrecursionlimit(10**7)

N, D = map(int, input().split())
A_lists = [list(map(int, input().split())) for _ in range(N)]

dsu = DSU(N)
for i in range(N):
    for j in range(N):
        if i != j:
            a, b = A_lists[i]
            aa, bb = A_lists[j]
            # sqrtを使ってしまうとTLEになってしまう
            if pow(abs(a-aa), 2) + pow(abs(b-bb), 2) <= D*D:
                dsu.merge(i, j)

for i in range(N):
    if dsu.same(0, i):
        print("Yes")
    else:
        print("No")