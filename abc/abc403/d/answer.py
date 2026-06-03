from atcoder.dsu import DSU

N, D = map(int, input().split()) # 取得例：1 2
A_list = list(map(int, input().split())) # 取得例：[1,2,3]、1行の入力用

a2n_list = [0]*(10**6+1)
dsu = DSU(10**6+1)
a_set = set(A_list)
for a in A_list:
    if a+D in a_set:
        dsu.merge(a, a+D)
    elif a-D in a_set:
        dsu.merge(a, a-D)
    a2n_list[a] += 1

res = 0
for g_list in dsu.groups():
    if len(g_list) >= 3:
        for a in g_list[1:-1]:
            res += a2n_list[a]
    elif len(g_list) == 2:
        res += min(a2n_list[g_list[0]], a2n_list[g_list[1]])

print(res)