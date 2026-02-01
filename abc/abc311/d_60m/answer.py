from collections import deque

N, M = map(int, input().split())
g_lists = [list(input()) for _ in range(N)] # 取得例:[["#","#"], [".","."]・・・["#","#"]]

pass_lists = [[None]*M for _ in range(N)]
for i in range(N):
    for j in range(M):
        if g_lists[i][j] == ".":
            pass_lists[i][j] = False

move_dict = {"L":(0, -1), "U":(-1, 0), "R":(0, 1), "D":(1, 0)}
dq = deque([("L", (1, 1)), ("U", (1, 1)), ("R", (1, 1)), ("D", (1, 1))])
seen_sets = set([("L", (1, 1)), ("U", (1, 1)), ("R", (1, 1)), ("D", (1, 1))])
pass_lists[1][1] = True
res = 1
while len(dq):
    m, cur_ij = dq.popleft()
    i, j = cur_ij
    mi, mj = move_dict[m]
    ii = i + mi
    jj = j + mj
    if 0 <= ii < N and 0 <= jj < M and g_lists[ii][jj] == "." and (m, ii, jj) not in seen_sets:
        dq.append((m, (ii, jj)))
        seen_sets.add((m, ii, jj))
        if not pass_lists[ii][jj]:
            pass_lists[ii][jj] = True
            res += 1
    elif 0 <= ii < N and 0 <= jj < M and g_lists[ii][jj] == "#":
        for m, move_ij in move_dict.items():
            mi, mj = move_ij
            ii = i + mi
            jj = j + mj
            if 0 <= ii < N and 0 <= jj < M and g_lists[ii][jj] == "." and (m, ii, jj) not in seen_sets:
                dq.append((m, (ii, jj)))
                seen_sets.add((m, ii, jj))
                if not pass_lists[ii][jj]:
                    pass_lists[ii][jj] = True
                    res += 1

print(res)