N, A, B = map(int, input().split())
P, Q, R, S = map(int, input().split())

l_k, h_k = max(1-A, 1-B),  min(N-A, N-B)
ll_k, hh_k = max(1-A, B-N), min(N-A, B-1)

A -= 1
B -= 1
P -= 1
R -= 1
grid_lists = [["."]*(S-R) for _ in range(Q-P)]
for i in range(Q-P):
    for j in range(S-R):
        ii = i + P
        jj = j + R
        if ii-A == jj-B:
            grid_lists[i][j] = "#"

        if A-ii == (jj-B):
            grid_lists[i][j] = "#"

for grid_list in grid_lists:
    print("".join(grid_list))