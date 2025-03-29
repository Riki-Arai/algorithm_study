N = int(input())

for i in range(0, N+1):
    for j in range(0, N+1):
        for k in range(0, N+1):
            if i + j + k <= N:
                print(i, j, k)