N, M = map(int, input().split())

max_l = [0] * (M + 1)
for _ in range(N):
    L, R = map(int, input().split())
    max_l[R] = max(max_l[R], L)

ans = 0
ng = 0
for r in range(1, M + 1):
    ng = max(ng, max_l[r])
    ans += r - ng

print(ans)