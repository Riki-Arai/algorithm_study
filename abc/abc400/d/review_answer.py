from collections import deque

H, W = map(int, input().split())
S = [input() for _ in range(H)]
A, B, C, D = map(int, input().split())

A -= 1
B -= 1
C -= 1
D -= 1

INF = 10**18
dist = [[INF] * W for _ in range(H)]
dist[A][B] = 0

dq = deque()
dq.append((A, B))

directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]

while dq:
    i, j = dq.popleft()

    # コスト0: 隣の通路へ普通に移動
    for di, dj in directions:
        ni = i + di
        nj = j + dj

        if 0 <= ni < H and 0 <= nj < W:
            if S[ni][nj] == "." and dist[ni][nj] > dist[i][j]:
                dist[ni][nj] = dist[i][j]
                dq.appendleft((ni, nj))

    # コスト1: パンチして1マス先・2マス先へ行けるようにする
    for di, dj in directions:
        for k in range(1, 3):
            ni = i + di * k
            nj = j + dj * k

            if 0 <= ni < H and 0 <= nj < W:
                if dist[ni][nj] > dist[i][j] + 1:
                    dist[ni][nj] = dist[i][j] + 1
                    dq.append((ni, nj))

print(dist[C][D])