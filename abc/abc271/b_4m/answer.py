N, Q = map(int, input().split())
A_lists = [list(map(int, input().split())) for _ in range(N)]
S_lists = [list(map(int, input().split())) for _ in range(Q)] # 取得例:[[1,2], [3,4]・・[9,10]]

for S_list in S_lists:
    s, t = S_list
    print(A_lists[s-1][t])
