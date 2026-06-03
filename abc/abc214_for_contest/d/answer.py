import heapq as hq

H, W = map(int, input().split())
S_lists = [list(input()) for _ in range(H)]

move_lists = [
    (0, -1), (1, -1), (1, 0), (1, 1),
    (0, 1), (-1, 1), (-1, 0), (-1, -1)
]

T_lists = [["."] * W for _ in range(H)]
for i in range(H):
    for j in range(W):
        if S_lists[i][j] == ".":
            for mi, mj in move_lists:
                ii = i + mi
                jj = j + mj
                if 0 <= ii < H and 0 <= jj < W and S_lists[ii][jj] == "#":
                    T_lists[i][j] = "#"
                    break

INF = 10**18
dis_lists = [[INF] * W for _ in range(H)]
dq_lists = []
hq.heapify(dq_lists)

for i in range(H):
    for j in range(W):
        if T_lists[i][j] == "#":
            hq.heappush(dq_lists, (0, i, j))
            dis_lists[i][j] = 0

while dq_lists:
    dis, i, j = hq.heappop(dq_lists)

    if dis > dis_lists[i][j]:
        continue

    for mi, mj in move_lists:
        ii = i + mi
        jj = j + mj

        if 0 <= ii < H and 0 <= jj < W and dis_lists[ii][jj] > dis + 1:
            dis_lists[ii][jj] = dis + 1
            hq.heappush(dq_lists, (dis + 1, ii, jj))

res_lists = [["."] * W for _ in range(H)]
for i in range(H):
    for j in range(W):
        if dis_lists[i][j] != INF and dis_lists[i][j] % 2 == 1:
            res_lists[i][j] = "#"

for res_list in res_lists:
    print("".join(res_list))