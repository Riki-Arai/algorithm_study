N = int(input())
H_list = list(map(int, input().split()))

dp_list = [float("INF")]*N
dp_list[0] = 0
for i in range(1, N):
    if i == 1:
        dp_list[i] = dp_list[0] + abs(H_list[i]-H_list[i-1])
    else:
        dp_list[i] = min(dp_list[i-2]+abs(H_list[i]-H_list[i-2]), dp_list[i-1]+abs(H_list[i]-H_list[i-1]))

print(dp_list[N-1])
