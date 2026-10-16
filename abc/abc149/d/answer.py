N, K = map(int, input().split()) # 取得例：1 2
R, S, P = map(int, input().split()) # 取得例：1 2
T = input().strip()

res = 0
dp_lists = [[0, 0, 0] for _ in range(N)]
for i in range(K):
    for j in range(i, N, K):
        if j == i:
            if T[j] == "r":
                dp_lists[j][2] += P
            elif T[j] == "s":
                dp_lists[j][0] += R
            else:
                dp_lists[j][1] += S
        else:
            if T[j] == "r":
                dp_lists[j][0] = max(dp_lists[j-K][1], dp_lists[j-K][2])
                dp_lists[j][1] = max(dp_lists[j-K][0], dp_lists[j-K][2])
                dp_lists[j][2] = max(dp_lists[j-K][0]+P, dp_lists[j-K][1]+P)
            elif T[j] == "s":
                dp_lists[j][0] = max(dp_lists[j-K][1]+R, dp_lists[j-K][2]+R)
                dp_lists[j][1] = max(dp_lists[j-K][0], dp_lists[j-K][2])
                dp_lists[j][2] = max(dp_lists[j-K][0], dp_lists[j-K][1])
            else:
                dp_lists[j][0] = max(dp_lists[j-K][1], dp_lists[j-K][2])
                dp_lists[j][1] = max(dp_lists[j-K][0]+S, dp_lists[j-K][2]+S)
                dp_lists[j][2] = max(dp_lists[j-K][0], dp_lists[j-K][1])

    res += max(dp_lists[j])

print(res)