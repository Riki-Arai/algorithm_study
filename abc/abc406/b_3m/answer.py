N, K = map(int, input().split()) # 取得例：1 2
A_list = list(map(int, input().split())) # 取得例：[1,2,3]、1行の入力用

res = 1
for a in A_list:
    res = res*a
    if len(str(res)) > K:
        res = 1

print(res)