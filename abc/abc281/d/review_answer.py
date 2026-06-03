N, K, D = map(int, input().split())
A_list = map(int, input().split())

dp_lists = [[-1]*D for _ in range(K+1)]
dp_lists[0][0] = 0
for a in A_list:
    r = a % D
    for i in range(K, 0, -1):
        for j in range(D-1, -1, -1):
            if dp_lists[i-1][(j-r)%D] >= 0:
                dp_lists[i][j] = max(dp_lists[i-1][(j-r)%D]+a, dp_lists[i][j])

print(dp_lists[K][0])