import bisect as bi

N = int(input()) # 数値：1
A_list = list(map(int, input().split())) # 取得例：[1,2,3]、1行の入力用

c_r = 0
res_list = []
A_list.sort()
for i in range(1, max(A_list)+1):
    b_i = bi.bisect_left(A_list, i)
    if N-b_i+c_r >= 10:
        m, r = divmod((N-b_i+c_r), 10)
        res_list.append(str(r))
        c_r = m
    else:
        res_list.append(str(N-b_i+c_r))
        c_r = 0

if c_r != 0:
    res_list.append(str(c_r))

print("".join(res_list[::-1]))