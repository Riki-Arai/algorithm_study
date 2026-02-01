import heapq

Q = int(input().strip())

offset = 0
que = []
for _ in range(Q):
    tmp = input().split()
    type_ = int(tmp[0])
    if type_ == 1:
        X = int(tmp[1])
        # C++ で que.push(X - offset)
        heapq.heappush(que, X - offset)
    elif type_ == 2:
        X = int(tmp[1])
        offset += X
    else:  # type_ == 3
        val = heapq.heappop(que)
        # C++ で出力したのは val + offset
        print(val + offset)