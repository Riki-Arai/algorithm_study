H, W, K = map(int, input().split())
S_lists = [list(input().strip()) for _ in range(H)]

res = float("INF")
for i in range(H):
    x_cum_list = [0]
    d_cum_list = [0]
    for j in range(W):
        s = S_lists[i][j]
        if s == "x":
            x_cum_list.append(x_cum_list[-1]+1)
            d_cum_list.append(d_cum_list[-1])
        elif s == "o":
            x_cum_list.append(x_cum_list[-1])
            d_cum_list.append(d_cum_list[-1]+1)
        else:
            x_cum_list.append(x_cum_list[-1])
            d_cum_list.append(d_cum_list[-1])

    for j in range(W-(K-1)):
        if x_cum_list[j+K]-x_cum_list[j] == 0:
            d_n = d_cum_list[j+K]-d_cum_list[j]
            res = min(max(K-d_n, 0), res)

for j in range(W):
    x_cum_list = [0]
    d_cum_list = [0]
    for i in range(H):
        s = S_lists[i][j]
        if s == "x":
            x_cum_list.append(x_cum_list[-1]+1)
            d_cum_list.append(d_cum_list[-1])
        elif s == "o":
            x_cum_list.append(x_cum_list[-1])
            d_cum_list.append(d_cum_list[-1]+1)
        else:
            x_cum_list.append(x_cum_list[-1])
            d_cum_list.append(d_cum_list[-1])

    for i in range(H-(K-1)):
        if x_cum_list[i+K]-x_cum_list[i] == 0:
            d_n = d_cum_list[i+K]-d_cum_list[i]
            res = min(max(K-d_n, 0), res)

if res == float("INF"):
    print(-1)
else:
    print(res)



H, W, K = map(int, input().split())
S = [input().strip() for _ in range(H)]

X = [0] * (max(H, W) + 1)
D = [0] * (max(H, W) + 1)
ans = float("INF")
for y in range(H):
    X[0] = 0
    D[0] = 0
    for i in range(W):
        X[i + 1] = X[i] + (S[y][i] == 'x')
        D[i + 1] = D[i] + (S[y][i] == '.')

    for i in range(W - K + 1):
        if X[i + K] - X[i] == 0:
            ans = min(ans, D[i + K] - D[i])

for x in range(W):
    X[0] = 0
    D[0] = 0
    for i in range(H):
        X[i + 1] = X[i] + (S[i][x] == 'x')
        D[i + 1] = D[i] + (S[i][x] == '.')

    for i in range(H - K + 1):
        if X[i + K] - X[i] == 0:
            ans = min(ans, D[i + K] - D[i])

print(-1 if ans > K else ans)