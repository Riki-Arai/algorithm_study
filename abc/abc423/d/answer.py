import sys, heapq as hq
sys.setrecursionlimit(10**7)

N, K = map(int, input().split()) # 取得例：1 2
X_lists = [list(map(int, input().split())) for _ in range(N)] # 取得例:[[1,2], [3,4]・・[9,10]]

max_a = 0
cur_k = 0
res_lists = []
hq.heapify(res_lists)
for a, b, c in X_lists:
    if cur_k+c <= K:
        max_a = max(a, max_a)
        hq.heappush(res_lists, (max_a+b, c))
        cur_k += c
        print(max_a)
    else:
        while len(res_lists) and cur_k+c > K:
            tt, cc = hq.heappop(res_lists)
            cur_k -= cc

        max_a = max(a, tt)
        hq.heappush(res_lists, (max_a+b, c))
        cur_k += c
        print(max_a)