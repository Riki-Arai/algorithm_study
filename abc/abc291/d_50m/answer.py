N = int(input())
card_lists = [list(map(int, input().split())) for _ in range(N)]

dp_lists = [[0, 0] for _ in range(N*1)]
dp_lists[0][0] = 1
dp_lists[0][1] = 1
for i in range(1, N):
    for j in range(2):
        x = card_lists[i][j]
        for k in range(2):
            y = card_lists[i-1][k]
            if x != y:
                dp_lists[i][j] = (dp_lists[i][j] + dp_lists[i-1][k])% 998244353

print(sum(dp_lists[N-1])% 998244353)