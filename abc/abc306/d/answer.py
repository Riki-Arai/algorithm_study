N = int(input())

dp_lists = [[0, 0] for _ in range(N+1)]
for i in range(1, N+1):
    X, Y = map(int, input().split())
    if X == 0:
        dp_lists[i][0] = max(dp_lists[i-1][1]+Y, dp_lists[i-1][0]+Y, dp_lists[i-1][0])
        dp_lists[i][1] = dp_lists[i-1][1]
    else:
        dp_lists[i][0] = dp_lists[i-1][0]
        dp_lists[i][1] = max(dp_lists[i-1][0]+Y, dp_lists[i-1][1])

print(max(dp_lists[N]))