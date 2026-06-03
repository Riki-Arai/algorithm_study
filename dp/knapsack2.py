N, W = map(int, input().split())
x_lists = [list(map(int, input().split())) for _ in range(N)]

v_inf = 10**5
dp_list = [float("INF")]*(v_inf+1)
dp_list[0] = 0
for w, v in x_lists:
    for i in range(v_inf, v-1, -1):
        if dp_list[i-v] != float("INF") and dp_list[i-v]+w <= W:
            dp_list[i] = min(dp_list[i-v]+w, dp_list[i])

res = 0
for i in range(v_inf+1):
    if dp_list[i] != float("INF"):
        res = i

print(res)
