M = int(input())
D_list = list(map(int, input().split()))

mid = (sum(D_list) + 1) / 2
for i, d in enumerate(D_list, 1):
    if mid > d:
        mid -= d
    else:
        print(i, int(mid))
        exit()