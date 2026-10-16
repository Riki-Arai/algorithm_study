import sys; sys.setrecursionlimit(10**7)

N = int(input()) # 数値：1
A_list = list(map(int, input().split())) # 取得例：[1,2,3]、1行の入力用

res = 0
for i, a in enumerate(A_list, 1):
    if i == a:
        res += 1
    elif a-1 < N and i == A_list[a-1]:
        res += 1

print(res)