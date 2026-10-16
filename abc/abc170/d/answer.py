from collections import defaultdict

N = int(input()) # 取得例：1
A_list = list(map(int, input().split())) # 取得例：[1,2,3]、1行の入力用

max_a = 10**6+1
n_list = [False]*max_a
n2c_dict = defaultdict(int)
for a in A_list:
    n_list[a] = True
    n2c_dict[a] += 1

for a in set(A_list):
    if n2c_dict[a] >= 2:
        n_list[a] = False
    for i in range(2*a, max_a, a):
        if n_list[i]:
            n_list[i] = False

print(sum(n_list))