import sys
from bisect import bisect_left

input = sys.stdin.readline

N, M, C = map(int, input().split())
A = list(map(int, input().split()))

# 同じ地点の人数をまとめる
A.sort()

pos = []
cnt = []

for x in A:
    if pos and pos[-1] == x:
        cnt[-1] += 1
    else:
        pos.append(x)
        cnt.append(1)

K = len(pos)

# 2周分にする
pos2 = pos + [x + M for x in pos]
cnt2 = cnt + cnt

# 累積和
# pref[i] = 0 ～ i-1 番目の地点までにいる人数
pref = [0] * (2 * K + 1)

for i in range(2 * K):
    pref[i + 1] = pref[i] + cnt2[i]

ans = 0

for j in range(K):
    # 「最初に人と出会う地点」が pos[j] になる
    # スタート地点 i の個数
    if j == 0:
        gap = M - pos[-1] + pos[0]
        base = 0

        # この区間では2周目の pos[0] が最初の人
        base = N
        target = base + C

        # 2周目の pos[0] 以降で、
        # 累積人数が target 以上になる地点を探す
        idx = bisect_left(pref, target, K + 1, 2 * K + 1)

        x = pref[idx] - base
    else:
        gap = pos[j] - pos[j - 1]

        # pos[j] より前にいる人数
        base = pref[j]
        target = base + C

        idx = bisect_left(pref, target, j + 1, 2 * K + 1)

        x = pref[idx] - base

    ans += gap * x

print(ans)