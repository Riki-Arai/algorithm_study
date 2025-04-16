A_list = list(map(int, input().split()))
if len(set(A_list)) == 2:
    res_list = list(set([1, 2, 3]) - set(A_list))
    print(res_list[0])
else:
    print(-1)