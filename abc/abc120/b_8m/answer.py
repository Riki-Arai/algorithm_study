import sys; sys.setrecursionlimit(10**7)

A, B, K = map(int, input().split()) # 取得例：1 2

res_list = []
for i in range(1, min(A, B)+1):
    if A%i == 0 and B%i == 0:
        res_list.append(i)

print(res_list[::-1][K-1])