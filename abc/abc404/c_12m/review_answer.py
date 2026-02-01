import sys
sys.setrecursionlimit(10**7)

N, M = map(int, input().split()) # 取得例：1 2
X_lists = [list(map(int, input().split())) for _ in range(M)] # 取得例:[[1,2], [3,4]・・[9,10]]

g_lists = [[]*(N+1) for _ in range(N+1)]
for a, b in X_lists:
    g_lists[a].append(b)
    g_lists[b].append(a)

for g_list in g_lists[1:]:
    if len(g_list) != 2:
        print("No")
        exit()

seen_set = set()
def dfs(n):
    if n in seen_set:
        return
    seen_set.add(n)
    for nn in g_lists[n]:
        dfs(nn)

dfs(1)
if len(seen_set) == N:
    print("Yes")
else:
    print("No")