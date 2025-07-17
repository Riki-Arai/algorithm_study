N, Q = map(int, input().split())

ans = 0
cnt = [0] + [1] * N
pos = list(range(N + 1))
for i in range(Q):
    query = list(map(int, input().split()))
    if query[0] == 1:
        P, H = query[1:]
        # 鳩 P は移動する前は巣 pos[P] にいる
        # 鳩 P が移動することで 巣 pos[P] にいる鳩の数が 2 から 1 に減る場合, ans を 1 減らす
        if cnt[pos[P]] == 2:
            ans -= 1
        # 巣 pos[P] の鳩の数を 1 減らす
        cnt[pos[P]] -= 1

        # 鳩 P がいる巣を H に変更する
        pos[P] = H
        # 巣 H の鳩の数を 1 増やす
        cnt[pos[P]] += 1
        # 鳩 P が移動することで 巣 H にいる鳩の数が 1 から 2 に増える場合，ans を 1 増やす
        if cnt[pos[P]] == 2:
            ans += 1
    else:
        print(ans)


## first
#N, Q = map(int, input().split())
#A_lists = [list(map(int, input().split())) for _ in range(Q)] # 取得例:[[1,2], [3,4]・・[9,10]]
#
#res = 0
#res_list = [1] * N
#pos_dic = {i+1: i for i in range(N)}
#for A_list in A_lists:
#    if A_list[0] == 2:
#        print(res)
#    else:
#        b_pos = pos_dic[A_list[1]]
#        n_pos = A_list[2] - 1
#        if res_list[b_pos] == 2:
#            if res - 1 >= 0:
#                res -= 1
#            else:
#                res = 0
#
#        if res_list[n_pos] == 1:
#            res += 1
#
#        res_list[b_pos] -= 1
#        res_list[n_pos] += 1
#        pos_dic[A_list[1]] = n_pos