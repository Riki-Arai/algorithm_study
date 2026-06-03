from sortedcontainers import SortedList

H, W, Q = map(int, input().split())

h_lists = [SortedList() for _ in range(H + 1)]
for i in range(1, H + 1):
    for j in range(1, W + 1):
        h_lists[i].add(j)

w_lists = [SortedList() for _ in range(W + 1)]
for j in range(1, W + 1):
    for i in range(1, H + 1):
        w_lists[j].add(i)

broken = set()
def destroy(r, c):
    if (r, c) in broken:
        return
    broken.add((r, c))
    h_lists[r].discard(c)
    w_lists[c].discard(r)

for _ in range(Q):
    R, C = map(int, input().split())

    if (R, C) not in broken:
        destroy(R, C)
        continue

    row = h_lists[R]
    idx = row.bisect_left(C)
    if idx - 1 >= 0:
        left_c = row[idx - 1]
        destroy(R, left_c)

    row = h_lists[R]
    idx = row.bisect_left(C)
    if idx < len(row):
        right_c = row[idx]
        destroy(R, right_c)

    col = w_lists[C]
    idx = col.bisect_left(R)

    if idx - 1 >= 0:
        up_r = col[idx - 1]
        destroy(up_r, C)

    col = w_lists[C]
    idx = col.bisect_left(R)
    if idx < len(col):
        down_r = col[idx]
        destroy(down_r, C)

print(H * W - len(broken))