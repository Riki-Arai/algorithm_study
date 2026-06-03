from collections import deque

T = int(input())

for _ in range(T):
    N = int(input())
    S = input().strip()
    ng_set = set()
    for i in range(len(S)):
        if S[i] == "1":
            ng_set.add(i+1)

    goal = 0
    for i in range(N):
        goal |= 1 << i

    dq = deque()
    seen_set = set()
    for i in range(N):
        if 1 << i not in ng_set:
            dq.append(1 << i)

    while len(dq):
        bit_n = dq.popleft()
        if bit_n == goal:
            print("Yes")
            break
        for n in range(N):
            bit_nn = bit_n | 1 << n
            if bit_nn not in ng_set and bit_nn not in seen_set:
                seen_set.add(bit_nn)
                dq.append(bit_nn)
    else:
        print("No")



from collections import deque

T = int(input())

for _ in range(T):
    N = int(input())
    S = input().strip()

    goal = (1 << N) - 1

    if S[goal - 1] == '1':
        print("No")
        continue

    dq = deque([0])
    seen = {0}
    res_list =  [False for _ in range(2 ** N + 1)]
    while dq:
        s = dq.popleft()
        for i in range(N):
            ns = s | (1 << i)
            if ns not in seen and S[ns - 1] == '0':
                res_list[ns] = True
                seen.add(ns)
                dq.append(ns)

    if res_list[2 ** N-1]:
        print("Yes")
    else:
        print("No")