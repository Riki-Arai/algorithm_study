from collections import deque

N = int(input())

LIMIT = 10**9
pows = []
for i in range(30):
    x = 1 << i
    digits = len(str(x))
    pows.append((x, 10 ** digits))

q = deque([0])
visited = {0}
good = set()
while q:
    cur = q.popleft()

    for x, mul in pows:
        nxt = cur * mul + x

        if nxt > LIMIT:
            continue

        if nxt not in visited:
            visited.add(nxt)
            good.add(nxt)
            q.append(nxt)

ans = sorted(good)
print(ans[N - 1])