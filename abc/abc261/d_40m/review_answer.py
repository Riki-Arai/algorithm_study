from collections import defaultdict

N, M = map(int, input().split())
X_list = list(map(int, input().split())) # 取得例：[1, 2, 3]、1行の入力用
c_dict = defaultdict(int)
for _ in range(M):
    C, Y = map(int, input().split())
    c_dict[C-1] = Y

INF = -10**18
dp_lists = [[INF]*(N+1) for _ in range(N+1)]
dp_lists[0][0] = 0
for i in range(1, N+1):
    for j in range(N, -1, -1):
        if dp_lists[i-1][j] != INF:
            dp_lists[i][j+1] = max(dp_lists[i-1][j]+X_list[i-1]+c_dict[j], dp_lists[i][j+1])

    for j in range(N, -1, -1):
        dp_lists[i][0] = max(dp_lists[i-1][j], dp_lists[i][0])

print(max(dp_lists[N]))