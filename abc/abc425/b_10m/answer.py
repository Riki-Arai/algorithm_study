from collections import deque

N = int(input()) # 数値：1
A_list = list(map(int, input().split())) # 取得例：[1,2,3]、1行の入力用

f_a_list = sorted(filter(lambda x: x!=-1, A_list))
f_a_set = set(f_a_list)
if len(f_a_list) != len(f_a_set):
    print("No")
    exit()

dq = deque()
for i in range(1, N+1):
    if i not in f_a_set:
        dq.append(i)

res_list = []
for a in A_list:
    if a == -1:
        res_list.append(dq.popleft())
    else:
        res_list.append(a)

print("Yes")
print(*res_list)