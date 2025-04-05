N, K, A = map(int, input().split())

res_list = [i for i in range(1, N+1)]
for i in range(A-1, K+A-1):
    res = res_list[i%N]
print(res)