import sys; sys.setrecursionlimit(10**7)

N, M = map(int, input().split()) # 取得例：1 2

grid_lists = [[] for _ in range(N+1)]
for _ in range(M):
    A, B = map(int, input().split()) # 取得例：1 2
    grid_lists[A].append(B)

seen_set = set()
def dfs(a):
    for b in grid_lists[a]:
        if b not in seen_set:
            seen_set.add(b)
            dfs(b)

seen_set.add(1)
dfs(1)
print(len(seen_set))