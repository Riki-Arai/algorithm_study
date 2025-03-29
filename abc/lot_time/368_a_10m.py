N, K = list(map(int, input().split()))
a_list = list(map(int, input().split()))
res_list = a_list[N - K:] + a_list[:N - K]
print(*res_list)
