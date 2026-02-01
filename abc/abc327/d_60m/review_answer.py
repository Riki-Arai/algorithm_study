from collections import deque

N, M = map(int, input().split())
A_list = list(map(int, input().split())) # 取得例：[1, 2, 3]、1行の入力用
B_list = list(map(int, input().split())) # 取得例：[1, 2, 3]、1行の入力用

n_list = []
n_set = set()
g_lists = [set() for _ in range(N+1)]
for i in range(M):
    a, b = A_list[i], B_list[i]
    g_lists[a].add(b)
    g_lists[b].add(a)

seen_set = set()
wb_list = [-1]*(N+1)
for n in range(1, N+1):
    if n in seen_set:
        continue
    dq = deque()
    dq.append(n)
    seen_set.add(n)
    wb_list[n] = 0
    dq.append(n)
    while len(dq):
        n = dq.popleft()
        for n_n in g_lists[n]:
            if n_n in seen_set:
                if wb_list[n] == wb_list[n_n]:
                    print("No")
                    exit()
            else:
                seen_set.add(n_n)
                wb_list[n_n] = wb_list[n]^1
                dq.append(n_n)

print("Yes")