from collections import deque

N, M, K = map(int, input().split()) # 取得例：1 2

g_lists = [[[], []] for _ in range(N+1)]
for _ in range(M):
    u, v, a = map(int, input().split()) # 取得例：1 2
    g_lists[u][a].append(v)
    g_lists[v][a].append(u)

res = float("INF")
s_set = set(list(map(int, input().split()))) # 取得例：[1,2,3]、1行の入力用
if 1 in s_set:
    seen_sets = set([(1, 0), (1, 1)])
    dq = deque([(1, 0, 1), (1, 0, 0)])
else:
    seen_sets = set([(1, 1)])
    dq = deque([(1, 0, 1)])

while len(dq):
    u, dis, p_flag = dq.popleft()
    if u == N:
        res = min(dis, res)

    for v in g_lists[u][p_flag]:
        if (v, p_flag) not in seen_sets:
            if v in s_set:
                dq.append((v, dis+1, p_flag^1))
                seen_sets.add((v, p_flag^1))

            dq.append((v, dis+1, p_flag))
            seen_sets.add((v, p_flag))

if res == float("INF"):
    print(-1)
else:
    print(res)