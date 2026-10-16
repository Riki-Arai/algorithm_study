N, M = map(int, input().split())

A_list = list(map(int, input().split()))
C_list = list(map(int, input().split()))

A_list.reverse()
C_list.reverse()
res_list = []
for i in range(M+1):
    n = C_list[i] // A_list[0]
    res_list.append(n)
    for j in range(1, N+1):
        C_list[i+j] -= A_list[j] * n

print(*res_list[::-1])