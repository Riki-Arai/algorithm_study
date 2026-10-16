from sortedcontainers import SortedList

N, M, Q = map(int, input().split())
input_lists = [list(map(int, input().split())) for _ in range(N)] # 取得例:[[1,2], [3,4]・・[9,10]]
X_list = list(map(int, input().split())) # 取得例：[1,2,3]、1行の入力用

s_x_list = SortedList(X_list)
input_lists.sort(lambda x: x[1], reverse=True)
for _ in range(Q):
    L, R = map(int, input().split())
    cs_x_list = s_x_list.copy()
    for i in range(L-1, R):
        cs_x_list.remove(X_list[i])

    res = 0
    for w, v in input_lists:
        b_i = cs_x_list.bisect_left(w)
        if b_i != len(cs_x_list):
            res += v
            cs_x_list.remove(cs_x_list[b_i])

        if len(cs_x_list) == 0:
            break

    print(res)