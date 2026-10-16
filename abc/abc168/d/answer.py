from collections import deque

N, M = map(int, input().split()) # 取得例：1 2
g_lists = [[] for _ in range(N+1)]
for _ in range(M):
    A, B = map(int, input().split()) # 取得例：1 2
    g_lists[A].append(B)
    g_lists[B].append(A)

seen_set = set()
res_list = [None]*(N+1)
dq = deque([1])
while len(dq):
    a = dq.popleft()
    for b in g_lists[a]:
        if b not in seen_set:
            res_list[b] = a
            seen_set.add(b)
            dq.append(b)

if res_list[2:].count(None) == 0:
    print("Yes")
    for res in res_list[2:]:
        print(res)
else:
    print("No")