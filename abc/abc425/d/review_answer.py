from collections import deque

H, W = map(int, input().split()) # 取得例：1 2
S_lists = [list(input()) for _ in range(H)] # 取得例:[["#","#"], [".","."]・・・["#","#"]]、文字列をリストに分解

c_lists = [[float("INF")]*W for _ in range(H)]
dq = deque()
for i in range(H):
    for j in range(W):
        if S_lists[i][j] == "#":
            dq.append((i, j, 0))
            c_lists[i][j] = 0

move_lists = {"L":(-1, 0), "U":(0, -1), "R":(1, 0), "D":(0, 1)}.values()
while len(dq):
    i, j, c = dq.popleft()
    for mi, mj in move_lists:
        ii = i+mi
        jj = j+mj
        if 0 <= ii < H and 0 <= jj < W and c_lists[ii][jj] == float("INF"):
            count = 0
            for mi2, mj2 in move_lists:
                iii = ii+mi2
                jjj = jj+mj2
                if 0 <= iii < H and 0 <= jjj < W and c_lists[iii][jjj] <= c:
                    count += 1

            if count == 1:
                c_lists[ii][jj] = c+1
                dq.append((ii, jj, c+1))

res = 0
for i in range(H):
    for j in range(W):
        if c_lists[i][j] != float("INF"):
            res += 1

print(res)