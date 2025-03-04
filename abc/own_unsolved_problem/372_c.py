N, Q = map(int, input().split())
S = list(input())
cnt = 0

for i in range(N-2):
    if S[i] == "A" and S[i+1] == "B" and S[i+2] == "C":
        cnt += 1

for _ in range(Q):
    x, c = input().split()
    x = int(x)

    if x >= 2 and x <= N-1 and S[x-2] == "A" and S[x-1] == "B" and S[x] == "C":
        cnt -= 1
    if x >= 1 and x <= N-2 and S[x-1] == "A" and S[x] == "B" and S[x+1] == "C":
        cnt -= 1
    if x >= 3 and x <= N and S[x-3] == "A" and S[x-2] == "B" and S[x-1] == "C":
        cnt -= 1

    S[x-1] = c

    if x >= 2 and x <= N-1 and S[x-2] == "A" and S[x-1] == "B" and S[x] == "C":
        cnt += 1
    if x >= 1 and x <= N-2 and S[x-1] == "A" and S[x] == "B" and S[x+1] == "C":
        cnt += 1
    if x >= 3 and x <= N and S[x-3] == "A" and S[x-2] == "B" and S[x-1] == "C":
        cnt += 1

    print(cnt)

