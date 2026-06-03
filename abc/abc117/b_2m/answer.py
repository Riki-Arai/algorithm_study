import sys; sys.setrecursionlimit(10**7)

N = int(input()) # 数値：1
L_list = list(map(int, input().split())) # 取得例：[1,2,3]、1行の入力用

max_l = max(L_list)
L_list.remove(max_l)
total = sum(L_list)
if max_l < total:
    print("Yes")
else:
    print("No")