N, K, X = map(int, input().split())
a_list = list(input().split())

res_list = a_list[:K] + [str(X)] + a_list[K:]
print(*res_list)
