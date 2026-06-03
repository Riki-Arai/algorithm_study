import sys; sys.setrecursionlimit(10**7)

N, M = map(int, input().split()) # 取得例：1 2

res_list = [0]*(M+1)
for _ in range(N):
    X_list = list(map(int, input().split())) # 取得例：[1,2,3]、1行の入力用
    for a in X_list[1:]:
        res_list[a] += 1

print(res_list.count(N))