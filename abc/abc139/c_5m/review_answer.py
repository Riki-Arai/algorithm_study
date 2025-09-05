N = int(input()) # 数値：1
H_list = list(map(int, input().split())) # 取得例：[1,2,3]、1行の入力用

res = 0
tmp_res = 0
base_h = H_list[0]
for h in H_list[1:]:
    if h <= base_h:
        tmp_res += 1
        base_h = h
    else:
        res = max(tmp_res, res)
        tmp_res = 0
        base_h = h

print(max(res, tmp_res))