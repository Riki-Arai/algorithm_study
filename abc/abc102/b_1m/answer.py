import sys; sys.setrecursionlimit(10**7)

N = int(input()) # 数値：1
A_list = list(map(int, input().split())) # 取得例：[1,2,3]、1行の入力用

res = 0
for i in range(N):
    for j in range(i+1, N):
        res = max(abs(A_list[i]-A_list[j]), res)

print(res)