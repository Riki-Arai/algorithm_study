import bisect as bi

N, T = map(int, input().split())
S = input().strip()
X_list = list(map(int, input().split())) # 取得例：[1, 2, 3]、1行の入力用

zero_r_list, zero_l_list, one_lists = [], [], []
for i in range(N):
    s = S[i]
    x = X_list[i]
    if s == "1":
        one_lists.append((x, x+T))
    else:
        zero_l_list.append(x-T)
        zero_r_list.append(x)

res = 0
zero_l_list.sort()
zero_r_list.sort()
for l, r in one_lists:
    b_r_i = bi.bisect_right(zero_r_list, l)
    b_l_i = bi.bisect_right(zero_l_list, r, b_r_i)
    res += max(b_l_i-b_r_i, 0)

print(res)