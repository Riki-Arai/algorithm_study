from collections import deque

H, W = map(int, input().split())
S_lists = [list(input()) for _ in range(H)] # 取得例:[["#","#"], [".","."]・・・["#","#"]]

S = "snuke"
move_lists = [(-1, 0), (0, -1), (1, 0), (0, 1)]
seen_set = set()
seen_set.add((0, 0))
dq = deque()
dq.append((0, 0, 0))
while len(dq):
    i, j, s_i = dq.popleft()
    if i == H-1 and j == W-1:
        print("Yes")
        exit()

    n_s_i = (s_i+1)%5
    for mi, mj in move_lists:
        ii = i + mi
        jj = j + mj
        if 0 <= ii < H and 0 <= jj < W and S[n_s_i] == S_lists[ii][jj] and (ii, jj) not in seen_set:
            dq.append((ii, jj, n_s_i))
            seen_set.add((ii, jj))

print("No" )