import bisect as bi

N = int(input())
A_list = list(map(int, input().split())) # 取得例：[1, 2, 3]、1行の入力用
Q = int(input())

sleep_list = []
for i in range(1, N-1, 2):
    sleep_list.append(A_list[i+1]-A_list[i])

cum_list = [0]
for s in sleep_list:
    cum_list.append(cum_list[-1]+s)

for _ in range(Q):
    l, r = map(int, input().split())

    bl_i = bi.bisect_right(A_list, l)
    br_i = bi.bisect_right(A_list, r)

    res = cum_list[br_i//2]-cum_list[bl_i//2]
    if bl_i > 0 and bl_i%2 == 0:
        res += A_list[bl_i]-l

    if br_i > 0 and br_i%2 == 0:
        res -= A_list[br_i]-r

    print(res)