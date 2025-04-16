N = int(input())
A_list = list(map(int, input().split())) # 取得例：[1, 2, 3]、1行の入力用
Q = int(input())
Q_lists = [list(map(int, input().split())) for _ in range(Q)] # 取得例:[[1,2], [3,4]・・[9,10]]

for Q_list in Q_lists:
    if Q_list[0] == 1:
        A_list[Q_list[1]-1] = Q_list[2]
    elif Q_list[0] == 2:
        print(A_list[Q_list[1]-1])