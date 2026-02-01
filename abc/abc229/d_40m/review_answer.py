from collections import deque

s = input().strip()
k = int(input())
n = len(s)

cnt = [0] * (n + 1)
for i in range(n):
    cnt[i + 1] = cnt[i] + (1 if s[i] == '.' else 0)

dq = deque()
ans = 0
l = 0
for r in range(n):
    dq.append(r)
    # '.' の個数が k を超えたら左端を更新
    while dq and cnt[r+1] - cnt[l] > k:
        l = dq.popleft() + 1

    ans = max(ans, r - l + 1)

print(ans)