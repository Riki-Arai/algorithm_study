import sys; sys.setrecursionlimit(10**7)

N, M = map(int, input().split()) # 取得例：1 2

cur_list = [0]*(M+1)
next_list = [0]*(M+1)
for _ in range(N):
    A, B = map(int, input().split()) # 取得例：1 2
    cur_list[A] += 1
    next_list[B] += 1

for i in range(1, M+1):
    print(next_list[i]-cur_list[i])