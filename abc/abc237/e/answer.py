import heapq as hq

N, M = map(int, input().split()) # 取得例：1 2
H_list =  list(map(int, input().split()))

g_lists = [[] for _ in range(N+1)]
for _ in range(M):
    U, V = map(int, input().split()) # 取得例：1 2