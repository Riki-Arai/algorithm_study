from collections import deque

N, K = map(int, input().split())
A_list = list(map(int, input().split()))

res = 0
cum = 0
dq = deque()
for r in range(N):
    cum += A_list[r]
    dq.append(A_list[r])

    while dq and cum >= K:
        # 現在のleftを始点とする区間はright, right+1, ..., N-1 のすべてが条件を満たす
        # 左側を固定してあり得る右側を数え上げるイメージ
        res += N - r
        cum -= dq.popleft()

print(res)