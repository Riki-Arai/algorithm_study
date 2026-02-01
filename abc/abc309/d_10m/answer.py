from collections import deque

N1, N2, M = map(int, input().split())

g_lists = [[]*(N1+N2+1) for _ in range(N1+N2+1)]
for _ in range(M):
    a, b = map(int, input().split())
    g_lists[a].append(b)
    g_lists[b].append(a)

dq = deque()
dq.append(1)
dq.append(N1+N2)
dis_list = [-1]*(N1+N2+1)
dis_list[1] = 0
dis_list[N1+N2] = 0
seen_set = set()
seen_set.add(1)
seen_set.add(N1+N2)
while len(dq):
    n = dq.popleft()
    dis = dis_list[n]
    for n_n in g_lists[n]:
        if n_n not in seen_set:
            dq.append(n_n)
            seen_set.add(n_n)
            dis_list[n_n] = dis + 1

print(max(dis_list[1:N1+1])+max(dis_list[N1+1:N1+N2+1])+1)