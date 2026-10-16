import sys
from collections import defaultdict
sys.setrecursionlimit(10**7)


N = int(input()) # 数値：1
A_list = list(map(int, input().split())) # 取得例：[1,2,3]、1行の入力用

g_lists = [[] for _ in range(N+1)]
for _ in range(N-1):
    U, V = map(int, input().split()) # 取得例：1 2
    g_lists[U].append(V)
    g_lists[V].append(U)

seen_set = set()
dup_set = set()
n2c_dict = defaultdict(int)
res_list = [False]*(N+1)
res_flag = False
def dfs(u):
    global res_flag
    res_list[u] = res_flag
    for v in g_lists[u]:
        if v not in seen_set:
            seen_set.add(v)
            if n2c_dict[A_list[v-1]]+1 == 2:
                dup_set.add(A_list[v-1])
                res_flag = True
            n2c_dict[A_list[v-1]] += 1
            dfs(v)
            if n2c_dict[A_list[v-1]]-1 == 1:
                dup_set.discard(A_list[v-1])
                if len(dup_set) == 0:
                    res_flag = False
            n2c_dict[A_list[v-1]] -= 1

n2c_dict[A_list[0]] += 1
seen_set.add(1)
dfs(1)
for k in range(1, N+1):
    if res_list[k]:
        print("Yes")
    else:
        print("No")