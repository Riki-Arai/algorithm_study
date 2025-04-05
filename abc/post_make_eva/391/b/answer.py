N, M = map(int, input().split())
S_list = [list(input()) for _ in range(N)]
T_list = [list(input()) for _ in range(M)]

for i in range(N):
    for j in range(N):
        count = 0
        for k in range(M):
            for l in range(M):
                 if i + k < N and j + l < N and S_list[i+k][j+l] == T_list[k][l]:
                    count += 1
            if count == M * 2:
                print(i+1, j+1)
                exit()