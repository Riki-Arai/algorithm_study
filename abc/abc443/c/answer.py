import bisect as bi

N, T = map(int, input().split()) # 取得例：1 2
A_list = list(map(int, input().split())) # 取得例：[1,2,3]、1行の入力用

res = 0
t = 0
while True:
    b_i = bi.bisect_left(A_list, t)
    if b_i == N:
        break
    a_t = A_list[b_i]
    if a_t >= t:
        res += a_t-t
        t = a_t+100

if t <= T:
    res += T-t

print(res)