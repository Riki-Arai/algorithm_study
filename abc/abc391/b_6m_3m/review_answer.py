N, M = map(int, input().split())
S_lists = [list(input()) for _ in range(N)]
T_lists = [list(input()) for _ in range(M)]

for a in range(N-M+1):
    for b in range(N-M+1):
        res_flag = True
        for i in range(M):
            for j in range(M):
                if S_lists[a+i][b+j] != T_lists[i][j]:
                    res_flag = False
                    break

    if res_flag:
        print(a+1, b+1)
        exit()