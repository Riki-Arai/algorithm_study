from collections import defaultdict

N, D = map(int, input().split()) # 取得例：1 2

t2n_dict = defaultdict(int)
for _ in range(N):
    S, T = map(int, input().split()) # 取得例：1 2
    if T-D+1 > S:
        t2n_dict[S] += 1
        t2n_dict[T-D+1] -= 1

if not len(t2n_dict):
    print(0)
    exit()

res = 0
res_lists = list(t2n_dict.items())
res_lists.sort(key=lambda x: x[0])
pre_t, count = res_lists[0]
for t, n in res_lists[1:]:
    if count >= 2:
        res += count*(count-1)//2 * (t-pre_t)
    count += n
    pre_t = t

print(res)