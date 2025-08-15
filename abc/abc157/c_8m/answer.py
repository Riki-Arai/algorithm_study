N, M = map(int, input().split()) # 取得例：1 2
A_lists = [list(map(int, input().split())) for _ in range(M)] # 取得例:[[1,2], [3,4]・・[9,10]]

for i in range(1000):
    n = str(i)
    if len(n) == N:
        for s, c in A_lists:
            if n[s-1] != str(c):
                break
        else:
            print(n)
            exit()

print(-1)