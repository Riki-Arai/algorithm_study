import sys; sys.setrecursionlimit(10**7)

N, M = map(int, input().split()) # 取得例：1 2

res_list = [0]*N
for i in range(M):
    res_list[i%N] += 1

for res in res_list:
    print(res)