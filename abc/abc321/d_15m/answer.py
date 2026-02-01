import bisect as bi

N, M, P = map(int, input().split())
A_list = sorted(list(map(int, input().split()))) # 取得例：[1, 2, 3]、1行の入力用
B_list = sorted(list(map(int, input().split()))) # 取得例：[1, 2, 3]、1行の入力用

cum_list = [0]
for b in B_list:
    cum_list.append(cum_list[-1]+b)

res = 0
for i in range(N):
    a = A_list[i]
    if P > a:
        diff = P - a
        b_i = bi.bisect_left(B_list, diff)
        res += a*b_i + cum_list[b_i]
        res += P*(M-b_i)
    else:
        res += P*M

print(res)