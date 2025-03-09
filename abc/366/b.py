N = int(input())
s_list = [input() for _ in range(N)]
h = max([len(s) for s in s_list])
grid_list = [["*"]*N for _ in range(h)]
print(grid_list)
