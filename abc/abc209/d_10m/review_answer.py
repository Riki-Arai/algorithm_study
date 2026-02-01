from collections import defaultdict, deque

N, Q = map(int, input().split())

g_lists = [[] for _ in range(N+1)]
for _ in range(N-1):
    a, b = map(int, input().split())
    g_lists[a].append(b)
    g_lists[b].append(a)

dis_list = [0]*(N+1)
seen_set = set()
dq = deque()
dq.append(1)
seen_set.add(1)
while len(dq):
    a = dq.popleft()
    dis = dis_list[a]
    for b in g_lists[a]:
        if b not in seen_set:
            dq.append(b)
            dis_list[b] = dis+1
            seen_set.add(b)

for _ in range(Q):
    c, d = map(int, input().split())
    c_dis = dis_list[c]
    d_dis = dis_list[d]
    if abs(c_dis-d_dis)%2 == 0:
        print("Town")
    else:
        print("Road")