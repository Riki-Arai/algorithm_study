'''
(1) 一番低いものは動かすべきではないのでそちらを軸に周辺の値を決めていく
(2) 以上を低い順で繰り返すことで最終的な値が決めていけばよく、優優先付きキューで実装をしていく
(3) popする前に値が変化したものは処理をしないようにすれば良い
'''
import sys, heapq as hq
sys.setrecursionlimit(10**7)


T = int(input())
for _ in range(T):
    N = int(input())
    R_list = list(map(int, input().split()))

    dq_lists = []
    hq.heapify(dq_lists)
    for i, r in enumerate(R_list):
        hq.heappush(dq_lists, (r, i))

    res = 0
    seen_set = set()
    while len(dq_lists):
        r, i = hq.heappop(dq_lists)
        if i in seen_set and R_list[i] < r:
            continue

        seen_set.add(i)
        if i == 0:
            if R_list[i+1]-r > 1:
                res += R_list[i+1] - (r+1)
                R_list[i+1] = r + 1
                hq.heappush(dq_lists, (r+1, i+1))
                seen_set.add(i+1)
        elif i == N-1:
            if R_list[i-1]-r > 1:
                res += R_list[i-1] - (r+1)
                R_list[i-1] = r + 1
                hq.heappush(dq_lists, (r+1, i-1))
                seen_set.add(i-1)
        else:
            if R_list[i+1]-r > 1:
                res += R_list[i+1] - (r+1)
                R_list[i+1] = r + 1
                hq.heappush(dq_lists, (r+1, i+1))
                seen_set.add(i+1)

            if R_list[i-1]-r > 1:
                res += R_list[i-1] - (r+1)
                R_list[i-1] = r + 1
                hq.heappush(dq_lists, (r+1, i-1))
                seen_set.add(i-1)

    print(res)