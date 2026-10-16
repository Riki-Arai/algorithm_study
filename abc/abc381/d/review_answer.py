from collections import deque

N = int(input())
A_list = list(map(int, input().split()))

res = 0
for i in range(2):
    tmp_res = 0
    dq = deque()
    seen_set = set()
    for j in range(i, N-1, 2):
        a, aa = A_list[j], A_list[j+1]
        if a != aa:
            seen_set.clear()
            dq.clear()
            tmp_res = 0
            continue

        while len(dq) and a in seen_set:
            seen_set.discard(dq.popleft())
            tmp_res -= 2

        tmp_res += 2
        seen_set.add(a)
        dq.append(a)
        res = max(tmp_res, res)

print(res)