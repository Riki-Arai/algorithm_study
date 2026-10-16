'''
(1) 数が多いもものを残す確実に隣接してしまうので、優先的に左側に配置する方針が良さそう
(2) 優先度付きキューを活用して数が多いものから順番に取得する
(3) ただし現時点の末尾と一致してしまう時はもう一度キューから別の文字列を取得
'''
import sys, heapq as hq
from collections import Counter
sys.setrecursionlimit(10**7)

T = int(input()) # 数値：1

for _ in range(T):
    S = input().strip() # 取得例："A"
    n2s_lists = []
    for k, v in Counter(list(S)).items():
        n2s_lists.append((-v, k))

    res_list = []
    n2s_lists.sort()
    hq.heapify(n2s_lists)
    while len(n2s_lists):
        n, s = hq.heappop(n2s_lists)
        n *= -1
        if len(res_list):
            if res_list[-1] == s:
                if len(n2s_lists):
                    nn, ss = hq.heappop(n2s_lists)
                    nn *= -1
                    res_list.append(ss)
                    if nn-1 > 0:
                        hq.heappush(n2s_lists, (-(nn-1), ss))
                    hq.heappush(n2s_lists, (-n, s))
                else:
                    break
            else:
                res_list.append(s)
                if n-1 > 0:
                    hq.heappush(n2s_lists, (-(n-1), s))
        else:
            res_list.append(s)
            if n-1 > 0:
                hq.heappush(n2s_lists, (-(n-1), s))

        1

    if len(res_list) == len(S):
        print("Yes")
        print("".join(res_list))
    else:
        print("No")