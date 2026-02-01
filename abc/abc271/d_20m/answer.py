N, S = map(int, input().split())

dp_lists = [[False, ""]] * (10**4+1)
dp_lists[0] = [True, ""]
for _ in range(N):
    a, b = map(int, input().split())
    new_dp_lists = [[False, ""]] * (10**4+1)
    for i in range(10**4, -1, -1):
        if i-a >= 0 and dp_lists[i-a][0]:
            new_dp_lists[i] = [True, dp_lists[i-a][1]+"H"]
        if i-b >= 0 and dp_lists[i-b][0]:
            new_dp_lists[i] = [True, dp_lists[i-b][1]+"T"]

    dp_lists = new_dp_lists.copy()

if dp_lists[S][0]:
    print("Yes")
    print(dp_lists[S][1])
else:
    print("No")