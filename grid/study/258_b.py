n = int(input())
grid = [input() for _ in range(n)]

# 8方向の移動
directions = [(-1, 0), (1, 0), (0, -1), (0, 1),
              (-1, 1), (-1, -1), (1, -1), (1, 1)]  # 右下 (1, 1) を追加

max_number = 0  # `-float('inf')` ではなく `0` にする

for i in range(n):
    for j in range(n):
        for dx, dy in directions:
            x, y = i, j
            num_list = []
            for _ in range(n):
                num_list.append(grid[x][y])
                x = (x + dx) % n  # 円環状の移動
                y = (y + dy) % n  # 円環状の移動
            max_number = max(max_number, int("".join(num_list)))

print(max_number)

