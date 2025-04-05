N, M = map(int, input().split())
S_list = [list(input()) for _ in range(N)]
T_list = [list(input()) for _ in range(M)]

for a in range(N - M + 1):
    for b in range(N - M + 1):
        count = 0
        for i in range(M):
            for j in range(M):
                # Sa+i−1,b+j−1を0baseに写像するとSa+i+1,b+j+1となる。コード用にするときは-1するのでSa+i,b+jとなる。
                if a + i < N and b + j < N and S_list[a+i][b+j] == T_list[i][j]:
                    count += 1
        if count == M * M:
            print(a, b)
            exit()