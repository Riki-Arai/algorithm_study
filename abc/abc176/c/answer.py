N = int(input()) # 取得例：1
A_list = list(map(int, input().split())) # 取得例：[1,2,3]、1行の入力用

max_v = 0
res = 0
for a in A_list:
    if max_v > a:
        res += max_v - a
    max_v = max(a, max_v)

print(res)