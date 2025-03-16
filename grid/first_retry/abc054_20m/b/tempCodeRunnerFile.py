N, M = map(int, input().split())
A_list = [list(input()) for _ in range(N)]
B_list = [list(input()) for _ in range(M)]

for i in range(N):
    count = 0
    for j in range(N):
        for k in range(M):
            for l in range(M):
                if i + k < N and j + l < N and A_list[i+k][j+l] == B_list[k][l]:
                    count += 1

    if count == M*2:
        print("Yes")
        exit()