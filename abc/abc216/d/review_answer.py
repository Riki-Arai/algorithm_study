from collections import defaultdict, Counter, deque

N, M = map(int, input().split())

a_lists = []
for _ in range(M):
    k = int(input().strip())
    a_list = list(map(int, input().split()))
    a_lists.append(a_list[::-1])

ball_set = set()
dq = deque([i for i in range(M)])
b2m_dict = defaultdict(int)
while len(dq) > 0:
    m = dq.popleft()
    if len(a_lists[m]) == 0:
        continue
    a = a_lists[m].pop()
    if a not in ball_set:
        b2m_dict[a] = m
        ball_set.add(a)
    else:
        dq.append(b2m_dict[a])
        dq.append(m)
        ball_set.discard(a)
        del b2m_dict[a]

if len(ball_set) == 0:
    print("Yes")
else:
    print("No")