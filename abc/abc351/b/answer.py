N = int(input())
A_list = [list(input()) for _ in range(N)]
B_list = [list(input()) for _ in range(N)]

i, j = 0, 0
for a, b in zip(A_list, B_list):
    if a != b:
        for aa, bb in zip(a, b):
            if aa != bb:
                print(i+1, j+1)
                exit()
            j += 1
    i += 1