N = int(input())
A_list = list(map(int, input().split()))
W_list = list(map(int, input().split()))

res = 0
n_list = [float("INF")] * N
for i in range(N):
    idx = A_list[i] - 1
    if n_list[idx] == float("INF"):
        n_list[idx] = W_list[i]
    else:
        if W_list[i] > n_list[idx]:
            res += n_list[idx]
            n_list[idx] = W_list[i]
        else:
            res += W_list[i]

print(res)