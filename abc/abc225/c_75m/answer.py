N, M = map(int, input().split())
A_lists = [list(map(int, input().split())) for _ in range(N)]

base_idx = ((A_lists[0][0]-1)//7, (A_lists[0][0]-1)%7)
for i in range(N):
    i_idx = base_idx[0] + i
    for j in range(M):
        j_idx = base_idx[1] + j
        if i_idx*7 + j_idx != A_lists[i][j]-1:
            print("No")
            exit()

        if not(i_idx*7 <= i_idx*7 + j_idx <= i_idx*7+6):
            print("No")
            exit()

print("Yes")