N = int(input())
A_list = list(map(int, input().split())) # 取得例：[1, 2, 3]、1行の入力用
Q = int(input())

replace_n = None
replace_set = None
for _ in range(Q):
    Q_list = list(map(int, input().split())) # 取得例：[1, 2, 3]、1行の入力用
    if Q_list[0] == 1:
        _, x = Q_list
        replace_n = x
        replace_set = set()
    elif Q_list[0] == 2:
        _, i, x = Q_list
        i -= 1
        if replace_set == None:
            A_list[i] += x
        else:
            if i in replace_set:
                A_list[i] += x
            else:
                replace_set.add(i)
                A_list[i] = replace_n
                A_list[i] += x
    else:
        _, i = Q_list
        i -= 1
        if replace_set == None:
            print(A_list[i])
        else:
            if i in replace_set:
                print(A_list[i])
            else:
                replace_set.add(i)
                A_list[i] = replace_n
                print(A_list[i])