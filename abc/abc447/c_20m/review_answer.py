from collections import deque

S = input().strip() # 取得例："A"
T = input().strip() # 取得例："A"

if S.replace('A', '') == T.replace('A', ''):
    s_dq, t_dq = deque(list(S)), deque(list(T))
    res = 0
    while len(s_dq) and len(t_dq):
        s, t = s_dq.popleft(), t_dq.popleft()
        if s == t:
            continue
        elif s == "A" and t != "A":
            res += 1
            t_dq.appendleft(t)
        elif s != "A" and t == "A":
            res += 1
            s_dq.appendleft(s)

    print(res+len(t_dq)+len(s_dq))
else:
    print(-1)