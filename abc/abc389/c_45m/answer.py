Q = int(input())
A_lists = [list(map(int, input().split())) for _ in range(Q)] # 取得例:[[1,2], [3,4]・・[9,10]]

snake_tall = 0
head_idx, tail_idx = 0, 0
head_list, tail_list = [], []
for A_list in A_lists:
    if A_list[0] == 2:
        snake_tall += tail_list[tail_idx]
        tail_idx += 1
        head_idx += 1
    elif A_list[0] == 3:
        print(head_list[head_idx+A_list[1]-1] - snake_tall)
    else:
        if len(head_list) == 0:
            head_list.append(0)
            tail_list.append(A_list[1])
        else:
            head_list.append(tail_list[-1]+head_list[-1])
            tail_list.append(A_list[1])