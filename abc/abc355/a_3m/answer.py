A, B = map(int, input().split())
res_list = [1, 2, 3]
if A != B:
    res_list.remove(A)
    res_list.remove(B)
    print(res_list[0])
else:
    print(-1)