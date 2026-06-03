import sys; sys.setrecursionlimit(10**7)

N = int(input()) # 数値：1

said_set = set()
for i in range(N):
    W = input().strip()
    if i == 0:
        said_set.add(W)
        pre_w = W
    else:
        if W in said_set or pre_w[-1] != W[0]:
            print("No")
            exit()
        said_set.add(W)
        pre_w = W

print("Yes")