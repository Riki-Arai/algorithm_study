
N, Q = map(int, input().split())
INF = float("inf")

L = [INF] + list(map(int, input().split()))
R = list(map(int, input().split())) + [INF]

# prefix[i] = R[0:i] の最小値
prefix = [INF] * (N + 1)
for i in range(N):
    prefix[i + 1] = min(prefix[i], R[i])

# suffix[i] = L[i:N] の最小値
suffix = [INF] * (N + 1)
for i in range(N - 1, -1, -1):
    suffix[i] = min(suffix[i + 1], L[i])

for _ in range(Q):
    s, t = map(int, input().split())
    s -= 1
    t -= 1

    if s < t:
        ans = min(R[s], L[s] + prefix[s])
    else:
        ans = min(L[s], R[s] + suffix[s + 1])

    print(ans)
