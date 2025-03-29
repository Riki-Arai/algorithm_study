N = int(input())
A_lists = [list("?" * N) for _ in range(N)]

for i in range(N):
    j = N - i
    # コードの場合においてはiが偶数の場合が「#」となる。
    if j >= i and i % 2 == 0:
        for k in range(i, j):
            for l in range(i, j):
                A_lists[k][l] = "#"

    elif j >= i and i % 2 != 0:
        for k in range(i, j):
            for l in range(i, j):
                A_lists[k][l] = "."

for a in A_lists:
    print("".join(a))