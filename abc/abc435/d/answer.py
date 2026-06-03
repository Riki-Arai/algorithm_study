N, M = map(int, input().split()) # 取得例：1 2

g_lists = [[] for _ in range(N+1)]
for _ in range(M):
    X, Y = map(int, input().split()) # 取得例：1 2
    g_lists[X].append(Y)

seen_set = set()
def dfs(u):
    for v in g_lists[u]:
        if v not in seen_set:
            seen_set.add(v)
            dfs(v)

Q = int(input().strip())
for _ in range(Q):
    q, v = map(int, input().split()) # 取得例：1 2
    if q == 1:
        seen_set.add(v)
        dfs(v)
        1
    else:
        if v in seen_set:
            print("Yes")
        else:
            print("No")