Q = int(input().strip())

res_list = []
for _ in range(Q):
    input_ = input().split()
    if input_[0] == "1":
        c = input_[1]
        if len(res_list):
            if c == "(":
                res_list.append(res_list[-1]+1)
            else:
                if res_list[-1]-1 >= 0:
                    res_list.append(res_list[-1]-1)
                else:
                    res_list.append(-float("INF"))
        else:
            if c == "(":
                res_list.append(1)
            else:
                res_list.append(-float("INF"))
    else:
        res_list.pop()

    if len(res_list) == 0:
        print("Yes")
    elif len(res_list) and res_list[-1] == 0:
        print("Yes")
    else:
        print("No")



#q = int(input().strip())
#
#x = [0]
#INF = 1001001001
#for _ in range(q):
#    type_ = input().strip().split()
#    if type_[0] == "1":
#        c = type_[1]
#        nx = x[-1] + (1 if c == '(' else -1)
#        if nx < 0:
#            nx = -INF
#        x.append(nx)
#    else:
#        x.pop()
#
#    if x[-1] == 0:
#        print("Yes")
#    else:
#        print("No")