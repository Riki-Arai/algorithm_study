# r=0であれば切り上げで割った値を求めれば良い
# しかし今回はrが0ではないので、そこでrだけを左にずらしてしまって、あとでrだけ右にずらしてしまえば良い
N = int(input())
q_dict = {}
for i in range(1, N+1):
    q, r = map(int, input().split())
    q_dict[i] = (q, r)

Q = int(input())
for _ in range(Q):
    t, d = map(int, input().split())
    q, r = q_dict[t]
    print((((d-r)+(q-1))//q)*q + r)

#N = int(input())
#Q_lists = [list(map(int, input().split())) for _ in range(N)] # 取得例:[[1,2], [3,4]・・[9,10]]
#Q = int(input())
#T_lists = [list(map(int, input().split())) for _ in range(Q)] # 取得例:[[1,2], [3,4]・・[9,10]]
#
#for T_list in T_lists:
#    t, d = T_list
#    q, r = Q_lists[t-1]
#    if d % q == r:
#        print(d)
#    elif d < q:
#        if d < r:
#            print(r)
#        else:
#            print(q+r)
#    else:
#        if d % q < r:
#            print(d+r-(d%q))
#        else:
#            print((d//q+1)*q+r)