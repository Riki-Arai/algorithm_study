N, K = map(int, input().split())
A = list(map(int, input().split()))

seen = {}
S = [0]
i = 0

while i not in seen:
    seen[i] = len(S) - 1
    S.append(S[-1] + A[i])
    i = (i + A[i]) % N

if K < len(S):
    print(S[K])
else:
    start = seen[i]
    length = len(S) - 1 - start
    total = S[-1] - S[start]

    q, r = divmod(K - start, length)
    print(q * total + S[start + r])