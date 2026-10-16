'''
(1) 最初は出次数が多い順に距離がdのところにTrueをすることを考えたが、後の処理でFalseになる可能性もあるのでうまくいかず
(2) 作図を通じてpからd未満の頂点は全てFalseになる性質がわかったので、それらを予めFalseにすればいいのではないか？
(3) (2)の処理でTrueだったもので距離がdのものが1個以上あるかを確認し、そこで問題がなければ良い
'''
from collections import deque

N, M = map(int, input().split()) # 取得例：1 2

g_lists = [[] for _ in range(N+1)]
for _ in range(M):
    u, v = map(int, input().split()) # 取得例：1 2
    g_lists[u].append(v)
    g_lists[v].append(u)

dq_lists = []
K = int(input().strip())
for _ in range(K):
    p, d = map(int, input().split()) # 取得例：1 2
    dq_lists.append((-d, p))

dq_lists.sort()
res_list = [True]*(N+1)
dis_lists = [[-float("INF")]*(N+1) for _ in range(N+1)]
for dq_list in dq_lists:
    dq = deque([(dq_list[0]*-1, dq_list[1], 0)])
    seen_set = set([dq_list[1]])
    dis_lists[dq_list[1]][dq_list[1]] = 0
    while len(dq):
        l_d, u, dis = dq.popleft()
        if dis < l_d:
            res_list[u] = False
        for v in g_lists[u]:
            if v not in seen_set:
                dis_lists[dq_list[1]][v] = dis+1
            if v not in seen_set and dis+1 < l_d:
                seen_set.add(v)
                dq.append([l_d, v, dis+1])

for dq_list in dq_lists:
    l_d, u = dq_list
    l_d *= -1
    for i, dis in enumerate(dis_lists[u][1:], 1):
        if dis == l_d and res_list[i]:
            break
    else:
        print("No")
        exit()

s_list = []
for res in res_list[1:]:
    if res:
        s_list.append("1")
    else:
        s_list.append("0")
print("Yes")
print("".join(s_list))