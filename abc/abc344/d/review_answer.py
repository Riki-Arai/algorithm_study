S = input().strip()
N = int(input())

l_S = len(S)
dp_list = [float("inf")] * (l_S + 1)
dp_list[0] = 0
for _ in range(N):
    input_ = input().split()
    a = int(input_[0])
    s_list = input_[1:]

    new_dp_list = dp_list.copy()
    for s in s_list:
        l_s = len(s)
        for j in range(l_S - l_s + 1):
            if S[j:j + l_s] == s and dp_list[j] != float("inf"):
                new_dp_list[j + l_s] = min(new_dp_list[j + l_s], dp_list[j] + 1)

    dp_list = new_dp_list.copy()

res = dp_list[l_S]
print(-1 if res == float("inf") else res)


S = input().strip()
N = int(input())

l_S = len(S)
dp_list = [float("INF")]*(l_S+1)
dp_list[0] = 0
for _ in range(N):
    input_ = input().split()
    a = int(input_[0])
    s_list = input_[1:]
    new_dp_list = dp_list.copy()
    for s in s_list:
        l_s = len(s)
        for j in range(l_S, l_s-1, -1):
            if dp_list[j-l_s] != float("INF"):
                for jj in range(l_s):
                    if S[j-l_s+jj] != s[jj]:
                        break
                else:
                    new_dp_list[j] = min(dp_list[j-l_s]+1, dp_list[j])

    dp_list = new_dp_list.copy()

res = dp_list[l_S]
if res == float("INF"):
    print(-1)
else:
    print(res)