import heapq as hq


Q = int(input()) # 数値：1

res_list = []
hq.heapify(res_list)
for _ in range(Q):
    q, h = map(int, input().split()) # 取得例：1 2
    if q == 1:
        hq.heappush(res_list, h)
    else:
        while len(res_list):
            hh = hq.heappop(res_list)
            if hh > h:
                hq.heappush(res_list, hh)
                break

    print(len(res_list))