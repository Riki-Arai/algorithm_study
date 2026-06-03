import heapq as hq

Q = int(input())

res_list = []
hq.heapify(res_list)
cum = 0
for _ in range(Q):
    input_ = list(map(int, input().split()))
    if input_[0] == 1:
        hq.heappush(res_list, cum)
    elif input_[0] == 2:
        T = input_[1]
        cum += T
    else:
        H = input_[1]
        res = 0
        while True:
            if len(res_list) == 0:
                break
            h = hq.heappop(res_list)
            if cum-h >= H:
                res += 1
            else:
                hq.heappush(res_list, h)
                break

        print(res)