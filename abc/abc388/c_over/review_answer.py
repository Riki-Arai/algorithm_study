from bisect import bisect

N = int(input())
A_list = list(map(int, input().split())) # 取得例：[1, 2, 3]、1行の入力用

res = 0
for a in A_list:
    res += bisect(A_list, a // 2)

print(res)