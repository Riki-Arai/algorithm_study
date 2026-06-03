import heapq

dxdy = ((0, 1), (0, -1), (1, 0), (-1, 0))
H, W = map(int, input().split())
MAP = [list(input()) for _ in range(H)]

energy = [[0] * W for _ in range(H)]
N = int(input())
for _ in range(N):
    r, c, e = map(int, input().split())
    r -= 1
    c -= 1
    energy[r][c] = e

for i in range(H):
    for j in range(W):
        if MAP[i][j] == "S":
            sy, sx = i, j
        elif MAP[i][j] == "T":
            gy, gx = i, j

dist = [[-1] * W for _ in range(H)]
pq = []
dist[sy][sx] = energy[sy][sx]
heapq.heappush(pq, (-energy[sy][sx], sy, sx))
while pq:
    d, y, x = heapq.heappop(pq)
    d *= -1

    if dist[y][x] > d:
        continue

    if y == gy and x == gx:
        print("Yes")
        exit()

    if d == 0:
        continue

    for dx, dy in dxdy:
        nx = x + dx
        ny = y + dy

        if 0 <= nx < W and 0 <= ny < H and MAP[ny][nx] != "#":
            nd = max(d - 1, energy[ny][nx])

            if dist[ny][nx] >= nd:
                continue

            dist[ny][nx] = nd
            heapq.heappush(pq, (-nd, ny, nx))

print("No")