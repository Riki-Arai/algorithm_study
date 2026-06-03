X, Y, Z = map(int, input().split())
S = input().strip()

dp_lists = [[float("INF"), float("INF")] for _ in range(len(S))]
if S[0] == "a":
    dp_lists[0][0] = X
    dp_lists[0][1] = Z + Y
else:
    dp_lists[0][0] = Y
    dp_lists[0][1] = Z + X

for i, s in enumerate(S[1:], 1):
    if s == "a":
        dp_lists[i][0] = min(dp_lists[i-1][0]+X, dp_lists[i-1][1]+Z+X)
        dp_lists[i][1] = min(dp_lists[i-1][1]+Y, dp_lists[i-1][0]+Z+Y)
    else:
        dp_lists[i][0] = min(dp_lists[i-1][0]+Y, dp_lists[i-1][1]+Z+Y)
        dp_lists[i][1] = min(dp_lists[i-1][1]+X, dp_lists[i-1][0]+Z+X)

print(min(dp_lists[len(S)-1]))