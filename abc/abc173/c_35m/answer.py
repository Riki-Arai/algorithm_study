import sys
import itertools

input = sys.stdin.readline
H, W, K = map(int, input().split())
A = [input().strip() for _ in range(H)]

# 黒マスの座標をリスト化
black_cells = [(i, j) for i in range(H) for j in range(W) if A[i][j] == '#']
total_black = len(black_cells)

res = 0
# itertools.productを使って行・列を全探索
for row_sel in itertools.product([0, 1], repeat=H):
    for col_sel in itertools.product([0, 1], repeat=W):
        painted = 0
        # 選んだ行または列に属する黒マスをカウント
        for r, c in black_cells:
            if row_sel[r] == 1 or col_sel[c] == 1:
                painted += 1
        # 残る黒マスがK個ならカウント
        if total_black - painted == K:
            res += 1

print(res)