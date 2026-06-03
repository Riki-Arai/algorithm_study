import bisect as bi

N = int(input())
X_list = list(map(int, input().split())) # 取得例：[1, 2, 3]、1行の入力用
P_list = list(map(int, input().split())) # 取得例：[1, 2, 3]、1行の入力用

cum_list = [0]
for p in P_list:
    cum_list.append(cum_list[-1]+p)

Q = int(input())
for _ in range(Q):
    L, R = map(int, input().split())
    b_l = bi.bisect_left(X_list, L)
    b_r = bi.bisect_right(X_list, R)
    print(cum_list[b_r]-cum_list[b_l])