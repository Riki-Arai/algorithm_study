from collections import deque

H, W = map(int, input().split())
S_lists = [list(input()) for _ in range(H)] # 取得例:[["#","#"], [".","."]・・・["#","#"]]

move_lists = {"L":(-1, 0), "U":(0, -1), "R":(1, 0), "D":(0, 1)}.values()
grid_lists = []
for i in range(H):
    for j in range(W):
        if S_lists[i][j] == ".":
            for mj, mi in move_lists:
                ii = i + mi
                jj = j + mj
                if 0 <= ii < H and 0 <= jj < W and S_lists[ii][jj] == "#":
                    break
            else:
                grid_lists.append((i, j))

res = 1
seen_set = set()
for i, j in grid_lists:
    if (i, j) in seen_set:
        continue
    tmp_res = 1
    dq = deque()
    dq.append((i, j))
    seen_set.add((i, j))
    aroud_set = set()
    while len(dq):
        i, j = dq.popleft()
        if S_lists[i][j] == ".":
            for mj, mi in move_lists:
                jj = j + mj
                ii = i + mi
                if 0 <= ii < H and 0 <= jj < W and (ii, jj) not in seen_set:
                    for mj2, mi2 in move_lists:
                        if 0 <= ii+mi2 < H and 0 <= jj+mj2 < W and S_lists[ii+mi2][jj+mj2] == "#":
                            aroud_set.add((ii, jj))
                            break
                    else:
                        tmp_res += 1
                        seen_set.add((ii, jj))
                        dq.append((ii, jj))

    res = max(tmp_res+len(aroud_set), res)

print(res)