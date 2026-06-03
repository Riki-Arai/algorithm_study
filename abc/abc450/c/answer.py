from collections import deque

H, W = map(int, input().split()) # 取得例：1 2
S_lists = [list(input()) for _ in range(H)] # 取得例:[["#","#"], [".","."]・・・["#","#"]]、文字列をリストに分解

res = 0
move_lists = {"L":(-1, 0), "U":(0, -1), "R":(1, 0), "D":(0, 1)}.values()
dq = deque()
seen_sets = set()
for i in range(H):
    for j in range(W):
        if (i, j) in seen_sets:
            continue

        if S_lists[i][j] == "#":
            seen_sets.add((i, j))
            continue

        res_flag = True
        dq.append((i, j))
        seen_sets.add((i, j))
        while len(dq):
            ii, jj = dq.popleft()
            for mi in range(-1, 2):
                for mj in range(-1, 2):
                    if mi == 0 and mj == 0:
                        continue
                    iii = ii + mi
                    jjj = jj + mj
                    if not(0 <= iii < H):
                        res_flag = False

                    if not(0 <= jjj < W):
                        res_flag = False

            for mi, mj in move_lists:
                iiii = ii + mi
                jjjj = jj + mj
                if 0 <= iiii < H and 0 <= jjjj < W and S_lists[iiii][jjjj] == "." and (iiii, jjjj) not in seen_sets:
                    seen_sets.add((iiii, jjjj))
                    dq.append((iiii, jjjj))

        if res_flag:
            res += 1

print(res)