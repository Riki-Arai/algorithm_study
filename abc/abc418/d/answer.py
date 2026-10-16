N = int(input())
S = input().strip()

dp_lists = [[0, 0] for _ in range(N+1)]
for i in range(N):
    if S[i] == "0":
        dp_lists[i+1][0] = dp_lists[i][1]
        dp_lists[i+1][1] = dp_lists[i][0]+1
    else:
        dp_lists[i+1][0] = dp_lists[i][0]+1
        dp_lists[i+1][1] = dp_lists[i][1]

res = 0
for i in range(N+1):
    res += dp_lists[i][0]

print(res)