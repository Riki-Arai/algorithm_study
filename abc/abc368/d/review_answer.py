from collections import deque

N, K = map(int, input().split())

g_lists = [[] for _ in range(N+1)]
e_list = [0]*(N+1)
for i in range(N-1):
    A, B = map(int, input().split())

    g_lists[A].append(B)
    g_lists[B].append(A)

    e_list[A] += 1
    e_list[B] += 1

V_list = list(map(int, input().split())) # 取得例：[1,2,3]、1行の入力用
v_set = set(V_list)

dq = deque()
for i, e in enumerate(e_list[1:], 1):
    if i not in v_set and e == 1:
        dq.append(i)

rem = N-len(v_set)
while len(dq):
    a = dq.popleft()
    e_list[a] -= 1
    if e_list[a] == 0:
        rem -= 1

    for b in g_lists[a]:
        e_list[b] -= 1
        if b not in v_set and e_list[b] == 1:
            dq.append(b)

print(len(v_set)+rem)



import sys
from collections import deque
sys.setrecursionlimit(10**7)

N, K = map(int, input().split())

g_lists = [[] for _ in range(N+1)]
for _ in range(N-1):
    A, B = map(int, input().split())
    g_lists[A].append(B)
    g_lists[B].append(A)

v_set = set(list(map(int, input().split())))
res_set = v_set.copy()
seen_set = set()
dq = deque()
def dfs(a):
    if a in seen_set:
        return
    seen_set.add(a)
    dq.append(a)
    for b in g_lists[a]:
        if b not in seen_set:
            if b in v_set:
                res_set.add(b)
                while len(dq):
                    v = dq.popleft()
                    res_set.add(v)
            dfs(b)

    if len(dq):
        dq.pop()


for a in v_set:
    dfs(a)

print(len(res_set))