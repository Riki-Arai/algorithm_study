'''
(1) まずは木なのでサイクルは存在しない。そして1本の次数のものは潰しが効くので、最大最大次数のものから攻めると良さそう
(2) 番号の割り振り方についてはなるべくすでに使用した番号を使いたい
(3) そこで接続している辺のうちで番号をすでに割り振った番号を起点にまずは-1を行い、それでも不足していれば+1を行う
'''
from collections import deque
import sys

input = sys.stdin.readline

N = int(input())

G = [[] for _ in range(N)]
edges = []

for i in range(N - 1):
    a, b = map(int, input().split())
    a -= 1
    b -= 1
    G[a].append((b, i))
    G[b].append((a, i))
    edges.append((a, b))

# 最大次数の頂点（同率なら番号最小）
root = 0
mx = -1
for i in range(N):
    if len(G[i]) > mx:
        mx = len(G[i])
        root = i

K = mx
ans = [0] * (N - 1)

visited = [False] * N
visited[root] = True

# (頂点, 親辺の色)
q = deque()
q.append((root, K + 1))   # 根では全て1から使いたいので K+1 とする

while q:
    v, prev = q.popleft()

    # 使用可能な色を作る
    colors = []

    # prev-1, prev-2, ..., 1
    for c in range(prev - 1, 0, -1):
        colors.append(c)

    # prev+1, prev+2, ..., K
    for c in range(prev + 1, K + 1):
        colors.append(c)

    idx = 0
    for nv, eid in G[v]:
        if visited[nv]:
            continue
        col = colors[idx]
        idx += 1
        ans[eid] = col
        visited[nv] = True
        q.append((nv, col))

print(K)
print(*ans, sep="\n")