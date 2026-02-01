from collections import deque

atcoder = "atcoder"
S = input().strip()

que = deque()
dist = {}

que.append(S)
dist[S] = 0

while que:
    v = que.popleft()
    for i in range(len(atcoder) - 1):
        v2 = list(v)
        v2[i], v2[i + 1] = v2[i + 1], v2[i]
        v2 = ''.join(v2)
        if v2 not in dist:
            que.append(v2)
            dist[v2] = dist[v] + 1

print(dist[atcoder])

## first
#S = input().strip()
#
#res = 0
#S_list = list(S)
#ans_S = "atcoder"
#for i in range(len(S)):
#    tar_s = S_list[i]
#    ans_s = ans_S[i]
#    if tar_s != ans_S:
#        ii = S_list.index(ans_s)
#        res += ii-i
#        S_list.remove(ans_s)
#        S_list = S_list[:i] + [ans_s] + S_list[i:]
#
#print(res)