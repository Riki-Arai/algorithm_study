N = int(input()) # 数値：1
H_list = list(map(int, input().split())) # 取得例：[1,2,3]、1行の入力用

res = 0
max_h = 0
for h in H_list:
    if max_h <= h:
        res += 1
        max_h = h

print(res)