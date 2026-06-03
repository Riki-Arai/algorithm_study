N, Q = map(int, input().split())

b2b_list = [i for i in range(N+1)]
n2b_list = [i for i in range(N+1)]
b2n_list = [i for i in range(N+1)]
for _ in range(Q):
    query = list(map(int, input().split()))
    if query[0] == 1:
        _, a, b = query
        b2b_list[a] = n2b_list[b]
    elif query[0] == 2:
        _, a, b = query
        b_a = n2b_list[a]
        b_b = n2b_list[b]
        n2b_list[a], n2b_list[b] = b_b, b_a
        b2n_list[b_a], b2n_list[b_b] = b, a
    else:
        _, a = query
        print(b2n_list[b2b_list[a]])