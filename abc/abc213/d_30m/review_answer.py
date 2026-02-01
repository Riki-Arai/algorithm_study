import sys
from sortedcontainers import SortedList
sys.setrecursionlimit(10**7)

N = int(input())

g_lists = [SortedList()*(N+1) for _ in range(N+1)]
for _ in range(N-1):
    A, B = map(int, input().split())
    g_lists[A].add(B)
    g_lists[B].add(A)

res_list = []
seen_set = set()
def dfs(n):
    res_list.append(n)
    seen_set.add(n)
    for g in g_lists[n]:
        if g not in seen_set:
            dfs(g)
            # 末端である場合はseen_setによって弾かれているので、特にif文を追加せずにappendをすればいい
            res_list.append(n)

dfs(1)
print(*res_list)