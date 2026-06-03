import sys
sys.setrecursionlimit(10**7)

N = int(input()) # 数値：1
X_lists = [list(map(int, input().split())) for _ in range(N)] # 取得例:[[1,2], [3,4]・・[9,10]]

g_lists = [set() for _ in range(N+1)]
get_skill_list = []
for i, x_list in enumerate(X_lists, 1):
    a, b = x_list
    if (a, b) == (0, 0):
        get_skill_list.append(i)
    else:
        if a != i:
            g_lists[a].add(i)
        if b != i:
            g_lists[b].add(i)

skill_set = set()
def dfs(n):
    skill_set.add(n)
    for ss in g_lists[n]:
        if ss not in skill_set:
            dfs(ss)

for s in get_skill_list:
    dfs(s)

print(len(skill_set))