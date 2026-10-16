from collections import deque

L, N1, N2 = map(int, input().split()) # 取得例：1 2

n1_dq = deque([list(map(int, input().split())) for _ in range(N1)]) # 取得例:[[1,2], [3,4]・・[9,10]]、空白区切りの数値入力
n2_dq = deque([list(map(int, input().split())) for _ in range(N2)]) # 取得例:[[1,2], [3,4]・・[9,10]]、空白区切りの数値入力

res = 0
while len(n1_dq) and len(n2_dq):
    n1_v, n1_l = n1_dq.popleft()
    n2_v, n2_l = n2_dq.popleft()
    if n1_l > n2_l:
        if n1_v == n2_v:
            res += n2_l
        n1_l -= n2_l
        n1_dq.appendleft((n1_v, n1_l))
    elif n2_l > n1_l:
        if n1_v == n2_v:
            res += n1_l
        n2_l -= n1_l
        n2_dq.appendleft((n2_v, n2_l))
    else:
        if n1_v == n2_v:
            res += n1_l

print(res)