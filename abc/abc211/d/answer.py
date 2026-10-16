N, M = map(int, input().split())

g_lists = [[] for _ in range(N+1)]
for _ in range(M):
    A, B = map(int, input().split())
    g_lists[A].append(B)
    g_lists[B].append(A)