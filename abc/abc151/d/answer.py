import itertools as it
from collections import deque


H, W = map(int, input().split()) # 取得例：1 2
S_lists = [list(input()) for _ in range(H)] # 取得例:[["#","#"], [".","."]・・・["#","#"]]、文字列をリストに分解

s_lists = []
for i in range(H):
    for j in range(W):
        if S_lists[i][j] == ".":
            s_lists.append((i, j))

res = 0
move_lists = {"L":(-1, 0), "U":(0, -1), "R":(1, 0), "D":(0, 1)}.values()
for si, sj in s_lists:
    seen_sets = set([(si, sj)])
    dq = deque([(si, sj, 0)])
    dis_lists = [[-float("INF")]*W for _ in range(H)]
    dis_lists[si][sj] = 0
    while len(dq):
        i, j, dis = dq.popleft()
        for mi, mj in move_lists:
            ii = i + mi
            jj = j + mj
            if 0 <= ii < H and 0 <= jj < W and S_lists[ii][jj] == "." and (ii, jj) not in seen_sets:
                seen_sets.add((ii, jj))
                dis_lists[ii][jj] = dis + 1
                dq.append((ii, jj, dis+1))

    for gi in range(H):
        for gj in range(W):
            if (si, sj) != (gi, gj) and S_lists[gi][gj] == ".":
                res = max(dis_lists[gi][gj], res)

print(res)