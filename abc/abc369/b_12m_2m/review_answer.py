N = int(input())
A_lists = [input().split() for _ in range(N)] # 取得例:[[1,2], [3,4]・・[9,10]]

l_list = []
r_list = []
for A_list in A_lists:
    if A_list[1] == "L":
        l_list.append(int(A_list[0]))
    else:
        r_list.append(int(A_list[0]))

sum_l = sum([abs(l_list[i+1]-l_list[i]) for i in range(len(l_list)-1)])
sum_r = sum([abs(r_list[i+1]-r_list[i]) for i in range(len(r_list)-1)])
print(sum_l + sum_r)

##### 以下は最初
#N = int(input())
#A_lists = [input().split() for _ in range(N)] # 取得例:[[1,2], [3,4]・・[9,10]]
#
#res = 0
#r_list, l_list = [], []
#for A_list in A_lists:
#    A, S = int(A_list[0]), A_list[1]
#    if S == "R" and len(r_list) == 0:
#        r_list.append(A)
#    elif S == "L" and len(l_list) == 0:
#        l_list.append(A)
#    elif S == "R" and len(r_list) != 0:
#        res += abs(A-r_list[-1])
#        r_list.append(A)
#    elif S == "L" and len(l_list) != 0:
#        res += abs(A-l_list[-1])
#        l_list.append(A)
#
#print(res)