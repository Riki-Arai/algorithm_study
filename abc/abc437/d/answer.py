from bisect import bisect_left

N, Q = map(int, input().split())
A_list = list(map(int, input().split()))

A_list.sort()
res_list = []
for _ in range(Q):
    X, Y = map(int, input().split())

    i = bisect_left(A_list, X)
    if i == N:
        res_list.append(str(X + Y - 1))
        continue

    first_gap = A_list[i] - X
    if Y <= first_gap:
        res_list.append(str(X + Y - 1))
        continue

    def miss(j):
        return A_list[j] - X - (j - i)

    l, r = i, N
    while l < r:
        m = (l + r) // 2
        if miss(m) >= Y:
            r = m
        else:
            l = m + 1
    j = l
    if j == N:
        res_list.append(str(X + Y - 1 + (N - i)))
        continue

    prev_miss = 0 if j == i else miss(j - 1)
    gap_start = X if j == i else A_list[j - 1] + 1
    offset = Y - prev_miss
    res = gap_start + offset - 1
    res_list.append(str(res))

for res in res_list:
    print(res)