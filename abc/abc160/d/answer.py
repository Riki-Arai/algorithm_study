import itertools as it

N, X, Y = map(int, input().split()) # 取得例：1 2

res_list = [0]*N
for i, j in it.combinations([i for i in range(1, N+1)], 2):
    if j <= X or Y <= i:
        res_list[j-i] += 1
    else:
        min_k = min(j-i, abs(X-i)+abs(Y-j)+1)
        res_list[min_k] += 1

for res in res_list[1:]:
    print(res)