from collections import deque

N, M = map(int, input().split()) # 取得例：1 2

g_lists = [[] for _ in range(N+1)]
e_list = [0]*(N+1)
for _ in range(M):
    x, y = map(int, input().split()) # 取得例：1 2
    g_lists[x].append(y)
    e_list[y] += 1

dq = deque()
seen_set = set()
for i in range(1, len(e_list)):
    if e_list[i] == 0:
        dq.append((i, 0))
        seen_set.add(i)

dp_list = [0]*(N+1)
while len(dq):
    x, d = dq.popleft()
    for y in g_lists[x]:
        e_list[y] -= 1
        dp_list[y] = max(d+1, dp_list[y])
        if e_list[y] == 0 and y not in seen_set:
            seen_set.add(y)
            dq.append((y, d+1))

print(max(dp_list))