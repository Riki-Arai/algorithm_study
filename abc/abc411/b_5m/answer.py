N = int(input()) # 数値：1
D_list = list(map(int, input().split())) # 取得例：[1,2,3]、1行の入力用

cum_list = [0]
for d in D_list:
    cum_list.append(cum_list[-1]+d)

res_lists = []
cum_ = 0
for _ in range(N-1):
    cum_ = cum_list.pop(0)
    tmp_list = []
    for x in cum_list:
        tmp_list.append(x-cum_)

    res_lists.append(tmp_list)

for res_list in res_lists:
    print(*res_list)