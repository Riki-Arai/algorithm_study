from collections import deque

H, W = map(int, input().split()) # 取得例：1 2
S_lists = [list(input()) for _ in range(H)] # 取得例:[["#","#"], [".","."]・・・["#","#"]]、文字列をリストに分解

MOD = 10**9+7
move_lists = [(1, 0), (0, 1)]
dq = deque([(0, 0)])
dp_lists = [[0]*W for _ in range(H)]
dp_lists[0][0] = 1
seen_sets = set([(0, 0)])
while len(dq):
    i, j = dq.popleft()
    for mi, mj in move_lists:
        ii = i + mi
        jj = j + mj
        if 0 <= ii < H and 0 <= jj < W and S_lists[ii][jj] == "." and (ii, jj) not in seen_sets:
            dp_lists[ii][jj] = (dp_lists[ii][jj]+dp_lists[i][j])%MOD
            dq.append((ii, jj))
            seen_sets.add((ii, jj))
        elif 0 <= ii < H and 0 <= jj < W and S_lists[ii][jj] == "." and (ii, jj) in seen_sets:
            dp_lists[ii][jj] = (dp_lists[ii][jj]+dp_lists[i][j])%MOD

print(dp_lists[H-1][W-1])