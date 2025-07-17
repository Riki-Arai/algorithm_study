# 問題が確認したいのはデータ構造かもしれないが、それよりも計算量の方に迷った問題だった
N = int(input())
Q = int(input())

box_lists = [[] for _ in range(N+1)]
card_lists = [set() for _ in range(2*10**5+1)]
for _ in range(Q):
    q = input().split()
    if q[0] == "1":
        i, j = int(q[1]), int(q[2])
        box_lists[j].append(i)
        card_lists[i].add(j)
    elif q[0] == "2":
        i = int(q[1])
        box_list = box_lists[i]
        # Σkᵢlog kᵢ ≤ Q log Qであることから計算量は結局はQlogQに抑えられる
        print(*sorted(box_list))
    else:
        i = int(q[1])
        print(*sorted(list(card_lists[i])))