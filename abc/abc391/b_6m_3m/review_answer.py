N, M = map(int, input().split())
S_lists = [list(input()) for _ in range(N)]
T_lists = [list(input()) for _ in range(M)]

for a in range(N-M+1):
    for b in range(N-M+1):
        res = 0
        for i in range(M):
            for j in range(M):
                # 問題文では1-baseの条件でコードは0-baseであるため、インデックスを直す必要がある
                if S_lists[a+i][b+j] == T_lists[i][j]:
                    res += 1

        if res == M*M:
            print(a+1, b+1)
            exit()