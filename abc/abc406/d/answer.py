from collections import defaultdict

H, W, N = map(int, input().split()) # 取得例：1 2

x2y_dict = defaultdict(set)
y2x_dict = defaultdict(set)
for _ in range(N):
    X, Y = map(int, input().split()) # 取得例：1 2
    x2y_dict[X].add(Y)
    y2x_dict[Y].add(X)

Q = int(input().strip())
for _ in range(Q):
    q, n = map(int, input().split()) # 取得例：1 2
    if q == 1:
        print(len(x2y_dict[n]))
        for y in x2y_dict[n]:
            y2x_dict[y].discard(n)
        x2y_dict[n] = set()
    else:
        print(len(y2x_dict[n]))
        for x in y2x_dict[n]:
            x2y_dict[x].discard(n)
        y2x_dict[n] = set()