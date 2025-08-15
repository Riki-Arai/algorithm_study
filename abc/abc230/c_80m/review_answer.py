N, A, B = map(int, input().split())
P, Q, R, S = map(int, input().split())

l_k, h_k = max(1-A, 1-B),  min(N-A, N-B)
ll_k, hh_k = max(1-A, B-N), min(N-A, B-1)

A -= 1
B -= 1
grid_lists = [["."]*(S-R+1) for _ in range(Q-P+1)]
for i in range(Q-P+1):
    for j in range(S-R+1):
        ki = (i + P-1) - A
        kj = (j + R-1) - B
        if ki == kj and l_k <= ki <= h_k:
            grid_lists[i][j] = "#"

        if ki == -1*kj and ll_k <= ki <= hh_k:
            grid_lists[i][j] = "#"

for grid_list in grid_lists:
    print("".join(grid_list))