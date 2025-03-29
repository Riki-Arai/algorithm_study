import collections 

N, Q = map(int, input().split())
A_list = list(map(int, input().split())) # 取得例：[1, 2, 3]、1行の入力用

c_list = collections.Counter(A_list)
tmp = 0
for k in c_list:
    if c_list[k] % 2 != 0:
        tmp += 1

print(N-tmp)