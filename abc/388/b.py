N, D = list(map(int, input().split()))

s_list = []
for _ in range(N):
    s_list.append(list(map(int, input().split())))

w_list = []
for d in range(1, D+1):
    for s in s_list:
        w_list.append(s[0] * (s[1] + d))
    print(max(w_list))
