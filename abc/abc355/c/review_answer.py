N, T = map(int, input().split())
A = list(map(lambda x: int(x)-1, input().split())) # -1をすることで後の処理でずらすことをなくす
row = [0] * N
col = [0] * N
diag = [0] * 2

for i in range(T):
    x = A[i] // N
    y = A[i] % N

    row[x] += 1
    if row[x] == N:
        print(i + 1)
        exit()

    col[y] += 1
    if col[y] == N:
        print(i + 1)
        exit()

    if x == y:
        diag[0] += 1
        if diag[0] == N:
            print(i + 1)
            exit()

    if x + y == N - 1: # 逆のななめはx+yが一定という性質を持つ
        diag[1] += 1
        if diag[1] == N:
            print(i + 1)
            exit()

print(-1)