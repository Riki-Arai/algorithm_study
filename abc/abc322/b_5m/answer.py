N, M = map(int, input().split())
S = input().strip()
T = input().strip()

rev_S = S[::-1]
rev_T = T[::-1]

if S in T:
    s_idx = T.index(S) 
else:
    s_idx = -100

if rev_S in rev_T:
    rev_s_idx = rev_T.index(rev_S) 
else:
    rev_s_idx = -100

if s_idx == 0 and rev_s_idx == 0:
    print(0)
elif s_idx == 0 and rev_s_idx != 0:
    print(1)
elif s_idx != 0 and rev_s_idx == 0:
    print(2)
else:
    print(3)