N = int(input())
A_list = list(map(int, input().split())) # 取得例：[1, 2, 3]、1行の入力用
Q = int(input())
A_lists = [list(map(int, input().split())) for _ in range(Q)] # 取得例:[[1,2], [3,4]・・[9,10]]

for a in A_lists:
    pre_idx = A_list.index(a[0])
    post_idx = A_list.index(a[1])
    if pre_idx < post_idx: 
        print(A_list[pre_idx])
    else:
        print(A_list[post_idx])