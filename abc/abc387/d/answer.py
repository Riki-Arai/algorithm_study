from collections import defaultdict, deque, Counter

H, W = map(int, input().split())

S_lists = [list(input()) for _ in range(H)] # 取得例:[["#","#"], [".","."]・・・["#","#"]]
dq = deque()
seen_set = set()
for i in range(H):
    for j in range(W):
        if S_lists[i][j] == "S":
            dq.append((0, 0, i, j))
            dq.append((1, 0, i, j))
            seen_set.add((0, i, j))
            seen_set.add((1, i, j))
        elif S_lists[i][j] == "G":
            g = (i, j)

res = float("INF")
move_lists = [[(-1, 0), (1, 0)], [(0, -1), (0, 1)]]
while len(dq):
    bit_m, dis, i, j  = dq.popleft()
    for mi, mj in move_lists[bit_m]:
        ii, jj = i+mi, j+mj
        if ii == g[0] and jj == g[1]:
            res = min(dis+1, res)
            continue
        if 0 <= ii < H and 0 <= jj < W and S_lists[ii][jj] != "#" and (bit_m, ii, jj) not in seen_set:
            seen_set.add((bit_m, ii, jj))
            dq.append((bit_m^1, dis+1, ii, jj))

if res == float("INF"):
    print(-1)
else:
    print(res)