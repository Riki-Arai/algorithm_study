import sys; sys.setrecursionlimit(10**7)

N, M = map(int, input().split()) # 取得例：1 2

g_lists = [set() for _ in range(N+1)]
for _ in range(M):
    A, B = map(int, input().split()) # 取得例：1 2
    g_lists[A].add(B)
    g_lists[B].add(A)

res_list = []
for i in range(1, N+1):
    n = len(g_lists[i])
    r = N-n-1
    if r >= 3:
        res_list.append(r*(r-1)*(r-2)//6)
    else:
        res_list.append(0)

print(*res_list)