import sys
sys.setrecursionlimit(10**7)

N, X, Y = map(int, input().split())
g_lists = [[] for _ in range(N+1)]
for _ in range(N-1):
    U, V = map(int, input().split())
    g_lists[U].append(V)
    g_lists[V].append(U)
