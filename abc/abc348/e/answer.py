from collections import defaultdict, deque, Counter

N = int(input()) # 数値：1

g_lists = [[] for _ in range(N+1)]
e_list = [0]*(N+1)
for _ in range(N-1):
    A, B = map(int, input().split()) # 取得例：1 2
    g_lists[A].append(B)
    g_lists[B].append(A)
    e_list[A] += 1
    e_list[B] += 1

dq = deque()
seen_set = set()
for i in range(1, N+1):
    if e_list[i] == 1:
        seen_set.add(i)
        dq.append((i, 0))
        break

res = 0
C_list = list(map(int, input().split())) # 取得例：[1,2,3]、1行の入力用
while len(dq):
    a, dis = dq.popleft()
    for b in g_lists[a]:
        if b not in seen_set:
            res += C_list[b-1]*(dis+1)
            seen_set.add(b)
            dq.append((b, dis+1))

sum_c = sum(C_list)
dq = deque([i, 0, res])
e_list[i] = 0
while len(dq):
    a, dis, tmp_res = dq.popleft()
    for b in g_lists[a]:
        if e_list[b]-1 == 1:
            tmp_res += C_list[a-1]
            tmp_res -= sum_c
            seen_set.add(b)
            dq.append((b, dis+1))

        e_list[b] -= 1