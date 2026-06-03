import sys; sys.setrecursionlimit(10**7)

N, M, C = map(int, input().split()) # 取得例：1 2
B_list = list(map(int, input().split())) # 取得例：[1,2,3]、1行の入力用

res = 0
for _ in range(N):
    A_list = list(map(int, input().split())) # 取得例：[1,2,3]、1行の入力用
    total = 0
    for i in range(M):
        total += A_list[i]*B_list[i]

    if total+C > 0:
        res += 1

print(res)