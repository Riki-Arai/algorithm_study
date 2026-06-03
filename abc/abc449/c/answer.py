import sys
from bisect import bisect_left, bisect_right
from collections import defaultdict

input = sys.stdin.readline

N, L, R = map(int, input().split())
S = input().strip()

pos = defaultdict(list)

# 文字ごとに位置を保存
for i, c in enumerate(S):
    pos[c].append(i)

ans = 0

for c in pos:
    arr = pos[c]
    m = len(arr)

    for i in range(m):
        left = arr[i] + L
        right = arr[i] + R

        l = bisect_left(arr, left)
        r = bisect_right(arr, right)

        ans += r - l

print(ans)