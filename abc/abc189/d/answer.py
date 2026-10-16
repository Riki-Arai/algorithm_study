N = int(input()) # 数値

dp_lists = [[0, 0] for _ in range(N+1)]
dp_lists[0] = [1, 1]
for i in range(1, N+1):
    S = input().strip() # 文字列
    if S == "AND":
        dp_lists[i][0] = 2*dp_lists[i-1][0] + dp_lists[i-1][1]
        dp_lists[i][1] = dp_lists[i-1][1]
    else:
        dp_lists[i][0] = dp_lists[i-1][0]
        dp_lists[i][1] = dp_lists[i-1][0] + 2*dp_lists[i-1][1]

print(dp_lists[N][1])