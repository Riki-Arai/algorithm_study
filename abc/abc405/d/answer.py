import copy
from collections import deque

H, W = map(int, input().split()) # 取得例：1 2

g_lists = [list(input()) for _ in range(H)] # 取得例:[["#","#"], [".","."]・・・["#","#"]]、文字列をリストに分解

dq = deque()
seen_sets = set()
for i in range(H):
    for j in range(W):
        if g_lists[i][j] == "E":
            dq.append((i, j))
            seen_sets.add((i, j))

move_dicts = {"v":(-1, 0), ">":(0, -1), "^":(1, 0), "<":(0, 1)}
res_lists = copy.deepcopy(g_lists)
while len(dq):
    i, j = dq.popleft()
    for dir, x in move_dicts.items():
        ii = i + x[0]
        jj = j + x[1]
        if 0 <= ii < H and 0 <= jj < W and g_lists[ii][jj] == "." and (ii, jj) not in seen_sets:
            res_lists[ii][jj] = dir
            seen_sets.add((ii, jj))
            dq.append((ii, jj))

for res_list in res_lists:
    print("".join(res_list))