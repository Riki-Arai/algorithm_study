from atcoder.dsu import DSU

N, M = map(int, input().split())

dsu = DSU(N)
g_lists = [[] for _ in range(N)]
for _ in range(M):
    A, B = map(int, input().split())
    g_lists[A-1].append(B-1)
    g_lists[B-1].append(A-1)
    dsu.merge(A-1, B-1)

res = 0
for g in dsu.groups():
    e = 0
    for n in g:
        e += len(g_lists[n])

    e //= 2
    res += len(g)*(len(g)-1)//2-e

print(res)