import sys, math, itertools, bisect, functools, copy, decimal
# 天井と床関数は丸める仕様らしく、桁数が上がると期待通りの動作をしないことを確認したのでimportしていない
from decimal import Decimal, ROUND_HALF_UP, ROUND_HALF_EVEN, ROUND_UP, ROUND_DOWN # 左のROUND_HALF_UPから四捨五入、四捨五入(銀行丸め)、切り上げ、切り捨て
from collections import defaultdict, Counter, deque
from atcoder.dsu import DSU

R, C = map(int, sys.stdin.readline().split())
sy, sx = map(int, sys.stdin.readline().split())
gy, gx = map(int, sys.stdin.readline().split())
G_lists = [list(input()) for _ in range(R)]
sx -= 1
sy -= 1
gx -= 1
gy -= 1

dq = deque()
move_dict = {"L":(-1, 0), "U":(0, -1), "R":(1, 0), "D":(0, 1)}
move_list = list(move_dict.values())
dq.append((sx, sy))
dis_lists = [[-1]*C for _ in range(R)]
dis_lists[sy][sx] = 0

while dq:
    x, y = dq.popleft()
    for mx, my in move_list:
        xx = x + mx
        yy = y + my
        if not (0 <= yy < R and 0 <= xx < C):
            continue
        if G_lists[yy][xx] == "#":
            continue
        if dis_lists[yy][xx] == -1:
            dis_lists[yy][xx] = dis_lists[y][x] + 1
            dq.append((xx, yy))

print(dis_lists[gy][gx])
