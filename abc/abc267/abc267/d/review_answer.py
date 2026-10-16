N, M = map(int, input().split())
A_list = list(map(int, input().split()))

dp_list = [-float("INF")]*M
dp_list[0] = A_list[0]
for i in range(1, N):
    for j in range(M-1, -1, -1):
        if j == 0:
            dp_list[j] = max(dp_list[j], A_list[i])
        else:
            dp_list[j] = max((j+1)*A_list[i]+dp_list[j-1], dp_list[j])

print(dp_list[-1])

#N, M = map(int, input().split())
#A = list(map(int, input().split()))
#
#dp = [-float("inf")] * (M + 1)
#dp[0] = 0
#for a in A:
#    for j in range(M, 0, -1):
#        dp[j] = max(dp[j], dp[j-1] + j * a)
#
#print(dp[M])