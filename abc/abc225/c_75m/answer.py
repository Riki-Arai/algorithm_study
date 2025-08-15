N, M = map(int, input().split())
A_lists = [list(map(int, input().split())) for _ in range(N)]

m, r = divmod(A_lists[0][0], 7)
for i in range(N):
    for j in range(M):
        if ((m+i)*7 + j+r) != A_lists[i][j]:
            print("No")
            exit()

        if not 0 <= (A_lists[i][j]-1)//7 < 10**100:
            print("No")
            exit()

print("Yes")