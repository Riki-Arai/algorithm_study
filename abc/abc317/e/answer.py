'''
(1) 視線で通れないところをマークし、その後にBFSをすればいい
(2) 計算量的にも最悪な見積もりでも0(2*H*W)なので間に合う
(3) setの判定方法が重かったのでC++でAC
'''
from collections import deque

H, W = map(int, input().split())
grid = [list(input()) for _ in range(H)]
 
# 視線によって見られているマスを保存する
# (方向, 行, 列) を入れる
seen_sets = set()
directions = {
    ">": (0, 1),
    "v": (1, 0),
    "<": (0, -1),
    "^": (-1, 0),
}
q = deque()
start = None
goal = None
for i in range(H):
    for j in range(W):
        if grid[i][j] == "S":
            start = (i, j)
        elif grid[i][j] == "G":
            goal = (i, j)
        elif grid[i][j] == "#":
            seen_sets.add(("", i, j))
        elif grid[i][j] in directions:
            q.append((grid[i][j], i, j))

# --------------------------------------------------
# 人の視線を調べる
# --------------------------------------------------
while len(q):
    direction, i, j = q.popleft()
    di, dj = directions[direction]
    ni = i + di
    nj = j + dj
    while 0 <= ni < H and 0 <= nj < W:
        if grid[ni][nj] == "#":
            break
        elif grid[ni][nj] in directions:
            break
        elif grid[ni][nj] == "!":
            if direction == "<" and (("<", ni, nj) in seen_sets or (">", ni, nj) in seen_sets):
                break
            elif direction == ">" and (("<", ni, nj) in seen_sets or (">", ni, nj) in seen_sets):
                break
            elif direction  == "^" and (("^", ni, nj) in seen_sets or ("v", ni, nj) in seen_sets):
                break
            elif direction  == "v" and (("^", ni, nj) in seen_sets or ("v", ni, nj) in seen_sets):
                break
        else:
            seen_sets.add((direction, ni, nj))
            grid[ni][nj] = "!"

        # S/G は問題上、視線に入らないことが保証されている
        ni += di
        nj += dj

dist = [[-1] * W for _ in range(H)]
q = deque()
q.append(start)
dist[start[0]][start[1]] = 0
while q:
    i, j = q.popleft()

    if (i, j) == goal:
        print(dist[i][j])
        exit()

    for di, dj in ((1, 0), (-1, 0), (0, 1), (0, -1)):
        ni = i + di
        nj = j + dj

        if not (0 <= ni < H and 0 <= nj < W):
            continue

        # 訪問済み
        if dist[ni][nj] != -1:
            continue

        # 通れないマス
        if grid[ni][nj] != "." and grid[ni][nj] != "G":
            continue

        dist[ni][nj] = dist[i][j] + 1
        q.append((ni, nj))

print(-1)