A_lists = [list(map(int, input().split())) for _ in range(3)] # 取得例:[[1,2], [3,4]・・[9,10]]

ab = pow(abs(A_lists[0][0] - A_lists[1][0]), 2) + pow(abs(A_lists[0][1] - A_lists[1][1]), 2)
bc = pow(abs(A_lists[1][0] - A_lists[2][0]), 2) + pow(abs(A_lists[1][1] - A_lists[2][1]), 2)
ca = pow(abs(A_lists[0][0] - A_lists[2][0]), 2) + pow(abs(A_lists[0][1] - A_lists[2][1]), 2)

list_ = [ab, bc, ca]
max_line = max(list_)
list_.remove(max_line)

if max_line == sum(list_):
    print("Yes")
else:
    print("No")