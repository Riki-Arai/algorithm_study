N = int(input())
X_lists = [list(map(int, input().split())) for _ in range(N)] # 取得例:[[1,2], [3,4]・・[9,10]]

dp_lists = [[0]*(N+1) for _ in range(N+1)]
for i, x_list in enumerate(X_lists, 1):
    a, b = x_list
    for x in range(a, b+1):
        dp_lists[i] = dp_lists[i-1] + dp_lists[]