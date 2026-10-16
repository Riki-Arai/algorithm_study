import sys; sys.setrecursionlimit(10**7)

N = int(input()) # 数値：1
A_list = list(map(int, input().split())) # 取得例：[1,2,3]、1行の入力用

cum_list = [0]
for a in A_list:
    cum_list.append(cum_list[-1]^a)

1