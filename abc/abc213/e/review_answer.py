'''
(1) 壊す or 壊さないの2択で壊さないところを優先的に探索すれば良さそうなので01BFSだが、自分の解答ではダイクストラで代用
(2) まずは壊さずに進めるところを優先的に探索し、壊さないといけないところはコストを+1するイメージ
(3) +1して進める範囲をどうするかだが、結局は解説に記載してある範囲を移動できるようになると考えてしまえばOK
    →壊す必要がないところも含むがそこは壊さないと行けないところと思うので+1しても問題がないと思われる
    →すでに小さい値を付与されていたり、あとでコストをより小さくできたりできそう
'''

from collections import deque

H, W = map(int, input().split())
S = [input() for _ in range(H)]

INF = 10**18
dist = [[INF] * W for _ in range(H)]
dist[0][0] = 0

dq = deque()
dq.append((0, 0))

# コスト0の移動
move0 = [(-1,0), (1,0), (0,-1), (0,1)]

# コスト1の移動（5×5内、角4マス除外）
move1 = []
for di in range(-2, 3):
    for dj in range(-2, 3):
        if abs(di) == 2 and abs(dj) == 2:
            continue
        if di == 0 and dj == 0:
            continue
        move1.append((di, dj))

while dq:
    i, j = dq.popleft()

    # コスト0移動
    for di, dj in move0:
        ni = i + di
        nj = j + dj

        if 0 <= ni < H and 0 <= nj < W:
            if S[ni][nj] == ".":
                if dist[ni][nj] > dist[i][j]:
                    dist[ni][nj] = dist[i][j]
                    dq.appendleft((ni, nj))

    # コスト1移動
    for di, dj in move1:
        ni = i + di
        nj = j + dj

        if 0 <= ni < H and 0 <= nj < W:
            if dist[ni][nj] > dist[i][j] + 1:
                dist[ni][nj] = dist[i][j] + 1
                dq.append((ni, nj))

print(dist[H-1][W-1])