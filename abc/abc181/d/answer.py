import itertools as it

S = input().strip() # 取得例：A

if len(S) == 1:
    if S == "8":
        print("Yes")
    else:
        print("No")
elif len(S) == 2:
    for s_list in it.permutations(list(S)):
        if int("".join(s_list))%8 == 0:
            print("Yes")
            exit()
    print("No")
else:
    s_list = []
    n_list = [0]*10
    for s in S:
        if n_list[int(s)] < 4:
            n_list[int(s)] += 1
            s_list.append(s)
    for s_list in it.permutations(s_list, 3):
        if int("".join(s_list))%8 == 0:
            print("Yes")
            exit()
    print("No")