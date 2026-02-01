from collections import defaultdict

N, K = map(int, input().split()) # 取得例：1 2
S = input().strip() # 取得例："A"

w_set = set()
for i in range(N-K+1):
    w_set.add(S[i:i+K])

max_v = 0
res_lists = []
for w in w_set:
    res_lists.append([0, w])
    for i in range(N-K+1):
        if S[i:i+K] == w:
            res_lists[-1][0] += 1

    max_v = max(res_lists[-1][0], max_v)

res_list = []
res_lists.sort(reverse=True)
for v, w in res_lists:
    if max_v == v:
        res_list.append(w)
    else:
        break

print(max_v)
print(*sorted(res_list))