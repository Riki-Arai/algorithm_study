H, W, X, Y = map(int, input().split())
grid = [list(input()) for _ in range(H)]
directions = [(-1, 0), (0, 1), (1, 0), (0, -1)]
counter = 1

for dx, dy in directions:
    x, y = X-1, Y-1
    while True:
        x+=dx
        y+=dy
        if x < 0 or x >= H or y < 0 or y >= W:
            break
        elif grid[x][y]=='#':
            break
        counter += 1

print(counter)
