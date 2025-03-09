N, M = list(map(int, input().split()))
a_list = [input() for _ in range(N)]
b_list = [input() for _ in range(M)]

for i in range(N - M + 1):
    for j in range(N - M + 1):
        if all([a_list[i+k][j:j+M] == b_list[k] for k in range(M)]):
            print("Yes")
            exit()
print("No")
