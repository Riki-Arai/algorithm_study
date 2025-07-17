N = int(input())
q_dict = {}
for i in range(1, N+1):
    q, r = map(int, input().split())
    q_dict[i] = (q, r)

Q = int(input())
for _ in range(Q):
    t, d = map(int, input().split())