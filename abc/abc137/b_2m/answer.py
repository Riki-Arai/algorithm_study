K, X = map(int, input().split()) # 取得例：1 2

res_list = []
for i in range(-K+1, K, 1):
    res_list.append(X+i)

print(*res_list)