from collections import deque

N, W = map(int, input().split())

b_lists = [deque() for _ in range(W+1)]
Z_lists = []
for i in range(1, N+1):
    X, Y = map(int, input().split())
    Z_lists.append((Y, X, i))

res_list = [float("INF")]*(N+1)
count = 0
Z_lists.sort()
for y, x, i in Z_lists:
    if len(b_lists[x]) == 0:
        count += 1
    b_lists[x].append(i)
    if count == W:
        max_y = 0
        ii_list = []
        for q in b_lists[1:]:
            ii = q.popleft()
            if len(q) == 0:
                count -= 1
            res_list[ii] = y

Q = int(input().strip())
for i in range(Q):
    T, A = map(int, input().split())
    if res_list[A] > T:
        print("Yes")
    else:
        print("No")