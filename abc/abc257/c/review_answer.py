from collections import defaultdict

N = int(input())
S = input()
W_list = list(map(int, input().split()))

sum = 0
res = 0
s_list = list(S)
x_lists = []
for i in range(N):
    x_lists.append((W_list[i], int(s_list[i])))
    if int(s_list[i]):
        sum += 1
        res += 1

x_lists.sort()
x_dict = defaultdict(int)
for k, v in x_lists:
    if v == 0:
        x_dict[k] += 1
    else:
        x_dict[k] -= 1

for v in x_dict.values():
    sum += v
    res = max(res, sum)

print(res)