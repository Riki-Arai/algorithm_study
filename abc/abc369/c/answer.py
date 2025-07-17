from collections import deque

N = int(input().strip())
A_list = list(map(int, input().split()))

res = 0
dq = deque()
for a in A_list:
    dq.append(a)
    while len(dq) >= 3 and (dq[-1]+dq[-3]) != 2*dq[-2]:
        dq.popleft()

    res += len(dq)

print(res)