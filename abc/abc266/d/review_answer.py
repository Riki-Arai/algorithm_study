N = int(input())

t_max = 10**5+1
t_max2 = 0
t_list = [[0, 0] for _ in range(t_max)]
for _ in range(N):
    T, X, A = map(int, input().split())
    t_list[T][0] = X
    t_list[T][1] = A
    t_max2 = max(T, t_max2)

dp_lists = [[-float("INF")]*5 for _ in range(t_max)]
dp_lists[0][0] = 0
for t in range(1, t_max):
    for j in range(5):
        dp_lists[t][j] = dp_lists[t-1][j]
        if j == 0:
            dp_lists[t][j] = max(dp_lists[t-1][j+1], dp_lists[t][j])
        elif j == 4:
            dp_lists[t][j] = max(dp_lists[t-1][j-1], dp_lists[t][j])
        else:
            dp_lists[t][j] = max(dp_lists[t-1][j+1], dp_lists[t-1][j-1], dp_lists[t][j])

    dp_lists[t][t_list[t][0]] += t_list[t][1]

print(max(dp_lists[t_max2]))