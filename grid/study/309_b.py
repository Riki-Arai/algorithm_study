n = int(input())
A = [input() for _ in range(n)]
for i in range(n):
    if i == 0:
        print(A[1][0] + A[0][: n - 1])
    elif i == n - 1:
        print(A[n - 1][1:n] + A[n - 2][n - 1])
    else:
        print(A[i + 1][0] + A[i][1 : n - 1] + A[i - 1][n - 1])
