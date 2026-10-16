import sys
from bisect import bisect_left, bisect_right

T = int(input().strip())

for _ in range(T):
    N, M = map(int, input().split())
    A = [x % M for x in map(int, input().split())]
    B = [x % M for x in map(int, input().split())]

    A.sort()
    B.sort()

    # (2) (ai + bi) % M == 0 となるペアを探して除外
    used_a = [False] * N
    used_b = [False] * N

    for i, a in enumerate(A):
        target = (-a) % M

        l = bisect_left(B, target)
        r = bisect_right(B, target)

        for j in range(l, r):
            if not used_b[j]:
                used_a[i] = True
                used_b[j] = True
                break

    # (3) 残った要素を大きい順に組み合わせる
    rem_a = [A[i] for i in range(N) if not used_a[i]]
    rem_b = [B[i] for i in range(N) if not used_b[i]]

    rem_a.sort(reverse=True)
    rem_b.sort()

    ans = 0
    for a, b in zip(rem_a, rem_b):
        ans += (a + b) % M

    print(ans)