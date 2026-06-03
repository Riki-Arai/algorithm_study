from collections import deque


T = int(input()) # 数値：1

for _ in range(T):
    N, D = map(int, input().split()) # 取得例：1 2
    A_list = list(map(int, input().split())) # 取得例：[1,2,3]、1行の入力用
    B_list = list(map(int, input().split())) # 取得例：[1,2,3]、1行の入力用

    dq = deque()
    day = 0
    for a, b in zip(A_list, B_list):
        day += 1
        dq.append((a, day))
        while b > 0:
            aa, d = dq.popleft()
            if aa-b >= 0:
                dq.appendleft((aa-b, d))
                b = 0
            else:
                b -= aa

        if day-dq[0][1] >= D:
            dq.popleft()

    res = 0
    while len(dq):
        aa, d = dq.popleft()
        res += aa

    print(res)