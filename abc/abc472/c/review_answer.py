from atcoder.segtree import SegTree

N, M, K = map(int, input().split())
A = list(map(int, input().split()))

def op(a, b):
    return a + b

e = 0
seg = SegTree(op, e, [0] * N)
ans = []
for i in range(N):
    # 直近 M 日間
    l = max(0, i - M + 1)

    # i 日目のおやつを食べた場合の合計
    current = seg.prod(l, i) + A[i]
    if current <= K:
        ans.append("Yes")
        seg.set(i, A[i])
    else:
        ans.append("No")
        seg.set(i, 0)

print("\n".join(ans))