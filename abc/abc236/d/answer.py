import sys
sys.setrecursionlimit(10**7)

N = int(input())
A_lists = [list(map(int, input().split())) for _ in range(2*N-1)]

g_lists = [[0]*2*N for _ in range(2*N)]
for i, A_list in enumerate(A_lists):
    for j, a in enumerate(A_list, i+1):
        g_lists[i][j] = a
        g_lists[j][i] = a