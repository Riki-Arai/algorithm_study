N = int(input())
A_list = [input() for _ in range(N)]

for i, a in enumerate(A_list):
    if i == 0:
        print(A_list[1][0] + A_list[0][:-1])
    elif i == N - 1:
        print(A_list[i][1:] + A_list[i-1][-1])
    else:
        print(A_list[i+1][0] + A_list[i][1:-1] + A_list[i-1][-1])