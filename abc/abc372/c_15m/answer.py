N, Q = map(int, input().split())
S = input().strip()

res = S.count("ABC")
s_list = list(S)
for _ in range(Q):
    X, C = input().split()
    idx = int(X) - 1
    if "".join(s_list[idx-2:idx+1]) == "ABC" or (idx - 1 >= 0 and idx + 1 < N and s_list[idx-1] + s_list[idx] + s_list[idx+1] == "ABC") or "".join(s_list[idx:idx+3]) == "ABC":
        res -= 1
    s_list[idx] = C
    if "".join(s_list[idx-2:idx+1]) == "ABC" or (idx - 1 >= 0 and idx + 1 < N and s_list[idx-1] + s_list[idx] + s_list[idx+1] == "ABC") or "".join(s_list[idx:idx+3]) == "ABC":
        res += 1

    print(res)