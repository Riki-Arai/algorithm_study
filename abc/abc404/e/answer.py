import sys

sys.setrecursionlimit(10**7)

N = int(input())
C = [0] + list(map(int, input().split()))
A = [0] + list(map(int, input().split()))

graph = [[] for _ in range(N)]

for i in range(1, N):
    for j in range(i - C[i], i):
        graph[i].append(j)

    for j in range(min(i + 1, N - 1), min(i + C[i] + 1, N)):
        graph[i].append(j)

total = sum(A)
 
ans = float("inf")
visited = [False] * N
def dfs(v, dist, beans):
    global ans

    if beans == total:
        ans = min(ans, dist)
        return

    for nv in graph[v]:
        if visited[nv]:
            continue

        visited[nv] = True

        dfs(
            nv,
            dist + 1,
            beans + A[nv]
        )

        visited[nv] = False


visited[0] = True
dfs(0, 0, A[0])

print(ans)