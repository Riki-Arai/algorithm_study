N, Q = map(int, input().split())

for _ in range(Q):
    query = list(map(int, input().split()))
    if query[0] == 1:
        _, a, b = query
    elif query[0] == 2:
        _, a, b = query
    else:
        _, a = query