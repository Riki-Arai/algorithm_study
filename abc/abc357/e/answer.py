from collections import deque
from atcoder.dsu import DSU

N = int(input()) # 数値：1
A_list = list(map(int, input().split())) # 取得例：[1,2,3]、1行の入力用

g_lists = [[] for _ in range(N+1)]
rev_g_lists = [[] for _ in range(N+1)]
dsu = DSU(N+1)
for i, a in enumerate(A_list, 1):
    g_lists[i].append(a)
    rev_g_lists[a].append(i)
    dsu.merge(i, a)

res = 0
dis_list = [0]*(N+1)
for g_list in dsu.groups()[1:]:
    if len(g_list) >= 2:
        dq = deque()
        seen_set = set()
        a = g_list[0]
        while True:
            if a in seen_set:
                break
            dq.append(a)
            seen_set.add(a)
            a = g_lists[a][0]

        cir_dq = deque()
        cir_set = set()
        seen_set = set()
        while True:
            b = dq.pop()
            cir_set.add(b)
            cir_dq.append(b)
            seen_set.add(b)
            if a == b:
                break

        dis_set = set()
        res += len(cir_set)**2
        while len(cir_dq):
            a = cir_dq.popleft()
            for b in rev_g_lists[a]:
                if b in cir_set:
                    continue

                dq = deque([(b, 1)])
                while len(dq):
                    b, dis = dq.popleft()
                    dis_list[b] = dis
                    dis_set.add(b)
                    for c in rev_g_lists[b]:
                        if c not in seen_set:
                            seen_set.add(c)
                            dq.append((c, dis+1))

    else:
        res += 1

rev_g_lists
for i, d in enumerate(dis_list[1:], 1):
    if i in dis_set:
        res += d+len(cir_set)

print(res)