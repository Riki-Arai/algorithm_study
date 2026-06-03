import sys; sys.setrecursionlimit(10**7)

N = int(input()) # 数値：1

root_lists = [[None]*N for _ in range(N)]
for i in range(N-1):
    C_list = list(map(int, input().split())) # 取得例：[1,2,3]、1行の入力用
    for j, c in enumerate(C_list, i+1):
        root_lists[i][j] = c
        root_lists[j][i] = c

for a in range(N):
    for b in range(a+1, N):
        for c in range(b+1, N):
            base_root = root_lists[a][c]
            new_root = root_lists[b][a] + root_lists[b][c]
            if new_root < base_root:
                print("Yes")
                exit()

print("No")