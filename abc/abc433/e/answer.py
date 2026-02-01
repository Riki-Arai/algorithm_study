N = int(input())
P_list = list(map(int,input().split()))

seen_list = [False]*N
res = 0
for s in range(N):
    if not seen_list[s]:
        length = 0
        cur = s
        while not seen_list[cur]:
            seen_list[cur] = True
            cur = P_list[cur] - 1
            length += 1

        if length > 1:
            res += length*(length-1)//2

print(res)