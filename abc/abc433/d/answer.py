from collections import defaultdict

N, M = map(int, input().split()) # 取得例：1 2
A_list = list(map(int, input().split()))

max_v = max(map(len, map(str, A_list)))
res = 0
res_lists = [defaultdict(int) for _ in range(max_v+2)]
for a in A_list:
    for i in range(max_v+1):
        res_lists[i+1][a*10**i%M] += 1

res = 0
for a in A_list:
    d = len(str(a))+1
    if M-a%M in res_lists[d]:
        res += res_lists[d][M-a%M]
    elif a%M == 0 and 0 in res_lists[d]:
        res += res_lists[d][0]

print(res)