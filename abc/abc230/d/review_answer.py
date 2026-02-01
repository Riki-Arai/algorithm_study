n, d = map(int, input().split())
p = []
for _ in range(n):
    l, r = map(int, input().split())
    p.append((r, l))  # (r, l) の順に格納（右端でソートするため）

p.sort()
ans = 0
x = -1
for r, l in p:
    if l <= x:
        continue
    ans += 1
    x = r + d - 1

print(ans)