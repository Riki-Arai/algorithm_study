import sys
input = sys.stdin.readline
H, W = map(int, input().split())
grid = [list(input().rstrip()) for _ in range(H)]

# 8方向へのオフセット
offsets = [(0, 1), (0, -1), (1, 0), (-1, 0),
           (1, 1), (1, -1), (-1, 1), (-1, -1)]

for i in range(H):
    for j in range(W):
        if grid[i][j] == '.':
            # 周囲8マスで '#' の数をカウントして置き換える
            grid[i][j] = str(sum(
                0 <= i+di < H and 0 <= j+dj < W
                and grid[i+di][j+dj] == '#'
                for di, dj in offsets
            ))

# 文字列にして出力
print(*(''.join(row) for row in grid), sep='\n')
