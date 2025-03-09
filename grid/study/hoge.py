H, W, X, Y = map(int, input().split())
grid = [list(input()) for _ in range(H)]

directions = [(-1, 0), (0, 1), (1, 0), (0, -1)]
res = 1 
for dx, dy in directions:
    x, y = X-1, Y-1
    while True:
        x += dx
        y += dy
        if 0 > x or x >= H or 0 > y or y >= W:
            break
        elif grid[x][y] == "#":
            break
        res += 1

print(res)
