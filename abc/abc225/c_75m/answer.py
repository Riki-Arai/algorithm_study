N, M = map(int, input().split())
A_lists = [list(map(int, input().split())) for _ in range(N)]

b_i, b_j = divmod(A_lists[0][0]-1, 7)
for i in range(N):
    for j in range(M):
        ii = i + b_i
        jj = j + b_j
        if A_lists[i][j] != 7*ii + jj + 1:
            print("No")
            exit()

print("Yes")