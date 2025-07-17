N, L, R = map(int, input().split())

res_list = [i for i in range(1, N+1)]
print(res_list[:L-1] + res_list[L-1:R][::-1] + res_list[R:])