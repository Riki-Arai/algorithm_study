from collections import defaultdict, deque

H, W = map(int, input().split()) # 取得例：1 2
S_lists = [list(input()) for _ in range(H)]

alp_dict = defaultdict(list)
for i in range(H):
    for j in range(W):
        if S_lists[i][j] not in (".", "#"):
            alp_dict[S_lists[i][j]].append((i, j))

move_lists = [(-1, 0), (0, -1), (1, 0), (0, 1)]
seen_set = set()
seen_alp_set = set()
dq = deque()
dq.append((0, 0, 0))
seen_set.add((0, 0))
while len(dq):
    i, j, res = dq.popleft()
    if i == H-1 and j == W-1:
        print(res)
        exit()

    b = S_lists[i][j]
    if b == ".":
        for mi, mj in move_lists:
            ii = i+mi
            jj = j+mj
            if 0 <= ii < H and 0 <= jj < W and (ii, jj) not in seen_set and S_lists[ii][jj] != "#":
                seen_set.add((ii, jj))
                dq.append((ii, jj, res+1))
    elif b == "#":
        continue
    else:
        if b not in seen_alp_set:
            seen_alp_set.add(b)
            for wi, wj in alp_dict[b]:
                if (wi, wj) not in seen_set:
                    seen_set.add((wi, wj))
                    dq.append((wi, wj, res+1))
        for mi, mj in move_lists:
            ii = i+mi
            jj = j+mj
            if 0 <= ii < H and 0 <= jj < W and (ii, jj) not in seen_set and S_lists[ii][jj] != "#":
                seen_set.add((ii, jj))
                dq.append((ii, jj, res+1))

print(-1)