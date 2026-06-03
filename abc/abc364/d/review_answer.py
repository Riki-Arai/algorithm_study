from bisect import bisect_left, bisect_right

N, Q = map(int, input().split())
A_list = list(map(int, input().split()))

A_list.sort()
for _ in range(Q):
    b, k = map(int, input().split())

    ok = 2 * 10**8 + 1
    ng = -1
    while ok-ng > 1:
        mid = (ok + ng) // 2

        left = b - mid
        right = b + mid

        cnt = bisect_right(A_list, right) - bisect_left(A_list, left)
        if cnt >= k:
            ok = mid
        else:
            ng = mid

    print(ok)