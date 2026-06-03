from collections import deque

T = int(input().strip())
for _ in range(T):
    N, D = map(int, input().split()) # 取得例：1 2
    A_list = list(map(int, input().split())) # 取得例：[1,2,3]、1行の入力用
    B_list = list(map(int, input().split())) # 取得例：[1,2,3]、1行の入力用

    dq = deque()
    for d in range(N):
        a, b = A_list[d], B_list[d]
        dq.append((d, a))

        while len(dq):
            dd, a = dq.popleft()
            if a >= b:
                a -= b
                dq.appendleft((dd, a))
                break
            else:
                b -= a

        while len(dq):
            dd, a = dq.popleft()
            if d-dd < D:
                dq.appendleft((dd, a))
                break

    res = 0
    while len(dq):
        _, a = dq.popleft()
        res += a

    print(res)