from collections import deque

N = int(input())
A_list = list(map(int, input().split()))

res = 0
for i in range(1, 3):
    dq = deque()
    seen_set = set()
    tmp_res = 0
    for j in range(i, N, 2):
        if A_list[j-1] != A_list[j]:
            seen_set.clear()
            dq.clear()
            tmp_res = 0
            continue
        a = A_list[j]
        tmp_res += 2
        while len(dq) and a in seen_set:
            seen_set.discard(dq.popleft())
            tmp_res += -2

        seen_set.add(a)
        dq.append(a)
        res = max(tmp_res, res)

print(res)