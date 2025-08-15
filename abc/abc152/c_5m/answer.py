N = int(input()) # 取得例：1
P_list = list(map(int, input().split())) # 取得例：[1,2,3]、1行の入力用

res = 0
min_v = float("INF")
for p in P_list:
    if p <= min_v:
        res += 1
        min_v = p

print(res)