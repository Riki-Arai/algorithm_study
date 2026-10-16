from collections import deque

S = input().strip() # 取得例：A
N = int(input()) # 取得例：1

rev_flag = 0
dq = deque(list(S))
for _ in range(N):
    input_ = input() # 取得例：1
    if input_[0] == "1":
        rev_flag ^= 1
    else:
        _, F, C = input_.split()
        if rev_flag == 0:
            if F == "1":
                dq.appendleft(C)
            else:
                dq.append(C)
        else:
            if F == "1":
                dq.append(C)
            else:
                dq.appendleft(C)

res_list = []
if rev_flag == 0:
    while len(dq):
        res_list.append(dq.popleft())
else:
    while len(dq):
        res_list.append(dq.pop())

print("".join(res_list))