S = input().strip()

MOD = 10**9+7
T = "chokudai"
dp_lists = [[0]*9 for _ in range(len(S)+1)]
for i in range(len(S)+1):
    dp_lists[i][0] = 1

for i in range(1, len(S)+1):
    ii = i-1
    for j in range(8, 0, -1):
        jj = j-1
        if S[ii] == T[jj]:
            dp_lists[i][j] = (dp_lists[ii][jj]+dp_lists[ii][j])%MOD
        else:
            dp_lists[i][j] = dp_lists[ii][j]%MOD

print(dp_lists[len(S)][8]%MOD)