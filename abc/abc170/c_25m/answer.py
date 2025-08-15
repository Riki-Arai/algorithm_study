X, N = map(int, input().split()) # 取得例：1 2
P_list = list(map(int, input().split())) # 取得例：[1,2,3]、1行の入力用

res = float("INF")
res_set = set(P_list)
for i in range(0, 200):
    if i not in res_set and abs(i-X) <= abs(res-X):
        if abs(i-X) == abs(res-X):
            res = min(i, res)
        else:
            res = i

print(res)