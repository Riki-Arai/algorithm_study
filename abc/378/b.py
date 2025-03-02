N = int(input())
q_dic = {}
c = 1
for _ in range(N):
    q, r = list(map(int, input().split()))
    q_dic[c] = [q, r]
    c += 1

Q = int(input())
t_lists = []
for _ in range(Q):
    t_lists.append(list(map(int, input().split())))

for t_list in t_lists:
    t, d = t_list
    q, r = q_dic[t]

    for _ in range(10**9):
        if d % q == r:
            print(d)
            break
        d += 1
