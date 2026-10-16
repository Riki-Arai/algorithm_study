N = int(input()) # 取得例：1
A_list = list(map(int, input().split())) # 取得例：[1,2,3]、1行の入力用

res = 0
cur_i = 0
cum, max_cum = 0, 0
for a in A_list:
    max_cum = max(max_cum, cum+a)
    res = max(cur_i+max_cum, res)
    cum += a
    cur_i += cum

print(res)