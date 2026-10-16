import sys; sys.setrecursionlimit(10**7)

N, M = map(int, input().split()) # 取得例：1 2
A_list = list(map(int, input().split())) # 取得例：[1,2,3]、1行の入力用
B_list = list(map(int, input().split())) # 取得例：[1,2,3]、1行の入力用

tmp_a_list = A_list.copy()
res = float("INF")
count = 0
for i in range(N-1):
    pre_a, a = tmp_a_list[i], tmp_a_list[i+1]
    if (pre_a+a)%M != B_list[i]:
        count += 1
        tmp_a_list[i+1] ^= 1
res = min(count, res)

tmp_a_list = A_list.copy()
tmp_a_list[0] ^= 1
count = 1
for i in range(N-1):
    pre_a, a = tmp_a_list[i], tmp_a_list[i+1]
    if (pre_a+a)%M != B_list[i]:
        count += 1
        tmp_a_list[i+1] ^= 1

print(min(count, res))