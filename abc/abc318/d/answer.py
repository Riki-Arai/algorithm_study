N = int(input())

d_lists = [[0]*N for _ in range(N)]
for i in range(N-1):
    row = list(map(int, input().split()))
    for j, v in enumerate(row, i+1):
        d_lists[i][j] = v