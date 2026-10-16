from collections import defaultdict

N = int(input()) # 数値：1
S = input().strip() # 取得例："A"

MOD = 998244353
res = (2**N-1)%MOD
for i in range(N):
    s2i_dict = defaultdict(int)
    for j in range(i, N):
        if S[j] in s2i_dict:
            if s2i_dict[S[j]]+1 == j:
                s2i_dict[S[j]] = j
            else:
                res = (res-(N-j))%MOD
                break
        else:
            s2i_dict[S[j]] = j

print(res)

hq_list = [(0, 1)]
hq.heapify(hq_list)
res_list = [float("inf")] * (N + 1)
res_list[1] = 0
while hq_list:
    w, u = hq.heappop(hq_list)
    if w > res_list[u]:
        continue

    for c, v in g_lists[u]:
        ww = w + c
        if res_list[v] > ww:
            res_list[v] = ww
            hq.heappush(hq_list, (ww, v))