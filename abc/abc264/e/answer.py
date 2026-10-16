'''
(1) 電線が切れるたびにBFSなどで全探索をするなどをしたところでTLEになってしまう
(2) そこで反対に考えて全て切れた状態から始めて修復する目線で考えてみる
(3) 修復した際にBFSで頂点の繋がりを調べていてはTLEになるのでDSUを使用していくい
(4) 最後のX_listのfor文の処理は単純にDSUにmergeしていけば良い（最初はBFSで探索をしてしまってTLEにしてしまっていた）
'''
from collections import deque
from atcoder.dsu import DSU

N, M, E = map(int, input().split()) # 取得例：1 2
input_lists = [list(map(int, input().split())) for _ in range(E)] # 取得例:[[1,2], [3,4]・・[9,10]]、空白区切りの数値入力

Q = int(input().strip())
X_list = list(reversed([int(input()) for _ in range(Q)])) # 取得例：[A1,A2・・・An]、N行の入力用(int型に変換)
x_set = set(X_list)

g_lsits = [[] for _ in range(N+M+1)]
for i, input_list in enumerate(input_lists, 1):
    if i not in x_set:
        u, v = input_list
        g_lsits[u].append(v)
        g_lsits[v].append(u)

dsu = DSU(N+M)
dq = deque()
for i in range(N+1, N+M+1):
    dsu.merge(N, i-1)

seen_set = set()
for i in range(1, N+M+1):
    if i in seen_set:
        continue
    dq.append(i)
    while len(dq):
        u = dq.popleft()
        for v in g_lsits[u]:
            dsu.merge(u-1, v-1)
            if v not in seen_set:
                seen_set.add(v)
                dq.append(v)

res_list = [dsu.size(N)-M]
for x in X_list:
    u, v = input_lists[x-1]
    dsu.merge(u-1, v-1)
    res_list.append(dsu.size(N)-M)

for res in reversed(res_list[:-1]):
    print(res)