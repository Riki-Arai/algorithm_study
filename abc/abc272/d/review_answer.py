from collections import deque

n, m = map(int, input().split())

D = [[-1] * n for _ in range(n)]
D[0][0] = 0
move = []
for i in range(-n, n + 1):
    for j in range(-n, n + 1):
        if i**2 + j**2 == m:
            move.append((i, j))

queue = deque([(0, 0)])
while queue:
    i, j = queue.popleft()
    for di, dj in move:
        ni, nj = i + di, j + dj
        if not (0 <= ni < n and 0 <= nj < n):
            continue
        if D[ni][nj] == -1:
            D[ni][nj] = D[i][j] + 1
            queue.append((ni, nj))
for row in D:
    print(*row)
