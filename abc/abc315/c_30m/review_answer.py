# 味をソートして一番味が大きいものを選択し、2番目以降はmaxを利用しながらふさわしいものを選べば良いだけの問題
# しかし最初は2番目or3番目のアイスから味が最大化するものを選ぼうとしてしまっていたために誤答を多発
# 手動で選択する場合だと特に考慮漏れが発生しやすくなると思うので、まずは自動で味を最大化する方法を考えるべきだった
N = int(input())
A_lists = [list(map(int, input().split())) for _ in range(N)] # 取得例:[[1,2], [3,4]・・[9,10]]

res = 0
A_lists.sort(key=lambda x: x[1], reverse=True)
# 味がとにかく最大のものを1番目に愚直に選んで問題なし
f_f, f_s = A_lists[0][0], A_lists[0][1]
# 2番目以降は探索してふさわしいものを選べば良い
for i in range(1, N):
    s_f, s_s = A_lists[i][0], A_lists[i][1]
    if f_f == s_f:
        res = max(f_s + s_s//2, res)
    else:
        res = max(f_s + s_s, res)

print(res)


## first
#N = int(input())
#A_lists = [list(map(int, input().split())) for _ in range(N)] # 取得例:[[1,2], [3,4]・・[9,10]]
#
#A_lists.sort(key=lambda x: x[1], reverse=True)
#f_f, f_s = A_lists[0][0], A_lists[0][1]
#s_f, s_s = A_lists[1][0], A_lists[1][1]
#if N == 2:
#    if f_f == s_f:
#        print(f_s + s_s//2)
#    else:
#        print(f_s + s_s)
#    exit()
#
#if s_f == f_f:
#    res = f_s + s_s//2
#    for i in range(2, N):
#        t_f, t_s = A_lists[i][0], A_lists[i][1]
#        if t_f == f_f:
#            res = max(f_s + t_s//2, res)
#        else:
#            res = max(f_s + t_s, res)
#    print(res)
#else:
#    print(f_s + s_s)