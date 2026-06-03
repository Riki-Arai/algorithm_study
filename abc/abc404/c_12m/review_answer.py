from atcoder.dsu import DSU

N, M = map(int, input().split()) # 取得例：1 2
X_lists = [list(map(int, input().split())) for _ in range(M)] # 取得例:[[1,2], [3,4]・・[9,10]]

dsu = DSU(N)
grid_lists = [[] for _ in range(N+1)]
for a, b in X_lists:
    dsu.merge(a-1, b-1)
    grid_lists[a].append(b)
    grid_lists[b].append(a)

def check_all_two(list):
    for x in list:
        if x != 2:
            return False
    return True

if len(dsu.groups()) == 1 and check_all_two(map(len, grid_lists[1:])):
    print("Yes")
else:
    print("No")


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