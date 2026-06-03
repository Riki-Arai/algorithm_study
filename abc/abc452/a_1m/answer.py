import sys; sys.setrecursionlimit(10**7)

M, D = map(int, input().split()) # 取得例：1 2

res_lists = [(1, 7), (3, 3), (5, 5), (7, 7), (9, 9)]
if (M, D) in res_lists:
    print("Yes")
else:
    print("No")