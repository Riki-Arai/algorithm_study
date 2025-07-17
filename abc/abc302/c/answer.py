import itertools

N, M = map(int, input().split())
A_list = [input() for _ in range(N)]

for p in itertools.permutations(A_list):
    for i in range(len(p)-1):
        res_flag = True
        count = 0
        for j in range(len(p[i])):
            if p[i][j] != p[i+1][j]:
                count += 1
        if count != 1:
            res_flag = False

    if res_flag:
        print("Yes")
        exit()

print("No")